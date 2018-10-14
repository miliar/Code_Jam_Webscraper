#-------------------------------------------------------------------------------
# Name:        ??????1
# Purpose:
#
# Author:      myegor
#
# Created:     07.05.2011
# Copyright:   (c) myegor 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def check_tail(x,c):
    if len(x) <= 1:
        return False
    a = x[-1]
    b = x[-2]
    for i in c:
        if (i[0]==a and i[1]==b) or (i[0]==b and i[1]==a):
            del x[-1]
            del x[-1]
            x.append(i[2])
            return True
    return False

def check_del(x,d):
    if len(x) <= 1:
        return (x,False)
    for i in d:
        try:
            a = x.index(i[0])
            b = x.index(i[1])
        except ValueError:
            continue
        if a != -1 and b != -1:
#            if a > b:
#                (a,b) = (b,a)
#            res = []
#            for z in range(len(x)):
#                if z < a or z > b:
#                    res.append(x[z])
            return ([],False)
    return (x,False)

def print_list(x):
    if len(x) == 0:
        return '[]'
    res = '[' + x[0];
    for i in range(1,len(x)):
        res = res + ', ' + x[i];
    res = res + ']'
    return res;

input = open('data1.txt','r')

testnum = int(input.readline())

for t in range(testnum):

    line = input.readline().split()
    cn = int(line[0])
    c = []
    for i in range(cn):
        c.append(line[i+1])
    dn = int(line[cn+1])
    d = []
    for i in range(dn):
        d.append(line[cn+i+1+1])
    nn = int(line[cn+dn+1+1])
    n = line[cn+dn+1+1+1]
    res = [];
    for i in n:
        res.append(i)
        while check_tail(res,c) == True: pass
        cont = True
        while cont:
            (res,cont) = check_del(res,d)
    print "Case #"+str(t+1)+": "+print_list(res)


input.close()