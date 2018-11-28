def add(data, width, num):
    if width not in data:
        data[width] = 0
    data[width] += num

def assign(data, K):
    # data is a dict from `width` to `number`
    width = max(data.keys())
    num = data[width]
    k = min(K, num)
    if (width % 2) == 0:
        ma = width // 2
        mi = ma - 1
    else:
        ma = (width-1) // 2
        mi = ma
    
    # Remove used
    data[width] -= k
    if data[width] == 0:
        del data[width]
    
    # Add new
    if ma > 0:
        add(data, ma, k)
    if mi > 0:
        add(data, mi, k)

    return ma, mi, K-k

def answer(line):
    N, K = [int(x) for x in line.split()]
    data = {N:1}
    while K > 0:
        ma, mi, K = assign(data, K)
    return str(ma) + " " + str(mi)

assert( answer("4 2") == "1 0" )
assert( answer("5 2") == "1 0" )
assert( answer("6 2") == "1 1" )
assert( answer("1000 1000") == "0 0" )
assert( answer("1000 1") == "500 499" )

import sys
with open(sys.argv[1]) as input:
    number = int(next(input))
    data = [line.strip() for line in input]

if len(data) != number:
    raise Exception("Read {} but expected {}".format(len(data), number))

with open(sys.argv[2], "w") as output:
    for i, N in enumerate(data):
        print("Case #{}: {}".format(i+1, answer(N)), file=output)
