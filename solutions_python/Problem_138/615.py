'''
Created on Apr 12, 2014

@author: di
'''
import sys

def getWarScore(Naomi,Ken,N):
    Ni = 0
    Ki = 0
    score = 0
    while Ki < N:
        if  Naomi[Ni] < Ken[Ki]:
            Ni += 1
            Ki += 1
            score += 1
        else:
            Ki += 1
    return N - score    
    
def getDWarScore(Naomi,Ken,N):
    Ni = N - 1
    Ki = N - 1
    score = 0
    
    while Ki >= 0:
        if Naomi[Ni] > Ken[Ki]:
            Ni -= 1
            Ki -= 1
            score += 1
        else:
            Ki -= 1
    return score 

casesnum = (int)(sys.stdin.readline());

case = 1
Naomi = list()
Ken = list()
score_W = 0;
score_DW = 0;

while case <= casesnum:
    N = (int)(sys.stdin.readline());
    Naomi = sorted([float(x) for x in sys.stdin.readline().split()])
    Ken = sorted([float(x) for x in sys.stdin.readline().split()])
    
    score_W =  getWarScore(Naomi,Ken,N)
    score_DW = getDWarScore(Naomi,Ken,N)
    
    print "Case #"+str(case)+": " + str(score_DW) + " "+ str(score_W)
    case += 1
    