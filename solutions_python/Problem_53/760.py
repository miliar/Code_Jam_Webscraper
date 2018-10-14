import sys
cases = int(sys.stdin.readline())
for i in range(1,cases+1):
    args = sys.stdin.readline().split()
    N = int(args[0])
    K = int(args[1])
    print("Case #{0}: {1}".format(i,"ON" if (K+1)%2**N == 0 else "OFF"))
