import sys

def flip(string):
    s, k = string.split()
    s = list(s)
    k = int(k)
    
    total = len(s)
    flips = 0
    #if +, turn -, if - turn +
    for i, c in enumerate(s):
        if c == "-":
            if (total - i) >= k:
                flips += 1
                #flip
                for j in range(0,k):
                    if s[i+j] == "-":
                        s[i+j] = "+"
                    else:
                        s[i+j] = "-"
            else:
                return "IMPOSSIBLE"
    #return IMPOSSIBLE or # of flips
    return flips


def main():
    with open(sys.argv[1], 'r') as infile:
        for i, line in enumerate(infile):
            if i == 0:
                continue
            print("Case #" + str(i) + ": " + str(flip(line)) )

if __name__ == "__main__":
    main()