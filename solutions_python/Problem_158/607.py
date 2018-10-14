import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())

    for i in range(t):
        N, R, C = f.readline().split()
        N = int(N); R = int(R); C = int(C)
        times = R*C
        nBy2 = int(N/2)
        if times%2==0 and N==2:
            print("Case #%d: GABRIEL"%(i+1))
            continue
        if R <= nBy2 or C <= nBy2:
            print("Case #%d: RICHARD"%(i+1))
            continue


        if times%N != 0 or N>=7:
            print("Case #%d: RICHARD"%(i+1))
        else:
            print("Case #%d: GABRIEL"%(i+1))
