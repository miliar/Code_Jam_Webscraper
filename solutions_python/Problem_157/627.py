import sys
import numpy as np
from pprint import pprint

numTests = int(sys.stdin.readline().rstrip("\n"))

I = 2
J = 3
K = 4

lookup = [
    [1,I,J,K],
    [I,-1,K,-J],
    [J,-K,-1,I],
    [K,J,-I,-1],
]

def to_quat_format(x):
    sign = -1 if x< 0 else 1
    x = x if x > 0 else -x

    if( sign < 0):
        if( x == 1):
            return "-1"
        elif( x == 2):
            return "-i"
        elif( x == 3):
            return "-j"
        elif (x == 4):
            return "-k"
    else:
        if( x == 1):
            return "1"
        elif( x == 2):
            return "i"
        elif( x == 3):
            return "j"
        elif (x == 4):
            return "k"

def mult_quat(x,y):
    sign = x*y
    if( sign < 0):
        sign = -1
    else:
        sign = 1
    if( x < 0): x = -x;
    if( y < 0): y = -y;

    return sign*lookup[x-1][y-1]

def reduce_quat(x):
    c = x[0]
    for i in xrange(1,len(x)):
        c = mult_quat(c,x[i])
    return c

def go_forward_backward(seq,total_len):
    forward = []

    c = None
    size = len(seq)
    for i in xrange(0,total_len):
        if( c == None):
            c = seq[i%size]
        else:
            c = mult_quat(c,seq[i%size])
        forward.append(c)

    backward  = []
    c = None
    for index in xrange(0,total_len):
        i = total_len - index - 1
        if(c == None):
            c = seq[i%size]
        else:
            c = mult_quat(seq[i%size],c)
        backward.append(c)
    backward.reverse()

    # print(forward)
    # print(backward)
    return forward,backward

def solve(seq,forward, backward,total_len):
    # loop through the forward sums
    for i in xrange(total_len):
        if forward[i] != I:
            continue

        # loop through the backward sums
        for k in xrange(total_len):
            back_k = total_len - k - 1

            if back_k < i:
                # we went pass the beginning point, no use..
                break

            if backward[back_k] == K:
                next_i = i + 1
                next_k = back_k - 1

                if(back_k - i -1 < 0):
                    continue
                else:
                    if( mult_quat(-forward[i],forward[next_k]) == J):
                        return True

    return False

def brute_solve(seq):
    c1 = None
    for i in xrange(len(seq)):
        if(c1 == None):
            c1 = seq[i]
        else:
            c1 = mult_quat(c1,seq[i])

        if(c1 == I):
            c2 = None
            for j in xrange(i+1,len(seq)):
                if(c2 == None):
                    c2 = seq[j]
                else:
                    c2 = mult_quat(c2,seq[j])

                if(c2 == J):

                    c3 = None
                    for k in xrange(j+1,len(seq)):
                        if(c3 == None):
                            c3 = seq[k]
                        else:
                            c3 = mult_quat(c3,seq[k])

                    if(c3 == K):
                        return True

    return False


# seqs = [
#     [I,J,K],
#     [K,J,I],
#     [J,K,J,K],
#     [I,J,J,J,J,J,K],
#     [I,K,I,K],
#     [I,I,J,I,K],
#     [I,J,K,J,I,K],
#     [I,K,I,K,J,I,K],
#     [I,I,J,I,K,J,I,K],
#     [I,I,J,I,I,J,J,I,K],
#     [I,I,J,I,I,J,J,J,K,K],
#     [I,I,J,I,I,J,J,K,I,K,K],
#     [I,I,J,I,I,K,I,K,I,K,I,K,K],
#     [I,I,J,I,I,K,I,K,K,K,K,I,I,J,J,K,I,K,K],
#     [I,I,K,K,I,I,K,K,I,I,K,K],
#     [I,I,K,K],
# ]
# numTests = len(seqs)

for i in xrange(numTests):
    L,X = sys.stdin.readline().rstrip("\n").split(" ")
    L = int(L)
    X = int(X)
    seq = sys.stdin.readline().rstrip("\n")
    seq = map(lambda x: ord(x)- ord('i') + 2,seq)
    total_len = len(seq)*X

    # seq = seqs[i]
    # total_len = len(seq)

    forward,backward = go_forward_backward(seq,total_len)
    if(solve(seq,forward,backward,total_len)):
        print("Case #"+ str(i + 1) + ": YES")
    else:
        print("Case #"+ str(i + 1) + ": NO")

    # if(brute_solve(seq)):
    # # if(brute_solve(seq*X)):
    #     print("Case #"+ str(i + 1) + ": YES")
    # else:
    #     print("Case #"+ str(i + 1) + ": NO")