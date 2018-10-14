import sys

if len(sys.argv)!=2:
  print 'Usage: snapper.py <inputfile>'
  exit(1)
  
inputfile=open(sys.argv[1],'r')
outputfile=open('snapper_results.txt','w')

numoflines=int(inputfile.readline())
for i in range(numoflines):
  N,K=inputfile.readline().split(' ')
  N=int(N)
  K=int(K.strip())
  expn=2**N
  result='ON' if K%expn==expn-1 else 'OFF'
  outputfile.write("Case #%d: %s\n"% (i+1,result))