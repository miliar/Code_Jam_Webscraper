
import re, sys



def solve(input):
    ps = [int(c) for c in input[input.find(' ')+1:]]
    n = 0
    t = 0
    for i in range(len(ps)):
        if ps[i] == 0 and t <= i:
            n += 1
            t += 1
        else:
            t += ps[i]
    return n

def main():
    if len(sys.argv) <= 1:
        print("No input")
        sys.exit(1)
    with open(sys.argv[1]) as f_in:
        T = int(f_in.readline().strip())
        for i in range(1, T+1):
            S = solve(f_in.readline().strip())
            print("Case #{0}: {1}".format(i, S))
    
        


if __name__ == "__main__":
    main()
    