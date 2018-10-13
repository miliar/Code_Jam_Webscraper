def optimal_switches(e, q, ef):
    e1 = e[:]
    sellQ = None
    res = 0
    while q:
        currQ = q.pop(0)
        if currQ in e1:
            e1.remove(currQ)
        if len(e1) == 0:
            e1 = ef[:]
            e1.remove(currQ)
            res += 1
    return res

def main():
    ifile = open('input.txt', 'r')
    ofile = open('output.txt', 'w')
    n = int(ifile.readline())
    for i in range(0, n):
        s = int(ifile.readline())
        engines = []
        for j in range(0, s):
            engines.append(ifile.readline().strip())
        q = int(ifile.readline())
        queries = []
        for j in range(0, q):
            queries.append(ifile.readline().strip())
        y = optimal_switches(engines, queries, engines)
        ofile.write('Case #%i: %i' % (i+1, y))
        if i != (n - 1):
            ofile.write('\n')

    ofile.close()

    print "done"
    
if __name__ == '__main__':
  main()