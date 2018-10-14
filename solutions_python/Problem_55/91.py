#!/usr/bin/env python
#By Jai Dhyani
#Automatically generated on 2010-05-07

import sys

def main():
    #this could be made faster by caching based on the front of the line
    in_file = "C-large.in"
    if len(sys.argv)==1:
        f = open( in_file )
        outfile = open( in_file+'.out', 'w' )
    else:
        f = open(sys.argv[1])
        outfile = open( sys.argv[1]+'.out', 'w' )
    T = int(f.readline())
    for t in xrange(T):
        num_runs, capacity, num_groups = readnums( f )
        group_size = readnums( f )
        profit = 0
        front = 0
        cache = dict()
        runs_left = num_runs
        profit=0
        while runs_left>0:
            print '%d runs left'%runs_left
            if front in cache:
                loop_p = profit-cache[front][0]
                loop_l =cache[front][1] - runs_left
                loops_left = runs_left/loop_l
                profit += (loop_p*loops_left)
                runs_left %= loop_l
                cache=dict()
            else:
                front_orig = front
                seats_left = capacity
                while seats_left >= group_size[front]:
                    seats_left-= group_size[front]
                    front = (front+1)%len(group_size)
                    if front==front_orig:
                        break
                cache[front_orig]=(profit, runs_left)
                profit += (capacity - seats_left)
                runs_left-=1
        answer='Case #%d: %d\n' % (t+1, profit)
        print answer
        outfile.write( answer )

def readnums(f):
    return [ int(num) for num in f.readline().split() ]

if __name__ =='__main__':
    main()

