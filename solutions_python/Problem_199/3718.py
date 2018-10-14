import fileinput
import sys

def flip(ip, i, n):
    for j in xrange(i,i+n):
        if ip[j] == '-':
            ip[j] = '+'
        else:
            ip[j] = '-'
def invert(ip,n):
    size = len(ip)
    flips = 0
    for i in xrange(size-n+1):
        if ip[i] == '-':
            flip(ip, i, n)
            flips += 1
    if '-' in ip[-n:]:
        return "IMPOSSIBLE"
    else:
        return flips

first = 0
count = 1
f = open('/home/deepak/Downloads/output.txt','w');
sys.stdout = f
for line in fileinput.input('/home/deepak/Downloads/A-large.in'):
    if first == 0:
        num = int(line)
        first = 1
        continue
#print line
#line = "-+-+- 4"
    ip1, ip2 = line.split(" ")
    ipl = list(ip1)
    print "Case #"+ str(count) + ": " + str(invert(ipl, int(ip2)))
    count += 1


