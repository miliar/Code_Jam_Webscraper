'''
Created on 12 avr. 2014

@author: Alexis Focheux
'''

# import sys

fichier = open('input.txt', 'r')
resFile = open('A.txt', 'w')
T = int(fichier.readline().strip());

for testcase in range(T):
    answer = int(fichier.readline().strip())
    for i in range(1, 5):
        temp = fichier.readline().split()
        if i == answer:
            sol = temp

    answer = int(fichier.readline().strip());
    for i in range(1, 5):
        temp = fichier.readline().split()
        if i == answer:
            check = temp
            
    res = list(set(check) & set(sol))
    l = len(res)

    if l == 1:
        resFile.write('Case #' + str(testcase + 1) + ': ' + res[0] + '\n');
    elif l > 1:
        resFile.write('Case #' + str(testcase + 1) + ': Bad magician!\n');
    else:
        resFile.write('Case #' + str(testcase + 1) + ': Volunteer cheated!\n');
