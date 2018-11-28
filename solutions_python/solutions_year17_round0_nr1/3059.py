#!/usr/bin/env python

def readFile(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    testCases = int(content[0])+1

    print 'Input\t\tOutput\n'
    for i in range(1, testCases):
        (pancakes, K) = content[i].split(" ")
        print pancakes + " " + K
        print "Case #%d: %s " % (i, countFlips(pancakes, K)) + "\n"

def read_inputs():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        print "Case #{}: {}".format(i, countFlips(n, m))

        # check out .format's specification for more formatting options

def is_all_happy_face(S):
    for c in S:
        if(c != '+'):
            return False
    return True

def flip(S, n, m):
    #print "n = %d, m = %d" % (n, m)
    if (m <= len(S)):
        for i in xrange(n, m):
            if S[i] == '+':
                S = S[:i] + '-' + S[i+1:]
            else:
                S = S[:i] + '+' + S[i+1:]
            #print S
    return S


def countFlips(S, K):

    k_num = (int(K))

    if is_all_happy_face(S): return 0

    nb_swaps = 0

    while '-' in S:
        start = S.find('-')
        end = start + (k_num)
        #print "start = %d, end %d" % (start,end)
        if start >= 0 and len(S) >= end:
            S = flip(S, start, end)
            nb_swaps += 1
        elif len(S) < end:
            break
        else:
            if is_all_happy_face(S):
                break;
            else:
                return 'IMPOSSIBLE'

    if '-' in S:
        return 'IMPOSSIBLE'

    return nb_swaps

def main():
    #readFile('inputs')
    read_inputs()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupting..'