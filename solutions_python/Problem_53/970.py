#!/usr/bin/env python2.6

# -*- coding : utf-8 -*-


class Snapper():
        def __init__(self):
                self.state = False
                self.power = False
        
        def toggle(self):
                self.state = not self.state
                

def is_light(N, K):
        for j in range(K):                
                for i in range(N):
                        if i<N-1:
                                snappers[i+1].power = snappers[i].power and snappers[i].state
                        
                        if snappers[i].power:
                                snappers[i].toggle()
                        else:
                                break
                
                for i in range(N-1):
                        snappers[i+1].power = snappers[i].power and snappers[i].state


        return (snappers[N-1].power and snappers[N-1].state)
        
max_N = 10
max_K = 100
T = 0
snappers = [Snapper() for x in range(max_N)]
snappers[0].power = True
        
def clean_snappers():
        for i in range(N):
                snappers[i].power = snappers[i].state = False
        snappers[0].power = True
                                        
lines = 0
with open("A-small-attempt6.in", "r") as fin:
        with open("A-small.out", "w") as fout:
                for line in fin:
                        lines+=1
                        if lines == 1:
                                T = int(line.strip())
                                continue
                        if lines < T+2:
                                per = '' if lines-1==T else '\n'
                                numbers = line.strip().split()
                                if len(numbers) == 2:
                                        N = int(numbers[0].strip())
                                        K = int(numbers[1].strip())
                                        if N>0 and K>-1 and N<=max_N and K<=max_K:
                                                answer = 'ON' if is_light(N, K) else 'OFF'
                                                clean_snappers()
                                                fout.write('Case #%d: %s%s' % (lines-1, answer, per))
                                        else:
                                                fout.write('Case #%d: OFF%s' % (lines-1, per))                                                 
                                else:
                                        fout.write('Case #%d: OFF%s' % (lines-1, per))               

