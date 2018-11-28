#!/usr/bin/python
import sys

def read_stuff():
        return [x for x in raw_input().strip().split()]

def main():
        T=int(read_stuff().pop(0))
        for t in xrange(1,T+1):
                #print t
                inp=read_stuff()
                N=int(inp.pop(0))
                otime=0
                btime=0
                od=1
                bd=1
                n=1
                while n<=N:
                        Ri=inp.pop(0)
                        Pi=int(inp.pop(0))
                        if Ri=='O':
                                otime=max(otime+abs(int(Pi)-od)+1,btime+1)
                                od = int(Pi)
                        elif Ri=='B':
                                btime=max(btime+abs(int(Pi)-bd)+1,otime+1)
                                bd = int(Pi)
                        n+=1
                print "Case #%d: %d" % (t,max(otime,btime))


if __name__=='__main__':
        main()

