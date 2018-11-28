__author__ = 'Daria'
import time
start = time.time()
#reading
input = open ('/Users/Daria/PycharmProjects/CodeJam/input.txt','r')
N = int(input.readline())
#print N
l = input.readlines()
input.close()
lines = []

def is_pair(a,b):
    n = len(a)
    for i in range(1,n):
        if int(a) == int(b[len(b)-i:] + b[:len(b)-i]):
          #  print a,b
            return True
    return False

def count_pairs(c,d):
    pairs = []
    s = int(c)
    t = int(d)
    for a in range(s,t+1):
        for b in range(a+1,t+1):
            if is_pair(str(a),str(b)) and [a,b] not in pairs:
                pairs.append([a,b])
    return len(pairs)

#output
output = open ('/Users/Daria/PycharmProjects/CodeJam/output.txt','w')
k = 0
for line in l:
    k += 1
    t = line.strip().split()
    c = count_pairs(t[0],t[1])
    output.write('Case #%i: %i'%(k,c))
    #print ('Case #%i: %i'%(k,c))
    output.write("\n")
output.close()

print time.time()-start