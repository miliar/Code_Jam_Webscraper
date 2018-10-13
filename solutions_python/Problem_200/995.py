def simpleTidy(N):
    digits=[x for x in list(str(N))]
    biggestLast="9"
    current=0
    for i in range(0, len(digits)):
        j=len(digits)-1-i
        largestPossible=min(biggestLast, digits[j])
        biggestLast=largestPossible
        current+=int(largestPossible)*(10**i)
    return current

def getBestTidy(N):
    digits=[x for x in list("0"+str(N))]
    possible=[]
    for i in range(len(digits)):
        newDigits=digits[:]
        if i > 0:
            if(newDigits[i-1]>"0"):
                newDigits[i-1]=str(int(newDigits[i-1])-1)
                for j in range(i, len(digits)):
                    newDigits[j]="9"
        possible.append(simpleTidy(int("".join(newDigits))))
    return max(possible)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N=int(input())
    print("Case #{}: {}".format(i, getBestTidy(N)))
