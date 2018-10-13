import sys

with open(sys.argv[1]) as f:
    for n in range(int(f.readline().strip())):
        print("Case #",str(n+1),": ",sep="")
