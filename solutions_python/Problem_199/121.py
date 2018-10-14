def flip(pancake, K, index):
    for i in range(index, index+K):
        if pancake[i] == "+":
            pancake[i] = "-"
        else:
            pancake[i] = "+"

def answer(N):
    pancake, K = N.split()
    K = int(K)
    pancake = list(pancake)
    count = 0
    for i in range(len(pancake)-K+1):
        if pancake[i] == "-":
            flip(pancake, K, i)
            count += 1
    if all(s=="+" for s in pancake):
        return count
    return "IMPOSSIBLE"

assert( answer("---+-++- 3") == 3 )
assert( answer("+++++ 4") == 0 )
assert( answer("-+-+- 4") == "IMPOSSIBLE" )

import sys
with open(sys.argv[1]) as input:
    number = int(next(input))
    data = [line.strip() for line in input]

if len(data) != number:
    raise Exception("Read {} but expected {}".format(len(data), number))

with open(sys.argv[2], "w") as output:
    for i, N in enumerate(data):
        print("Case #{}: {}".format(i+1, answer(N)), file=output)
