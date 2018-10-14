from itertools import groupby
import sys


def flip(pan) :
    ans = ''
    for c in pan :
        ans += '+' if (c=='-') else '-'
    return ans

def min_moves(word, k) :
    l = len(word)
    ans = 0
    #print "words :  " + word + "len : " + str(k)
    for i in range(l) :
        if(word[i] == '-') :
            if( (i + k) > l) :
                return -1
            word = word[0:i] + flip(word[i:i+k]) + word[i+k:]
            ans = ans + 1

    return ans


w = int(sys.stdin.readline().strip())
i = 1
for line in sys.stdin:
    inp = line.strip().split()[0]
    k = int(line.strip().split()[1])
    op = min_moves(inp,k)
    if op < 0 :
        print "Case #"+str(i)+": " + "IMPOSSIBLE"
    else :
        print "Case #"+str(i)+": " + str(op)
    i+=1

