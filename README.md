# Spell_Checker
A spell checker that give the correct spelling for a misspelt word

HEURISTIC DESIGN:  
 
1. Word Length Similarity 
Prioritise the suggestions with the same length as the misspelt word. 
For example, the misspelt word “wale” has the same length of words suggestions 
{“wide”, “area”, “glad”}, we can ignore other suggestions {“light”, “narrow”} 
 
 
2. Character frequency 
For each word in the dictionary get the count of the occurrence of the same 
characters. 
For example, for the misspelt word “wode” the count of the same character 
occurrence is 3 for “wide” but 1 for “area”, so we can prioritise “wide”. 
 
 
3. Position check 
Prioritise words with the most similar character index. 
For example, “arean” and “area” have the same characters in the same index 4 
times. 
 
 
4. Scoring heuristic 
a. Word Length Similarity (30% weight) 
Binary score: 1.0 if lengths match, 0.0 if they don't 
 
b. Character Frequency Matching (30% weight) 
 
c. Position Matching (40% weight) 
 
The final score is between 0 and 1, where: 
 
1.0 means a perfect match 
0.0 means no similarity at all 
Scores above 0.5 are considered potential matches
