'''
Created on 03 avr. 2014

@author: Alexis Focheux
'''

# import sys
import itertools

fichier = open('A-small-attempt0.in', 'r')
resFile = open('A.txt', 'w')
T = int(fichier.readline().strip());

for testcase in range(T):
    nS = int(fichier.readline().strip())
    S = []
    for _i in range(nS):
        S.append(fichier.readline().strip())
    if len(set([''.join(ch for ch, _ in itertools.groupby(ele)) for ele in S])) != 1:
        resFile.write('Case #' + str(testcase + 1) + ': ' + 'Fegla Won' + '\n');
        continue
    
    Sn=[]
    for ele in S:
        w=[]
        print(ele)
        prevLetter = ele[0]
        compteur = 0
        for letter in ele:
            if letter == prevLetter:
                compteur += 1
            else:
                w.append(compteur)
                compteur = 1
                prevLetter = letter
        w.append(compteur)
        Sn.append(w)
    print(Sn)
    
    p = 0 
    for i in range(len(Sn[0])):
        var = 0
        for j in range(len(Sn)):
            var += Sn[j][i]
        median = int(var / len(Sn))   
        for j in range(len(Sn)):
            p += abs(Sn[j][i] - median)          
            
    resFile.write('Case #' + str(testcase + 1) + ': ' + str(p) + '\n');
    