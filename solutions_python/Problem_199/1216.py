num = int(raw_input())
output = [0]*num
for k in range(num):
        pancake, size = raw_input().strip().split(" ")
        size = int(size)
        signs = pancake.replace("+", "1")
        signs = signs.replace("-", "0")
        signs = [int(x) for x in signs]
        for i in range(len(signs)-size+1):
            if signs[i]==0:
                signs[i:i+size] = [1-x for x in signs[i:i+size]]
                output[k] += 1
        if sum(signs[-size:])!=size:
            output[k] = -1
for i, k in enumerate(output):
    if k>=0:
        print ("Case #%d: %d"%(i+1,k))
    else:
        print ("Case #%d: IMPOSSIBLE"%(i+1))
