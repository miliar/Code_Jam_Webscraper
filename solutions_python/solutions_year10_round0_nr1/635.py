
def printResult(n,k,case):
    snapsneeded = (2**n) - 1
    if k < snapsneeded:
       result = "OFF"
    if k == snapsneeded:
        result = "ON"
    if k > snapsneeded:
        k -= snapsneeded
        snapsneeded += 1
        if k < snapsneeded:
            result = "OFF"
        elif k % snapsneeded == 0:
            result = "ON"
        else:
            result = "OFF"

    print("Case #%d: %s" % (case, result))



#Read in info sys in
for i in range(int(raw_input())):
    n = map(lambda x: int(x), raw_input().split())
    printResult(n[0],n[1],i+1)
