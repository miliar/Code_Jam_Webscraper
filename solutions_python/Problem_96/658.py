'''
Created on Apr 13, 2012

@author: aaron
'''
import sys

class Scores:
    def __init__(self, line):
        values = line.split(' ')
        num_googlers = int(values[0])
        self.num_suprise = int(values[1])
        self.pThresh = int(values[2])
        self.scores = tuple(int(value) for value in values[3:])
        if len(self.scores)!=num_googlers:
            raise Exception("Invalid number of scores")
    
    def computeMaxFreq(self):
        maxNoSuprise=0
        numCanImprove=0
        for score in self.scores:
            bestBest=Scores.getBestBest(score, False)
            if bestBest>=self.pThresh:
                maxNoSuprise+=1
            elif bestBest+1>=self.pThresh and Scores.canImprove(score):
                numCanImprove+=1
        return maxNoSuprise+min(numCanImprove, self.num_suprise)
        
    
    @staticmethod
    def getBestBest(score, isSuprising):
        if isSuprising:
            return (score+1)//3+1
        else:
            return (score+2)//3
    
    @staticmethod
    def canImprove(score):
        if score//3==0 and score%3==0:
            return False
        if Scores.getBestBest(score, True)>10:
            return False
        return score%3!=1

def readScoresFromFile(infile):
    lines=infile.readlines()
    if int(lines[0])!=len(lines)-1:
        raise Exception("Invalid number of test cases")
        exit(1)
    return tuple(Scores(line) for line in lines[1:])

def writeOutput(caseNum, output, outfile):
    outfile.write("Case #{0}: {1}\n".format(caseNum, output))

if __name__ == '__main__':
    infile = open("B-large.in")
    outfile = open("output.txt", 'w')
    scoresList = readScoresFromFile(infile)
    for i,scores in enumerate(scoresList):
        writeOutput(i+1, scores.computeMaxFreq(), outfile)
        
    