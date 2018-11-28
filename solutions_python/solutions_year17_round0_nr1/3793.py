





def countflips(Word,k):
    S=list(Word)
    flips=0
    lengthS=len(S)
    teststop=lengthS-k
    for i in range(lengthS):
        if checkdone(S):
            return flips
        elif S[i]=="-" and i>teststop:
            return "IMPOSSIBLE"
        elif S[i]=="-":
            flips+=1
            for j in range(k):
                switch=S[i+j]
                if switch=="-":
                    S[i+j]="+"
                else:
                    S[i+j]="-"
    


def checkdone(S):
    for i in S:
        if i=="-":
            return False
    return True

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    inputpair=input().split(" ")
    Word=inputpair[0]
    k=int(inputpair[1])
    print("Case #{}: {}".format(i, countflips(Word,k)))
  # check out .format's specification for more formatting options
