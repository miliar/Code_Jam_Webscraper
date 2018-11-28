#!/usr/bin/python

casenumber = int(raw_input())
def findFirstMinus(s,i):
    index = i
    for i in range(index, len(s)):
        if s[i] == '-':
            return i
        i += 1
    return -1

def flip(str, pos, length):
    for i in range(pos,pos+length):
        if str[i] == '-':
            str = str[:i] + '+' + str[i+1:]
        else:
            str = str[:i] + '-' + str[i+1:]
    return str

def mirror(str):
    l = len(str)
    res = ""
    index = l-1
    while index >=0:
        res+=str[index]
        index -= 1
    return res

for case in range(0, casenumber):
    s,k = raw_input().split(" ")
    size = len(s)
    flipSize = int(k)
    possibleFlip = size - int(k) + 1
    target = s.replace('-','+')
    stateMap = {}
    stateBacklog = []
    curr = s

    find = False
    if s == target:
        print "Case #{}: {}".format(case+1,0)
    else:
        stateMap[s] = 0
        stateBacklog.append(s)
        index = 0
        steps = 0
        while True:
            fristMinus = findFirstMinus(curr,index)
            if fristMinus >= 0:
                if fristMinus+flipSize<=size:
                    curr = flip(curr,fristMinus,flipSize)
                    index += 1
                    steps += 1
                else:
                    break
            else:
                find = True
                print "Case #{}: {}".format(case+1,steps)
                break;
        if not find:
            print "Case #{}: {}".format(case+1,'IMPOSSIBLE')
