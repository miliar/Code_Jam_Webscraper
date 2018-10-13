#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    fin = open("A-small-0.in", "r")
    fout = open("A-small-0.out", "w")
    T = int(fin.readline())

    for t in xrange(0, T):
        N = int(fin.readline().strip())
        s = [[]]*N
        count = []
        for i in range(0, N):
            s[i] = list(fin.readline().strip())
            print s[i]
        i = 0
        j = 0
        answer = 0
        while i<len(s[0]) and j<len(s[1]):
            if s[0][i] != s[1][j]:
                answer = "Fegla Won"
                break
            else:
                c1 = 1
                c2 = 1
                while i+1 < len(s[0]) and s[0][i+1] == s[0][i]:
                    i += 1
                    c1 += 1
                i += 1
                while j+1 < len(s[1]) and s[1][j+1] == s[1][j]:
                    j += 1
                    c2 += 1
                j += 1
                
                answer += abs(c1-c2)
        if i<len(s[0]) or j<len(s[1]):
            answer = "Fegla Won"

        print answer

        fout.write("Case #%i: %s\n" % (t+1, answer))
    
    fin.close()
    fout.close()

