import sys


def main():
    # Read standard input
    lines = sys.stdin.readlines()
    # For each sample input S : count ==  (lines[0])
    for s in range(int( lines[0] )):
        curr_params = lines[s+1].split()
        curr_S = list(curr_params[0])
        curr_K = int(curr_params[1])
        # print(curr_S)
        # print(curr_K)
        # For len(S) - len(K)
        counter = 0
        for i in range(len(curr_S) - curr_K + 1):
            # print "S[i] : " + curr_S[i]
            # If i^th elem is "-" then flip consecutive K & increment counter
            if curr_S[i] == "-":
                for idx in range(curr_K):
                    flip_idx = idx + i
                    if curr_S[flip_idx] == "-":
                        curr_S[flip_idx] = "+"
                    else:
                        curr_S[flip_idx] = "-"
                counter += 1
        # Output counter OR "IMPOSSIBLE" if last K digits != 1's
        isImpossible = False
        for i in range(len(curr_S)):
            if curr_S[i] != "+":
                isImpossible = True
        if isImpossible:
            print ("Case #"+ str(s+1) + ":" + " IMPOSSIBLE")
        else:
            print ("Case #"+ str(s+1) + ": " + str(counter))

main()
