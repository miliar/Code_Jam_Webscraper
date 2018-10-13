#!/usr/bin/python
__author__ = 'sbuono'

import sys

dic = {x: {x: '0' for x in 'n1ijkIJK'} for x  in 'n1ijkIJK'}

dic['n']['i'] = 'I'
dic['n']['j'] = 'J'
dic['n']['k'] = 'K'
dic['1']['i'] = 'i'
dic['1']['j'] = 'j'
dic['1']['k'] = 'k'
dic['i']['i'] = 'n'
dic['i']['j'] = 'k'
dic['i']['k'] = 'J'
dic['j']['i'] = 'K'
dic['j']['j'] = 'n'
dic['j']['k'] = 'i'
dic['k']['i'] = 'j'
dic['k']['j'] = 'I'
dic['k']['k'] = 'n'
dic['I']['i'] = '1'
dic['I']['j'] = 'K'
dic['I']['k'] = 'j'
dic['J']['i'] = 'k'
dic['J']['j'] = '1'
dic['J']['k'] = 'I'
dic['K']['i'] = 'J'
dic['K']['j'] = 'i'
dic['K']['k'] = '1'



def compute(tofind, char, str, offset) :

    print "Compute:", char

    cur = '1'
    i = offset
    while i < (len(str) - (2 - char)):

        cur = dic[cur][str[i]]

        if cur == tofind[char] :
            if char == 2 and (i == (len(str) - 1)) :
                return True
            elif char < 2 and compute(tofind, char + 1, str, i + 1) :
                return True

        i += 1
    return False

def findAllI(str) :

    list = []
    cur = '1'
    i = 0
    while i < (len(str) - 2):

        cur = dic[cur][str[i]]

        if cur == 'i' :
            list.append(i)
        i += 1

    return list

def findAllK(str) :

    list = []
    l = len(str)
    i = l

    while i > 1 :

        cur = '1'
        j = i
        while j < l :
            cur = dic[cur][str[j]]
            j += 1

        if cur == '1' :
            l = i
        if cur == 'k' :
            list.append(i)
            l = i
            break

        i -= 1
    if i == 1 :
        return []
    while i > 1 :

        cur = '1'
        j = i
        while j < l :
            cur = dic[cur][str[j]]
            j += 1

        if cur == '1' :
            list.append(i)
            l = i

        i -= 1

    return list

def isItJ(str, offset1, offset2, res) :
    cur = res
    i = offset1
    while i < offset2 :

        cur = dic[cur][str[i]]

        i += 1

    if cur == 'j' :
        return True, cur
    return False, cur

f = open(sys.argv[1])

nbTestCases = f.readline().strip()

case = 1

lines = f.readlines()

for i in range(0, len(lines), 2) :

    rep = False

    tmp = lines[i].strip().split()
    L = int(tmp[0])
    X = int(tmp[1])
    str = lines[i+1].strip()

    redux = 4
    h = X % redux
    newX = (h + redux) if (h + redux) < X else X
    str = str * newX
    # print newX
    # str = str * X

    tofind = "ijk"

    listi = findAllI(str)
    listk = findAllK(str)
    listk.reverse()

    # print len(listi), len(listk)

    for i in listi :
        res = '1'
        lastk = i + 1
        for k in listk :
            if k - i > 0 :
                succ, res = isItJ(str, lastk, k, res)

                if succ == True :
                    rep = True
                    break

                lastk = k
            if rep == True :
                break
        if rep == True :
                break

    if rep == True :
        print "Case #%d:" % (case), "YES"
    else :
        print "Case #%d:" % (case), "NO"

    case += 1