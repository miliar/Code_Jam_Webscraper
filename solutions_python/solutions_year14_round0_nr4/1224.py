'''
Created on 12 avr. 2014

@author: Alexis Focheux
'''

# import sys

fichier = open('D-large.in', 'r')
resFile = open('D.out', 'w')
T = int(fichier.readline().strip());

for testcase in range(T):
    print("============================================================")
    N=int(fichier.readline().strip())
    Naomi =[float(ele) for ele in fichier.readline().split()]
    Ken =[float(ele) for ele in fichier.readline().split()]
    Naomi.sort(key=None, reverse=False)
    Ken.sort(key=None, reverse=False)
    print (Naomi)
    print (Ken)
    print("------------------------------------------------------------")
    scoreLegit = 0
    scoreCheat = 0    
    length = N
    Temp = list(Ken)
    
    
    for i in range(N):
        j = 0
        for ele in Ken:
            if Naomi[i] < ele:
                j = Ken.index(ele)
                break
        if Naomi[i] > Ken[j]:
            scoreLegit += 1
            Ken.pop(0)
        else:
            Ken.pop(j)

    Ken = list(Temp)
#     print(Ken[0])
#     print(Naomi[0])$
    for ele in Naomi:
        if ele < Ken[0]:
            Ken.pop(-1)
        else:
            scoreCheat += 1
            Ken.pop(0)

    
    print(testcase,N,scoreCheat,scoreLegit)
    resFile.write('Case #' + str(testcase + 1) + ': ' + str(scoreCheat) + ' '  + str(scoreLegit) + '\n');
