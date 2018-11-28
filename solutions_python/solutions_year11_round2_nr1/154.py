'''
Created on May 8, 2011

@author: Guy
'''
import numpy as np


class Team:
    def __init__(self,idx,games):
        self.RPI = 0
        self.WP=0
        self.OWP=0
        self.OOWP=0
        
        self.numGames = 0
        self.numWins = 0
        self.idx = idx
        self.games = games
        self.opponents = set()
        self.calcWins()
    
    def calcWins(self):
        self.numWins=0
        self.numGames=0
        self.opponents = set()
        for i in xrange(len(self.games)):
            if self.games[i]!='.': 
                self.numGames+=1
                self.opponents.add(i)
            if self.games[i]=='1': self.numWins+=1
        self.WP=self.numWins/float(self.numGames)
    
    def calcOWP(self,teams):
        tot = 0
        for opp in self.opponents:
            if self.games[opp]=='1': #beat this opponent, numwins remains unchanged
                tot+=teams[opp].numWins/float(teams[opp].numGames-1)
            else: #has lost to this opponent, reduce his numwins by 1 when calculating
                tot+=(teams[opp].numWins-1)/float(teams[opp].numGames-1)
        self.OWP = tot/len(self.opponents)
    
    def calcOOWP(self,teams):
        tot = 0
        for opp in self.opponents:
            tot+=teams[opp].OWP
        self.OOWP = tot/len(self.opponents)
        
    def calcRPI(self):
        self.RPI = 0.25*self.WP+0.50*self.OWP+0.25*self.OOWP
            
            
    
    
        
    


def processInput(inFileName,outFileName):
    f = open(inFileName)
    fo = open(outFileName,'w')
    numLines = int(f.readline().rstrip())
    for i in xrange(numLines):
        z =  'Case #' + str(i+1) +':'
        print z
        fo.write(str(z)+'\n')
        teams = []
        numTeams = int(f.readline().rstrip())
        for j in xrange(numTeams):
            teams.append(Team(j,f.readline().rstrip()))
        for j in xrange(numTeams):
            teams[j].calcOWP(teams)
        for j in xrange(numTeams):
            teams[j].calcOOWP(teams)
            teams[j].calcRPI()
            z =  teams[j].RPI
            print z
            fo.write(str(z)+'\n')
            

#Any text file will do - such as 'problemNameOut.txt'
processInput('A-large.in','largeOut.txt')