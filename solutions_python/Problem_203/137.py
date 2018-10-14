# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:01:22 2017

@author: cling
"""

def solve(R,C,S,fo):
    special = '?'*C
    sp = []
    flag = -1
    for i in range(R):
        s = S[i]
        if s==special:
            sp.append(0) 
        else:   
            sp.append(1)
            if flag==-1:
                flag = i
            c = [x for x in s if x!='?'][0]
            new_s = ''
            for j in range(C):
                if s[j]!='?':
                    c = s[j]
                new_s += c
            S[i] = new_s

    for i in range(R):
        if S[i]==special:
            S[i] = S[flag]
        else:
            flag = i
    
    for i in range(R):
        fo.write(S[i]+'\n')
    
def main():
    fo = open('output.txt','w')
    with open('input.txt','r') as f:
        line = f.readline()
        T = int(line[:-1])
        for t in range(T):
            line = f.readline()
            st = line[:-1].split(' ')
            R,C = int(st[0]),int(st[1])
            S = []
            for i in range(R):
                S.append(f.readline()[:-1])
            fo.write('Case #%d:\n' % (t+1))
            solve(R,C,S,fo)
    fo.close()
if __name__ == '__main__':
    main()