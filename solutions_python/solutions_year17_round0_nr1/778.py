# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:33:43 2017

@author: pierre
"""

import sys



def solve(input_string, K):
     l = list(input_string)
     l_bool = [a=='+' for a in l]

     inc = 0

     for ind in range(len(l)-K+1):
          if (not l_bool[ind]):
               for k in range(K):
                    l_bool[ind+k]=not l_bool[ind+k]
               inc+=1

     if (not all(l_bool)):
          return('IMPOSSIBLE')

     return str(inc)


if __name__ == '__main__':
     in_path = sys.argv[1]
     out_path = sys.argv[2]

     with open(in_path, "r") as f:
          N = int(f.readline())

          out = open(out_path, 'w')

          for i in range(N):
               out.write('Case #'+(str(i+1))+": ")
               new = f.readline().split(" ")

               S = new[0]
               K = int(new[1])

               out.write(solve(S, K))
               out.write('\n')

          out.close()