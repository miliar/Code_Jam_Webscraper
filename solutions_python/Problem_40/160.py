import pprint

def traverse(string, pos, node):
    i1 = string.find('(', pos) + 1
    while (string[i1]==' ') or (string[i1] == '\n'):
        i1 += 1
    i2 = i1
    while (string[i2]!=' ') and (string[i2] != '\n') and (string[i2]!='(') and (string[i2]!=')'):
        i2 += 1
    #i2 -= 1
    #i2 = min((string.find(' ', i1), string.find('\n', i1), string.find(')', i1)))
    #print(s[i1:i2]) 
    node.append(float(s[i1:i2]))
    i1 = i2
    while (string[i1]==' ') or (string[i1] == '\n'):
        i1 += 1
    if string[i1] == ')':
        node.append(0)
        return i1
    node.append(1)
    i2 = min((string.find(' ', i1), string.find('\n', i1), string.find('(', i1)))
    node.append(str(s[i1:i2]))
    subnode1 = []
    node.append(subnode1)
    subnode2 = []
    node.append(subnode2)
    return traverse(string, traverse(string, i2, subnode1), subnode2)

def calc(x, f, node):
    x = x * node[0];
    if node[1]:
        if node[2] in f:
            return calc(x, f, node[3])
        else:
            return calc(x, f, node[4])
    else:
        return x

if __name__ == "__main__":
    fin  = open('d:\\a.in', 'r')
    fout = open('d:\\a.out', 'w')
    N = int(fin.readline())
    for i in range(1, N+1):
        print('Line %d' % i)
        fout.write('Case #%d:\n' % i)
        L = int(fin.readline())
        s = '';
        for j in range(L):
            s += fin.readline()
        tree = []
        traverse(s, 0, tree)
        #pprint.pprint(tree)
        A = int(fin.readline())
        for j in range(A):
            line = fin.readline().split()
            line = line[2:len(s)]
            fout.write('%6f\n' % calc(1, line, tree))