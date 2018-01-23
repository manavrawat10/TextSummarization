# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:28:56 2018

@author: Manvenddra
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stopWords = set(stopwords.words("english"))
text="""
There are so many lessons one can learn about life from a dog. Imagine this scenario: it is raining heavily outside and you need to leave for someone's house. The dog is up and eager, to go with you. You tell it to stay home. As you leave, you see it squeezing out through the gap in the doorway. You scold it and order it back home. Then at every turn you make, you suddenly see it following you sheepishly at a distance. It follows at the risk of being reprimanded for the sore reason of being somewhere nearby. How else can we experience so selfless an instance of love and faithfulness? We can learn a lifelong lesson from this sincere warm display of perpetual companionship.
Observe the eating habits of your dog. It does not eat, except when hungry. It does not drink, unless it is thirsty. It does not gorge itself. It stops eating when it has had enough.

A dog also sets a perfect example of adaptability. If it is moved to a strange place, it is able to adapt itself to that place and to its thousand peculiarities without a murmur of complaint. It is able to learn and adapt to a new family's ways and customs. It is quick and ready to please. Man, being accustomed to comfort and wealth will be lost if suddenly stripped of all he is accustomed to.

A dog also teaches us a thing or two about, unselfish love. When a dog knows death is approaching, it tries, with its last vestige of strength, to crawl away elsewhere to die, in order to burden its owners no more.

A dog does things with all vigor. However, when there is nothing to do, it lies down and rests. It does not waste its strength and energy needlessly. Many working people are burning the candles at both ends. Many suffer nervous breakdowns due to stress. Perhaps, they should learn to rest like a dog does.

A dog above all is truly man's best friend. 
"""
words = word_tokenize(text)
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
sentences = sent_tokenize(text)
#print(sentences)
print(freqTable)
sentenceValue = dict()
for sentence in sentences:
    for wordValue in freqTable:
        #print(wordValue)
        if wordValue in sentence:
            if sentence in sentenceValue:
                sentenceValue[sentence]+=freqTable[wordValue]
            else:
                sentenceValue[sentence]=freqTable[wordValue]
print(sentenceValue)
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
print(sumValues)
# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))
print(average)
summary = ''
for sentence in sentences:
        if sentence in sentenceValue and sentenceValue[sentence] > (1.5 * average):
            summary +=  " " + sentence
print(summary)