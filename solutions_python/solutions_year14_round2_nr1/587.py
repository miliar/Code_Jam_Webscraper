#!/usr/bin/python3


def convert(string):
    result = []

    char = ""
    counter = 0
    for c in string:
        if c == char:
            counter += 1
            continue
        else:
            if counter == 0:
                char = c
                counter = 1
                continue
            result.append((char, counter))
            char = c
            counter = 1
    result.append((char, counter))
    return result

def check(strings):
    lengths = list(map(len, strings))
    ll = lengths[0]
    for l in lengths[1:]:
        if ll != l:
            return False

    chars = []
    for i,string in enumerate(strings):
        for j,t in enumerate(string):
            if i == 0:
                chars.append(t[0])
            else:
                if chars[j] != t[0]:
                    return False
    return True

def getAvgs(strings):
    avgs = []
    for i,string in enumerate(strings):
        for j,t in enumerate(string):
            if i == 0:
                avgs.append(t[1])
            else:
                avgs[j] = (avgs[j]*i + t[1]) / (i+1)
    avgs = list(map(lambda x: int(x+0.5), avgs))
    return avgs

def getDeviations(avgs, strings):
    dev = 0
    for string in strings:
        dev += sum(map(lambda avg, x: abs(avg-x[1]), avgs, string))
    return dev


T = int(input())

for t in range(T):
    N = int(input())
    
    strings = []
    for n in range(N):
        strings.append(input())
        
    ss = list(map(convert, strings))
    
    #print(ss)

    
    if not check(ss):
        print("Case #%d: Fegla Won" % (t+1))
    else:
        avgs = getAvgs(ss)
        
        dev = getDeviations(avgs, ss)
        
        print("Case #%d: %d" % ((t+1), dev))

    
    #print("%s %d" % (avgs, dev))


