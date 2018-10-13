#! /usr/bin/env python

'''
Created on 14/04/2012

@author: solid
'''

import sys

def getScores(number):
    scores = []
    factorial = (number % 3)/3
    if(factorial < 0.5):
        score_base = int(number/3) 
    else:
        score_base = int(number/3) + 1
    
    scores.append(score_base) 
    scores.append(score_base) 
    scores.append(number - 2*score_base) 
    
    scores.sort()
    scores.reverse()
    return scores

def getSurpriseScores(scores):
    if(0 <= scores[0] < 10 and 0 < scores[1] and scores[0] == scores[1]):
        scores[0] += 1
        scores[1] -=1
    elif(0 <= scores[1] < 10 and 0 < scores[2]):
        scores[1] += 1
        scores[2] -= 1
    
    scores.sort()
    scores.reverse()
    return scores

def processFile(inputFile):
    #initializes
    maxscores = []
    maxSurpriseScores = []
    
    for i in range(0,31):
        scores = getScores(i)
        maxscores.append(scores[0])        
        maxSurpriseScores.append(getSurpriseScores(scores)[0])
    
    fileR = open(inputFile)
    fileW = open("dancing.out","w")
    cases = fileR.readline()
    cases = cases[:len(cases)-1]
    cases = int(cases)
    
    for i in range(0,cases):
        number = 0
        line = fileR.readline()
        line = line.split(" ")        
        surprises = int(line[1])        
        p = int(line[2])
        scores = line[3:]       
        
        
        for score in scores:
            maxScore = maxscores[int(score)]
            maxSurprise = maxSurpriseScores[int(score)]
            if(maxScore >= p):
                number +=1
            elif(surprises > 0 and maxSurprise >= p):
                number += 1
                surprises -= 1
        result = "Case #{0}: {1}\n".format(i+1,number)
        fileW.write(result)
    
def main():
    inputFile = False
    try:
        inputFile = sys.argv[1]
    except IndexError:
        return 
    if(inputFile):
        processFile(inputFile)
    
if __name__ == '__main__':
    main()