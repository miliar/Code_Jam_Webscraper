import sys

infile = sys.argv[1]

f = open(infile, "r")

T = (int) (f.readline().strip())

for t in range(1, T+1):
    test = f.readline().strip().split(" ")

    # Combinations
    C = (int) (test[0])
    combines = {}
    for combo in test[1:1+C]:
        combines[combo[0:2]] = combo[2]
        combines[combo[0:2][::-1]] = combo[2]

    # Shift
    test = test[1+C:]

    # Opposed pairs
    D = (int) (test[0])
    opposed = {}
    for pair in test[1:1+D]:
        opposed[pair] = True
        opposed[pair[::-1]] = True

    # Shift
    test = test[1+D:]

    # Input
    N = (int) (test[0])
    data = test[1]

    # Solve
    output=""
    for letter in data:
        output = output + letter
        pair = output[-2:]
        if pair in combines:
            output = output[:-2] + combines[pair]
        else:
            for possible in output[:-1]:
                if possible+letter in opposed:
                    output = ""

    print ("Case #" + str(t) + ": [" + ", ".join(output)+ "]")

f.close();
