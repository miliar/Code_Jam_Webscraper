import sys, string

memo = {}


def main():
    filePrefix = 'C-large'
    fin = open(filePrefix + '.in', 'r')
    fout = open(filePrefix + '.out', 'w')
    #fout = sys.stdout
    N = int(fin.readline().strip())
    w = "welcome to code jam"
    junk_letters = ''.join([c for c in 'abcdefghijklmnopqrstuvwxyz'
                            if c not in w])
    nulltable = string.maketrans('', '')
    for i in xrange(N):
        W = fin.readline().strip()
        W = W.translate(nulltable, junk_letters)
        answer = C(W, w)
        fout.write("Case #%d: %0.4d\n" % ((i+1), answer))
        #break
    fin.close()
    fout.close()


# Straight-up recursive.
# def C(W, w, d = 0):
#     #indent = ' ' * d
#     #print "%sC(%s, %s)" % (indent, W, w)

#     if W == w:
#         ret = 1

#     else:
#         first, last = W.find(w[0]), W.rfind(w[-1])
    
#         if first == -1 or last == -1 or len(W) < len(w):
#             ret = 0

#         elif (first != 0) or (last != len(W) - 1):
#             ret = C(W[first:(last+1)], w, d+1)

#         else:
#             ret = (C(W[1:], w[1:], d+1) + C(W[1:], w, d+1)) % 10000

#     #print "%sReturns %d" % (indent, ret)
#     return ret


# Memoized.
def C(W, w, d = 0):
    global memo
    #indent = ' ' * d
    #print "%sC(%s, %s)" % (indent, W, w)

    memoKey = (W, w)
    if memoKey in memo:
        return memo[memoKey]

    if W == w:
        ret = 1

    elif len(w) == 0:
        ret = 1

    else:
        first, last = W.find(w[0]), W.rfind(w[-1])
    
        if first == -1 or last == -1 or len(W) < len(w):
            ret = 0

        elif (first != 0) or (last != len(W) - 1):
            ret = C(W[first:(last+1)], w, d+1)

        else:
            ret = (C(W[1:], w[1:], d+1) + C(W[1:], w, d+1)) % 10000

    memo[memoKey] = ret
    #print "%sReturns %d" % (indent, ret)
    return ret
