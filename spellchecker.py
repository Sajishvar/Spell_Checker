from collections import Counter

def load_dictionary(file_path):
    # Load words from a dictionary file
    with open(file_path, 'r') as file:
        dictionary = set(line.strip().lower() for line in file)
    return dictionary

def word_length_similarity(misspelt_word, candidate_word):
    # Binary score: 1.0 if lengths match, 0.0 if they don't
    return 1.0 if len(misspelt_word) == len(candidate_word) else 0.0

def character_frequency_similarity(misspelt_word, candidate_word):
    # Count frequency of each character in both words
    misspelt_counter = Counter(misspelt_word)
    candidate_counter = Counter(candidate_word)
    # Compute sum of minimum matches for each character
    matching_count = sum(min(misspelt_counter[char], candidate_counter[char]) for char in misspelt_counter)
    # Normalize by the length of the misspelt word
    return matching_count / len(misspelt_word)

def position_similarity(misspelt_word, candidate_word):
    # Count matching characters at the same positions
    match_count = sum(1 for m_char, c_char in zip(misspelt_word, candidate_word) if m_char == c_char)
    # Normalize by the length of the shorter word to avoid penalizing due to different lengths
    return match_count / min(len(misspelt_word), len(candidate_word))

def calculate_similarity_score(misspelt_word, candidate_word):
    # Weights
    weight_length = 0.3
    weight_frequency = 0.3
    weight_position = 0.4
    
    # Heuristic scores
    length_score = word_length_similarity(misspelt_word, candidate_word)
    frequency_score = character_frequency_similarity(misspelt_word, candidate_word)
    position_score = position_similarity(misspelt_word, candidate_word)
    
    # Weighted sum of the scores
    return (weight_length * length_score + 
            weight_frequency * frequency_score + 
            weight_position * position_score)

def suggest_corrections(misspelt_word, dictionary, threshold=0.5):
    # Calculate similarity scores for each word in the dictionary
    scored_candidates = [
        (candidate, calculate_similarity_score(misspelt_word, candidate))
        for candidate in dictionary
    ]
    # Filter candidates with scores above threshold
    scored_candidates = [(word, score) for word, score in scored_candidates if score > threshold]
    # Sort by score in descending order
    scored_candidates.sort(key=lambda x: x[1], reverse=True)
    
    return scored_candidates

# Example usage
dictionary_file = 'words.txt'
misspelt_word = 'arean'

# Load dictionary
dictionary = load_dictionary(dictionary_file)

# Get suggestions
suggestions = suggest_corrections(misspelt_word, dictionary)

# Print suggestions
for word, score in suggestions:
    print(f"Suggested word: {word}, Score: {score:.2f}")
