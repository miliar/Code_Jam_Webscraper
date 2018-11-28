import sys

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

data = sys.stdin.readlines()

T = int(data[0].strip())

for i in range(1,T+1):
    s = data[i].strip()
    N = int(s.split(' ')[0])
    K = '0000000000000000000000000000000000000' + bin(int(s.split(' ')[1]))
    print "Case #%d: %s" % (i, "OFF" if K[-N:].find('0') != -1 else 'ON')