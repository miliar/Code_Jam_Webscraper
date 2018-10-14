import sys
sys.setrecursionlimit(10000000)
def flipBits(bits, k):
    bits = list(bits)
    for x in range(k):
        if bits[x] == '+':
            bits[x] = '-'
        else:
            bits[x] = '+';
    return ''.join(bits);

def getFlips(bits, k, n):
    bits = bits.lstrip('+')
    if (len(bits) == 0):
        return n;
    
    if (len(bits) < k):
        return "IMPOSSIBLE";

    bits = flipBits(bits, k)
    bits = bits.lstrip('+');
    return getFlips(bits, k, n+1)


n = int(raw_input())
for i in range(n):
    string = str(raw_input()).split()
    bits = str(string[0])
    k = int(string[1])
    print "Case #{}: {}".format(i+1, getFlips(bits, k, 0))
