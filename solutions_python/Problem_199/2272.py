
from string import maketrans   # Required to call maketrans function.
import sys

intab='+-'
outtab='-+'
trantab = maketrans(intab, outtab)

def flip_pancake(s):
    return s.translate(trantab)

def num_flip(S,k):
    num_pancake=len(S)
    flips = 0
    for i in xrange(num_pancake):

        if (num_pancake-i)<k:
            if S[i]=='-':
                return 'IMPOSSIBLE'
            else:
                continue

        if S[i]=='-':
            S = S[:i]+flip_pancake(S[i:i+k])+S[i+k:]
            flips=flips+1
        elif S[i]=='+':
            continue
    return flips

with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fout:
    T=int(fin.readline())
    for i in xrange(T):
        S,K=fin.readline().split()
        print K,S
        K=int(K)
        S=str(S)
        fout.write('Case #'+str(i+1)+': '+str(num_flip(S,K))+'\n')


#T = int(raw_input('input_small_file.in'))
#print T
#for i in xrange(T):
#    K,S=int(raw_input('input_small_file.in').split())
#    S=int(S)
#    num_flip(S,K)
