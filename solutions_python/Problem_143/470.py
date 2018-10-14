'''
Created on 03 avr. 2014

@author: Alexis Focheux
'''

# import sys

fichier = open('B-small-attempt0.in', 'r')
resFile = open('B.out', 'w')
T = int(fichier.readline().strip());

for testcase in range(T):
    [A,B,K]=[int(ele) for ele in fichier.readline().split()]

    compteur = 0
    for a in range(A):
        for b in range (B):
            if (a&b) < K:
                compteur += 1
    print(compteur)

    resFile.write('Case #' + str(testcase + 1) + ': ' + str(compteur) + '\n');
