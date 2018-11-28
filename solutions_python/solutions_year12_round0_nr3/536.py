import cProfile


def getRecycled(number, start, end):
    s = str(number)
    rs = {}
    rs[number] = 0
    r = s
    for i in xrange(0, len(s) - 1):
        r = r[-1]+r[:-1]
        n = int(r)
        if n != number and n >= start and n <= end and not rs.has_key(n):
            rs[n] = 0
    return rs.keys()

def countRecycled(start, end):
    generated = {}
    count = 0 
    for i in xrange(start, end+1):
        if generated.has_key(i):
            continue
        recycled = getRecycled(i, start, end)
        nr = len(recycled)
        count += (nr * (nr - 1) / 2)
        for r1 in recycled:
            generated[r1] = 0
    return count
    
    
def main():
    f = open("input.txt")
    out = open("output.txt", "w")
    nr = int(f.readline())
    for i in range(1, nr + 1):
        problem = f.readline().strip()
        start = int(problem.split()[0])
        end = int(problem.split()[1])
        count = countRecycled(start, end)
        s = "Case #" + str(i) + ": " + str(count)
        print s
        out.write(s+"\n")
    f.close()
    out.close()    

if __name__ == '__main__':
    main()