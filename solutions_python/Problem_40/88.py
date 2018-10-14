def read_file(filename):
    fp = open(filename)
    lines = fp.readlines()
    return lines

def is_cute(filename):
    lines = read_file(filename)
    n = int(lines[0])
    index = 1
    s = ""
    for i in range(n):
        l = int(lines[index])
        tree = lines[index+1:index+1+l]
        treestr = ""
        for x in tree:
            treestr = treestr + x.strip() + " "
        #print treestr.split('(')
        a = int(lines[index+1+l])
        animals = lines[index+2+l:index+2+a+l]
        index = index + a + l + 2
        probs = ""
        for creature in animals:
            features = creature.split()[2:]
            p = treeprob(1,treestr, features)
            probs = probs + str(p) + "\n"        
        s = s + "Case #" + str(i+1) + ":\n" + probs
    return s

def treeprob(p, tree, features):
    tree = tree.strip()
    if tree.find(")") == len(tree) - 1:
        root = float(tree.lstrip("( ").rstrip(" )"))
        return root*p
    rootend = tree.find(" ")
    root = float(tree[:rootend].lstrip("( "))
    p = p*root
    nonroot = tree[rootend+1:]
    q = nonroot[:nonroot.find(" ")]
    nonq = nonroot[nonroot.find(" ")+1:len(nonroot)-1]
    subtrees = splittree(nonq)
    if q in features:
        return treeprob(p,subtrees[0],features)
    else:
        return treeprob(p,subtrees[1],features)

def splittree(tree):
    pcount = 0
    for x in range(len(tree)):
        if tree[x] == '(':
            pcount = pcount + 1
        if tree[x] == ')':
            pcount = pcount - 1
        if pcount == 0:
            return [tree[:x+1],tree[x+1:]]

        


def run(filename):
    a = open("output.txt","w")
    a.write(is_cute(filename))

run("A-large.txt")
