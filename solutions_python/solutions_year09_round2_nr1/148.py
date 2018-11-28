class tree:
    def __init__(self, weight=None, name=None, subtree=[], level=None):
        self.subtree = []
        self.weight = weight
        self.name = name
        self.level = level

    def __str__(self):
        return str(self.level)+' '+self.name+' '+str(self.weight)

def get_next_item(line,i):
    n = i
    while True:
        n = n + 1
        if (line[n] in [' ',')','(']) and ((n - i) >= 2):
            return (line[i:n], n)
        elif line[n] in [' ',')','(']:
            i = i + 1
        else:
            continue

def find_matching(line,i):
    assert line[i] == '('
    n = 0
    for j in range(i,len(line)):
        if line[j] == '(':
            n += 1
        elif line[j] == ')':
            n -= 1

        if n == 0:
            return j
    return i

def find_next(line,i):
    for j in range(i,len(line)):
        if line[j] == '(':
            return j
    return -1

def build_line(lines):
    tmp = []
    for line in lines:
        tmp.append(line.strip() + ' ')
    return ' '.join(tmp)

def parse(line):
    root = tree()
    start = find_next(line,0)
    end = find_matching(line,start)
    first_flag = True

    next_1 = start
    while True:
        next_1 = find_next(line,next_1+1)
        if next_1 != -1:
            next_1_end = find_matching(line,next_1)
            root.subtree.append(parse(line[next_1:next_1_end+1]))
            if first_flag == True:
                first_flag = False
                args = line[start+1:next_1]
                args = args.split()
                if len(args) == 1:
                    root.weight = float(args[0])
                elif len(args) == 2:
                    root.weight = float(args[0])
                    root.name = args[1]
                else:
                    assert False,'args: %s' % str(args)
            next_1 = next_1_end
        else:
            if first_flag == True:
                first_flag = False
                args = line[start+1:end]
                args = args.split()
                if len(args) == 1:
                    root.weight = float(args[0])
                elif len(args) == 2:
                    root.weight = float(args[0])
                    root.name = args[1]
                else:
                    assert False,'args: %s' % str(args)
            break

    return root

def cute_rate(root, af):
    p = 1.0
    cur = root
    if cur.name != None:
        if cur.name in af:
            return p*cute_rate(cur.subtree[0], af)*cur.weight
        else:
            return p*cute_rate(cur.subtree[1], af)*cur.weight
    else:
        return p*cur.weight
