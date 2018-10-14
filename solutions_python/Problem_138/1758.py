#!/usr/bin/python
import sys

from random import randint,randrange
import random
import sys, getopt
import argparse
import numpy as np
import copy

def second_largest(numbers):
    first, second = None, None
    for n in numbers:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second

f= open("4.txt", "r")

numCases=int(f.readline().rstrip('\n'))
case=0

while True:

    case +=1
    if case > numCases:
       break
    
    N  = int(f.readline().rstrip('\n'))
    Naomi  = f.readline().rstrip('\n')
    Naomi = Naomi.split(' ')
    Naomi = [float(x) for x in Naomi]
    Naomi2 = copy.deepcopy(Naomi)

    Ken  = f.readline().rstrip('\n')
    Ken = Ken.split(' ')
    Ken = [float(x) for x in Ken]
    Ken2 = copy.deepcopy(Ken)
    

    if not Ken2: break 
    KenScore=0
    KenScore2=0
    NaomiScore=0
    NaomiScore2=0
    num = 1
    #print "Playing Deceitful War"
    while num <= N:
      num += 1
    
      MaxKen = max(Ken)
      MinKen = min(Ken)
      MaxNaomi=max(Naomi)
      MinNaomi = min(Naomi)
      #print "Naomi is " + str(Naomi)

      #print "Ken is " + str(Ken)
      SecondMaxKen=second_largest(Ken)
      #print "SecondMaxKen is " + str(SecondMaxKen)


      if MaxNaomi < MaxKen:
        ChosenNaomi = MinNaomi
        if len(Ken) >= 2: 
          ToldNaomi = (MaxKen - SecondMaxKen)/2 + SecondMaxKen
        else:
          ToldNaomi = MaxKen-0.0001

      else:
        tmpMin=[]
        for block in Naomi:
           if block > MaxKen:
             tmpMin.append(block)

        ChosenNaomi=min(tmpMin)
        ToldNaomi=ChosenNaomi
        

      Naomi.remove(ChosenNaomi)
      #print "ToldNaomi is " + str(ToldNaomi)

      tmp=[]

      for block in Ken:
        if block > ToldNaomi:
           tmp.append(block)

      if len(tmp) > 0:
         ChosenKen=min(tmp)
      else:
         ChosenKen=MaxKen
      #print "ChosenNaomi is " + str(ChosenNaomi)
      #print "ChosenKen is " + str(ChosenKen)

      Ken.remove(ChosenKen)

      if ChosenKen > ChosenNaomi:
         KenScore+=1
      else:
         NaomiScore +=1

    firstString="Case #" + str(case) + ": " + str(NaomiScore)
    num = 1
    #print "Now playing Optimal War"
    while num <= N:
      num += 1

      MaxKen = max(Ken2)
      MinKen = min(Ken2)
      MaxNaomi=max(Naomi2)
      MinNaomi = min(Naomi2)

      ChosenNaomi = MaxNaomi
      Naomi2.remove(ChosenNaomi)

      #print "Before search, Ken is " + str(Ken2)
      tmp=[]
      for block in Ken2:
        if block > ChosenNaomi:
           tmp.append(block)

      if len(tmp) == 0:
         ChosenKen=MinKen
      else:
         ChosenKen=min(tmp)
      #print "Min is " + str(ChosenKen)
      #print "Ken2 is " +str(Ken2)

      Ken2.remove(ChosenKen)
      #print "Removed  " +str(ChosenKen)
      #print "Ken2 is now " +str(Ken2)

      if ChosenKen > ChosenNaomi:
         KenScore2+=1
      else:
         NaomiScore2 +=1

    finalString = firstString + " " + str(NaomiScore2)
    print finalString
