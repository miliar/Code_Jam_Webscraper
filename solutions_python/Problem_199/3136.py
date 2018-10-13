def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        arrInput = raw_input().split(" ")
        s = arrInput[0]
        k = int(arrInput[1])
        print "Case #{}: {}".format(i, flipPancakes(s, k))

def flipPancakes(s, k):
    ls = list(s)
    flipCount = 0
    for i in xrange(0, len(ls)-k+1, 1):
        if ls[i] is '-':
            for j in xrange(i, k+i, 1):
                if ls[j] is '-': ls[j] = '+'
                else: ls[j] = '-'
            flipCount = flipCount + 1
    if '-' in ls: flipCount = 'IMPOSSIBLE'
    return flipCount

main()