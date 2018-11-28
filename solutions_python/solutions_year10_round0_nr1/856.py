#from numpy import *
import re

#N : number of snapper devices plugged together
#1 <= N <= 10

#K : number of times fingers are snapped
#0 <= K <= 100

#the Nth snapper will be off 2^(N-1) times and then on 2^(N-1) times
#the light will be on when all snappers are on, which is after every
# 2^(N)-1 snaps (to count 0)
#ex : N = 4, will be on after every 16 snaps (15)
def snapper (N,K):
  K = K % (2**N)
  if (K == (2**N - 1)):
    return "ON"
  else:
    return "OFF"

filename = 'A-large'
input = open(filename+'.in','r')
output = open(filename+'.out','w')
#input = open('sample.in','r')
#output = open('sample.out','w')

#first line is garbage
input.readline()
lines = input.readlines()

for i in range(len(lines)):
  [N,K] = re.findall(r'[0-9]+', lines[i])
  N = int(N)
  K = int(K)
  output.write("Case #%d: %s\n" % (i+1,snapper(N,K)))

