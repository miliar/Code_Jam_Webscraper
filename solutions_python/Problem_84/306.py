import sys, math
from multiprocessing import Pool


def main(data):
    R,C,s = data
    for i in range(R):
        for j in range(C):
            try:
                if s[i][j] == "#": 
                    if s[i][j+1] == "#" and s[i+1][j] == "#" and s[i+1][j+1] == "#":
                        s[i][j] = "/"
                        s[i][j+1] = "\\"
                        s[i+1][j] = "\\"
                        s[i+1][j+1] = "/"
                    else:
                        return "Impossible"
            except:
                return "Impossible"
    return "\n".join(["".join(l) for l in s])
        
if __name__ == "__main__":
    mode = 0
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        mode = 1
    else:
        f = open("test.txt")
    T = int(f.readline())
    data = []
    for i in range(T):
        R,C = map(int, f.readline().strip().split())
        s = list()
        for j in range(R):
            s.append(list(f.readline().strip()))

        data.append((R, C, s))
    if mode == 1:
        pool = Pool()
        r = pool.map(main, data)
    else:
        r = map(main, data)
    for i in range(T):
        print "Case #%d: \n%s" % (i+1, r[i]) 