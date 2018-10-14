from collections import defaultdict
import sys

def solve(c, sr=0, pr=0, sw=0, pw=0):
    if c:
        return max(solve(c[1:], sr + c[0], pr, sw ^ c[0], pw),  solve(c[1:], sr, pr + c[0], sw, pw ^ c[0]))
    elif sr and pr and sw == pw:
        return sr

def go(filename):
    with open(filename) as f:
        with open("out.txt", "w") as output:
            for case in range(1, int(f.readline()) + 1):
                f.readline()            
                result = solve([int(v) for v in f.readline().split()])
                output.write("Case #%d: %s\n" % (case, result if result else "NO"))          

def main():
    if len(sys.argv) < 1:
        print "Usage: %s <filename>" % os.path.basename(sys.argv[0])
    else:
        go(sys.argv[1])

if __name__ == "__main__":
    main()
