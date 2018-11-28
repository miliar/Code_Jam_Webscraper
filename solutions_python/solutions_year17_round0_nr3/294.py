from heapq import *

def calc(n, k):
    hp = [(-n,1)]
    d = {n:1}
    i = 0
    while 1:
        # print hp
        elem = heappop(hp)
        ni = -elem[0]
        nc = elem[1]
        while (len(hp) > 0 and hp[0][0] == -ni):
            elem = heappop(hp)
            nc += elem[1]
        i += nc
        if i >= k:
            ni -= 1
            if ni % 2 == 0:
                return str(ni / 2) + " " + str(ni / 2)
            return str(ni / 2 + 1) + " " + str(ni / 2)
        split(ni, nc, hp, d)

def split(ni, nc, hp, d):
    ni -= 1
    if ni % 2 == 0:
        item = (-ni / 2, nc * 2)
        heappush(hp, item)
    else:
        item = (-(ni / 2), nc)
        heappush(hp, item)
        item = (-(ni / 2 + 1), nc)
        heappush(hp, item)


def main():
    inpfile = open("C-large.in", 'r')
    # inpfile = open("input", 'r')
    outfile = open('output', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        
        n = int(linelst[0])
        k = int(linelst[1])
        ret = calc(n, k)
        
        result = "Case #" + str(case) + ": " + str(ret)+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":
    
    main()
    
