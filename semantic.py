import spacy
nlp = spacy.load('en_core_web_md')


""" 
Code extract 1:
I think it's interesting that "cat" and "monkey" score the highest out of the 3 comparisons. I guess this is because they are both mammals
"Banana" and "Cat" are the least similar out of the 3 comparisons. This is likey because Cats don't eat Bananas and Bananas aren't mammals.
"""
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(f"{word1} + {word2}: {word1.similarity(word2)}")
print(f"{word3} + {word2}: {word3.similarity(word2)}")
print(f"{word3} + {word1}: {word3.similarity(word1)}")
print()

"""
My Own Examples: Rain/Snow got a similarity score of 0.76 which was quite expected
However, cloud/snow and cloud/rain both got 0.34. I thought they were more similar than that
"""

word1 = nlp("rain")
word2 = nlp("snow")
word3 = nlp("cloud")

print(f"{word1} + {word2}: {word1.similarity(word2)}")
print(f"{word3} + {word2}: {word3.similarity(word2)}")
print(f"{word3} + {word1}: {word3.similarity(word1)}")
print()

"""
I ran the 'example.py both with SM and MD to see how the results were different. 

I found that md returned a higher similarity score. Perhaps this is because sm is 'simpler'?

It goes to show that it is worth using different language models.
"""