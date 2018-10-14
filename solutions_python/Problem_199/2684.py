# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.

T = int(raw_input())  # number of cases
for i in xrange(1, T + 1):
        S, K = raw_input().split()
        S=list(S) # S is the sequence of pancakes
        K=int(K) # K is the size of the pancake flipper
        pos=0 # position in the sequence of pancakes
        flips=0
        problem=False # variable that will turn True if its impossible
        while pos+K <= len(S) : # We go along the sequence in blocks of length K
            if S[pos]=='+' :
                pos+=1
            else :
                flips+=1
                for j in range (K) :
                    if S[pos+j]=='-' :
                        S[pos+j]='+'
                    else :
                        S[pos+j]='-'
        while pos < len(S) :
            if S[pos]=='-':
                problem=True
            pos+=1
        if problem :
            print "Case #"+str(i)+": IMPOSSIBLE"
        else :
            print "Case #"+str(i)+": "+str(flips)
