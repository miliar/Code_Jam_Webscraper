def add_dir(node, di):
    cur = node
    for d in di:
        if not d in cur:
            cur[d] = {}
        cur = cur[d]

def create_dir(node, di):
    cur = node
    count = 0
    for d in di:
        if not d in cur:
            cur[d] = {}
            count += 1
        cur = cur[d]
    return count

if __name__ == '__main__':
    fin = 'A-large.in'
    fon = 'A-large.out'
    
    fi = open(fin, 'r')
    fo = open(fon, 'w')
    
    c = int(fi.readline())
    for i in xrange(c):
        n, m = [int(x) for x in fi.readline().split(' ')]
        root = {}
        for _ in xrange(n):
            line = fi.readline().strip()
            add_dir(root, line.split('/')[1:])
        count = 0
        for _ in xrange(m):
            line = fi.readline().strip()
            count += create_dir(root, line.split('/')[1:])
        fo.write("Case #%d: %s\n" % (i + 1, count))
    
    print "Done!"
    fi.close()
    fo.close()

