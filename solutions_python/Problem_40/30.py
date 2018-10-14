T = int(raw_input())

def findend(str, i):
   # print "  *%s*   %d" % (str, i)
    j, k = i + 1, 1;
    while k > 0:
        if str[j] == '(': k += 1
        elif str[j] == ')': k -= 1
        j += 1
    return j-1

def maketree(str):
    str = str.strip()
   # print str
    i = str.find(' ')
    if i == -1:
        return (float(str),'','','')
    i = str.find('(', i)
    arr = str[0:i].split()
   # print arr
    j = findend(str, i)
    k = str.find('(', j+1)
    l = findend(str, k)
  #  print " %d %d %d %d" % (i, j, k, l)
    return (float(arr[0]), arr[1], maketree(str[i+1:j]), maketree(str[k+1:l]))

for t in xrange(T):
    print "Case #%d: " % (t+1)
    L = int(raw_input())
    tree = ''
    for x in xrange(L):
        tree += raw_input()
    tree = tree.strip()
    root = maketree(tree[1:-1])
    A = int(raw_input())
    for i in xrange(A):
        ani = raw_input().split()
        node = root
        p = 1.0
        while node[2] != '':
            p *= node[0]
            if node[1] in ani[2:]:
                node = node[2]
            else:
                node = node[3]
        print "%.8f" %(p*node[0])