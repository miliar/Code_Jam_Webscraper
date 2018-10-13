#!/usr/bin/python

text = raw_input()
input = text.split(" ")

s = {}
for i in range(0, int(input[1])):
    string = raw_input()
    s[string] = 1

for i in range(0, int(input[2])):
    c = raw_input()
    d = [[0] for row in range(int(input[0]))]
    j = 0
    flag = False
    for cc in c:
        if cc == '(':
            flag = True
        elif cc == ')':
            j += 1
            flag = False
        else:
            d[j] += cc
            if flag == False:
               j += 1

    res = 0
    for key in s:
        tag = True
        for f in range(int(input[0])):
            if not key[f] in d[f]:
                tag = False
                break
        if tag == True:
            res += 1
#    print res
    print 'Case #'+str(i+1)+': '+str(res)
