#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    in_file = open("A-small-attempt0.in", mode='r')
    out_file = open("A-small-attempt0.out", mode='w')

    lines = in_file.readlines()      
    T = int(lines[0])
    
    for i in xrange(T):
        line = lines[2 * i + 1]
        A, N = [int(s) for s in line.strip().split(' ')]
        
        line = lines[2*i + 2]
        M = [int(s) for s in line.strip().split(' ')]
        
        if A == 1 or N == 0:
            out_file.write("Case #" + str(i+1) + ": " + str(N) + "\n") 
            print "Case #" + str(i+1) + ": " + str(N) + "\n"
            continue;
                
        M.sort()
        
        actions = [0] * N
        mote = A
        
        print A, M
        print
        
        for j in xrange(N):
            if j>0: actions[j] = actions[j-1]
            while mote <= M[j]:
                mote = 2 * mote - 1
                actions[j] += 1
            mote += M[j]
            print mote, actions
        
        if actions[0] >= N:
            out_file.write("Case #" + str(i+1) + ": " + str(N) + "\n") 
            print "Case #" + str(i+1) + ": " + str(N) + "\n"
            continue;
                
        for j in xrange(N):
            actions[j] += N-(j+1) 

        ans = min(actions)
        
        out_file.write("Case #" + str(i+1) + ": " + str(ans) + "\n") 
        print "Case #" + str(i+1) + ": " + str(ans) + "\n"
        
        
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
