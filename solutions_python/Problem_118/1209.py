import sys, math

cache = set()

def check_palindrom(value):
    s = str(value)
    for i in range(len(s)/2):
        if not (s[i]==s[-1-i]):
            return False
    return True

with open(sys.argv[2], "w") as outfile:
    with open(sys.argv[1], "r") as infile:
        for i in range(int(infile.readline())):
            lo, up = [int(c) for c in infile.readline().split()]
            count = 0
            for n in range(lo, up+1):
                if n in cache:
                    count += 1
                else:
                    if not check_palindrom(n):
                        continue
                    root = math.sqrt(n)
                    if root % 1.0:
                        continue
                    if check_palindrom(int(root)):
                        count+=1
                        cache.add(n)
            outfile.write("Case #%d: %d\n" % (i+1, count))
                