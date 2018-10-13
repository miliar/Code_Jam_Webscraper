#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkpattern(N, M, lawn):
    transpose = zip(*lawn)
    
    for y in xrange(N):
        for x in xrange(M):
            if (lawn[y][x] < max(lawn[y])) and lawn[y][x] < max(transpose[x]):
                return False
        
    return True

def main():
    in_file = open("B-large.in", mode='r')
    out_file = open("B-large.out", mode='w')

    lines = in_file.readlines()      
    T = int(lines[0])
    
    offset = 1
    
    for i in xrange(T):
        line = lines[offset]
        offset += 1
        
        N, M = line.strip().split(' ')
        N = int(N)
        M = int(M)
        
        lawn = []
        
        for y in xrange(N):
            row = []
            line = lines[offset+y]
            for x in line.strip().split(' '):
                row.append(int(x))
            lawn.append(row)
        
        offset += N
        
        if checkpattern(N, M, lawn):
            out_file.write("Case #" + str(i+1) +": YES\n")
        else:
            out_file.write("Case #" + str(i+1) +": NO\n")

        
    in_file.close()
    out_file.close()

if __name__ == '__main__':
    main()