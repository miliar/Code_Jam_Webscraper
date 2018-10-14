# pancake.py
# do linear pass and find number of moves to flip all pancakes to + from -,
# or indicate impossible.
# google code jam Q17

import sys

def solveOne(s,k):
    numMoves = 0;
    for i in range(len(s)-k+1):
        if s[i] == "-":
            numMoves += 1
            for j in range(k):
                if s[i+j] == "+":
                    s[i+j] = "-"
                else:
                    s[i+j] = "+"

    msg = "Case #" + str(a0+1) + ": "
    if "-" in s:
        msg += "IMPOSSIBLE"
    else:
        msg += str(numMoves)
    return msg

if __name__ == "__main__":
    # print(sys.argv[0])
    # print(len(sys.argv))
    if len(sys.argv) != 2:
        print("python3 pythonfile.py filename")
    else:
        file = open(sys.argv[1], "r")
        data = file.read().splitlines()
        tc = int(data[0].strip())
        # tc = int(input().strip())
        for a0 in range(tc):
            # inp = input().split(" ")
            inp = data[1+a0].split(" ")
            s = list(inp[0])
            k = int(inp[1])

            msg = solveOne(s,k)
            print(msg)
