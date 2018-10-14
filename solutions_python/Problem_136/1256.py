'''
Created on 12 avr. 2014

@author: Alexis Focheux
'''

# import sys

fichier = open('B-large.in', 'r')
resFile = open('B.out', 'w')
T = int(fichier.readline().strip());

for testcase in range(T):
    [C,F,X]=[float(ele) for ele in fichier.readline().split()]
    income = float(2)
    timeSpent = float(0) 
    flag = 1
    
    while(flag):
        currentTime = X / income + timeSpent
        estimatedTime = C / income + X / (income + F) + timeSpent
        if (currentTime > estimatedTime):
            timeSpent += C / income
            income = income + F            
        else:
            flag = 0
    resFile.write('Case #' + str(testcase + 1) + ': ' + str(currentTime) + '\n');
