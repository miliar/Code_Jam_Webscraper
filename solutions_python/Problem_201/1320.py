#!/usr/bin/env pypy

import sys,os,math

num_cases = int(sys.stdin.readline().strip())

def seat_values(N,K):
  power = int(math.floor(math.log(K,2))) + 1
  min_value = (N-K)/(2**power)
  max_value = (N-K+2**power/2)/(2**power)
  return (max_value, min_value)

for case in xrange(0,num_cases):
  stalls, people = sys.stdin.readline().strip().split()
  stalls = int(stalls)
  people = int(people)
  sys.stdout.write("Case #{}: {} {}\n".format(case+1, *seat_values(stalls, people)))

#person = int(sys.argv[1])
#for i in range(1,21):
#  sys.stdout.write("p{}: min:{} max:{}\n".format(person, *seat_values(i, person)))
