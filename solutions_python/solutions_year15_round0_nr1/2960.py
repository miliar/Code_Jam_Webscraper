#!/usr/bin/env python3

def load(filename):
    f = open(filename, 'r')
    testcases = int(f.readline())
    t = []
    for i in range(testcases):
        # load the testcase
        s = f.readline()
        ss = s.split()
        smax = int(ss[0])
        slist = list(ss[1])
        for j in range(len(slist)):
            slist[j] = int(slist[j])
        sthing = [smax, slist]
        t.append(sthing)
    #print(t)
    return t

def main():
    cases = load("A-small-attempt0.in")
    num = 1
    for case in cases:
        smax = case[0]
        s = case[1]

        clappers = 0
        friends = 0
        for index in range(0, len(s)):
            if clappers >= index:
                clappers += s[index]
            else:
                friends += index - clappers
                clappers += index - clappers
                clappers += s[index]
        print("Case " + str(num) + ": " + str(friends))
        num += 1

main()
