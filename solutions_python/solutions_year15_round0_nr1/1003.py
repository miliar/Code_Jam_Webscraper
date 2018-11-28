import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())

    for i in range(t):
        shy, pArray = input().split()
        shy = int(shy);     pArray = list(pArray)
        j=0
        prevCount = 0
        count = 0
        people = 0
        while(j<len(pArray)):
            if(j>people and int(pArray[j])!=0):
                count = j - people
                count = max(prevCount, count)
            people += int(pArray[j])
            prevCount = count
            j += 1

        print("Case #%d: %d"%(i+1, count))
