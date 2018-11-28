#!/usr/bin/python -tt
import sys

def Key(Tuple): 
  return Tuple[1]

def main():
  T = int(raw_input())
  
  for t in range(1, T+1):
    N = int(raw_input())
    wires = []
    for i in range(N): 
      wires.append(tuple(map(int, raw_input().split())))
    wires.sort()
    answer = 0
    #print "wires", wires
    for i, wire in enumerate(wires): 
      below = sorted(wires[i+1:], key=Key)
      for wire2 in below: 
        if wire2[1] < wire[1]: 
          answer += 1
        else: break
      #print i, wire
      #print below
    
    print ('Case #'+str(t)+': ' + str(answer))

if __name__ == '__main__':
  main()
