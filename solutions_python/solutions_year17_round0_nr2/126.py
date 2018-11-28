def first_problem(N):
    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            return i
    return -1

def okay(N):
    return first_problem(N) == -1

def answer(N):
    N = list(N)
    while not okay(N):
        index = first_problem(N)
        N[index] = int(N[index]) - 1
        for i in range(index+1, len(N)):
            N[i] = "9"
        if N[index] == 0 and index == 0:
            del N[0]
        else:
            N[index] = str( N[index] )
    return "".join(N)

assert( answer("132") == "129" )
assert( answer("1000") == "999" )
assert( answer("7") == "7" )
assert( answer("111111111111111110") == "99999999999999999" )

import sys
with open(sys.argv[1]) as input:
    number = int(next(input))
    data = [line.strip() for line in input]

if len(data) != number:
    raise Exception("Read {} but expected {}".format(len(data), number))

with open(sys.argv[2], "w") as output:
    for i, N in enumerate(data):
        print("Case #{}: {}".format(i+1, answer(N)), file=output)
