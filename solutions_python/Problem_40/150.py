#!/usr/bin/python
import sys

def get_cute(animal, features, tree, p = 1):
    """docstring for get_"""
    print features, tree, p
    wt = tree[0]
    p = p * wt 
    if len(tree) == 1:
        return p
        
    if isinstance(tree[1], str) :
        if tree[1] in features:
            return get_cute(animal, features, tree[2], p)
        else:
            return get_cute(animal, features, tree[3], p)
    else:
        return get_cute(animal, features, tree[2], p)

def main():
    """docstring for main"""
    
    f = file(sys.argv[1])
    lines = f.readlines()
    n = int(lines[0].strip())
    f2 = file(sys.argv[1] + ".out", "w")
    lno = 1
    for case in range(n):
        l = int(lines[lno])
        lno = lno + 1
        tree = "".join([x.strip() for x in lines[lno: lno+l]])
        lno = lno + l
        animals = int(lines[lno])
        lno = lno + 1
        print "----", tree
        f2.write("Case #%d:\n" % (case + 1))
        print "Case #%d:" % (case + 1)
        while '(' in tree or ')' in tree:
            for j in range(len(tree)):
                if tree[j] == "(":
                    tree = tree[0:j] + ", [" + tree[j+1:]
                elif tree[j] == ")":
                    tree = tree[0:j] + "]" + tree[j+1:]
        feature = 0
        for j in range(len(tree)-1):
            if tree[j] == ',' and feature == 1: 
                feature = 0
                tree = tree[0:j] + "\"" + tree[j:]

            if tree[j] == ' ':
                if ord(tree[j+1]) >= ord('a') and ord(tree[j+1]) <= ord('z'):
                    tree = tree[0:j] + ",\"" + tree[j+1:]
                    feature = 1
                

        tree = eval(tree[2:])
        print "----", tree
        for i in range(animals):
            x = lines[lno].strip().split(" ")
            ans = get_cute(x[0], x[2:], tree)
            lno = lno + 1
            print "%.7f" % (ans)
            f2.write("%.7f\n" % (ans))

    f2.close()
        
if __name__ == '__main__':
    main()

#(0.2 furry(0.81 fast(0.3)(0.2))(0.1 fishy(0.3 freshwater(0.01)(0.01))(0.1)))
t =     [0.2,  "furry", [0.81,  "fast", [0.3], [0.2], ], [0.1,  "fishy", [0.3,  "freshwater", [0.01], [0.01]], [0.1]]]
