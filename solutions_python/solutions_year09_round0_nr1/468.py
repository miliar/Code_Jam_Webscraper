#! /usr/bin/python
import sys

#nacteni 2 cisel
numbers = sys.stdin.readline()[:-1].split()
l = int(numbers[0])
d = int(numbers[1])
n = int(numbers[2])

dict = []
actual_dict = 0
while actual_dict < d:
    actual_dict += 1
    word = sys.stdin.readline()[:-1]
    dict.append(word)

dict.sort()

cases = n
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    #nacteni 1 cisla
    text = sys.stdin.readline()[:-1]
    
    textt = text.split(')')

    letters = []
    if len(textt) == 1:
        if textt[0] == text:
            for j in list(text):
                letters.append([j])
        else:
            new_pom = i.split('(')
            if len(new_pom) == 2:
                for j in list(new_pom[0]):
                    letters.append([j])
            letters.append(list(new_pom[1]))
    else:
        new = []
        for i in textt: 
            new.append(i.split('('))
        letters = []
        #first differently
        if (len(new[0]) != 1):
            for j in list(new[0][0]):
                letters.append([j])
        letters.append(list(new[0][1]))
        for i in range(1,len(new)-1):
            for j in list(new[i][0]):
                letters.append([j])
            letters.append(list(new[i][1]))
        #last differently
        last = len(new)-1
        for j in list(new[last][0]):
            letters.append([j])
        if (len(new[last]) != 1):
            letters.append(list(new[last][1]))


    #def f(s): return ((s[0] in ['s','f']) and (s[1] in ['e','d']))
    def f(s):
        so_far = True
        total = l
        count = 0
        while so_far and count < total:
            so_far = s[count] in letters[count]
            count += 1
        return so_far

    #print filter(f,dict)

    print "Case #%d: %d" %(actual_case,len(filter(f,dict)))
