
def istidy(n):
    n = str(n)
    n = [int(s) for s in n]
    #print(n)
    if sorted(n) == n:
        return True
    else:
        return False

def tinytidy(n):
    listn = [int(s) for s in str(n)]
    if len(listn)==1:
        num = int(''.join(map(str,listn)))
        return(num)
    else:
        for i in range(1,len(listn)): #skip first digit
            current = listn[i]
            previous = listn[i-1]
            if current < previous:
                if previous==1:
                    listn[0]=0
                    for j in range(1,len(listn)):
                        listn[j]=9
                    num = int(''.join(map(str,listn)))
                    return(num)

                else: # previous is anything else
                    listn[i-1]=listn[i-1]-1
                    for j in range(i,len(listn)):
                        listn[j]=9
                    num = int(''.join(map(str,listn)))
                    return(num)

t = int(input())  # read a line with a single integer

for line in range(1, t + 1):
    mynumber = int(input())
    n=mynumber
    while not istidy(n):
        n=tinytidy(n)
    print("Case #{}: {}".format(line, n))
