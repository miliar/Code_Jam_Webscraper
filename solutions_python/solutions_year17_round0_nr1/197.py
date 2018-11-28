import sys

f = sys.stdin

cases = int(f.readline().strip())

for ii in range(cases):
    line = f.readline().strip()
    rawsequence = line.split(" ")[0]
    n = int(line.split(" ")[1])
    arr = []
    for c in rawsequence:
        if c == '-':
            arr.append(False)
        else:
            arr.append(True)

    count = 0
    size = len(arr)
    while(1==1):
        i = 0
        foundCake = False
        while(i < size):
            if(not arr[i]):
                foundCake = True
                break;
            i += 1

        # We're all flipped!
        if(not foundCake):
            break;

        # If true, we can't fit spatula, and we're not finished. Failure
        if(i > size-n):
            count= -1
            break;

        # Flip the cakes
        for j in range(i,i+n):
            arr[j] = not arr[j]

        count += 1

    if (count == -1):
        ans = "IMPOSSIBLE"
    else:
        ans = str(count)

    print ("Case #{0}: {1}".format(ii+1, ans))


        
