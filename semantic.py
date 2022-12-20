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

"""
Code extract 2: Running these loops it is really interesting to see the similarity scores.
Somethings are really unexpected. For example, in the second loop, "pigeon" and "chicken"
only score 0.3, which is a lot lower than what I would have guessed considering they are both birds.
"""
tokens = nlp("cat apple monkey banana ")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print()

tokens = nlp("chicken soup chocolate pigeon ")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print()

"""
Code extract 3: In this extract, I can see that this would be really useful for search engines. It can take the user's input and return the high
scoring similarities.
"""
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)