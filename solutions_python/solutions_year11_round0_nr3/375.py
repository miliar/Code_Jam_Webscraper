import sys,os,functools,math
def Split(a):
    if(functools.reduce(lambda x,y:x^y,a) != 0):
        return 'NO'
    return sum(a)-min(a)

inputFile = open('c-small.in','r')
sys.stdin = inputFile
output = open('c-small.out','w')
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()]
    print('Case #' + str(i+1) + ': ' + str(Split(a)), file = output)

output.close()
inputFile.close()
