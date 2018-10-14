# omar.gomez#gmail.com

N = input()
#print N


for case in xrange(N):
    L = input()
    tree = "" 
    for _ in xrange(L):
        tree = tree + raw_input()
    
    tree_len = len(tree)

    def get_token(tree, len, pos):
        if pos >= len: return None, pos

        c = tree[pos]
        while pos < len and c == ' ':
            pos += 1
            c = tree[pos]

        if pos >= len: return None, pos

        if c == '(' or c == ')':
            return c, pos+1
        elif c.isdigit():
            tok = ''
            while c == '.' or c.isdigit():
                tok = tok + c
                pos += 1
                c = tree[pos]

            return tok, pos
        else:
            tok = ''
            while c.isalpha():
                tok = tok + c
                pos += 1
                c = tree[pos]

            return tok, pos

    #print "tree:", tree 
    print "Case #%d:" % (case+1)
    A = input()
    for _ in xrange(A):
        animal = raw_input().split()
        features = animal[2:2+int(animal[1])]
        tree_pos = 0

        def do_tree(p):
            global features, tree_pos, tree, tree_len
            t, tree_pos = get_token(tree, tree_len, tree_pos)
            #print t
            t, tree_pos = get_token(tree, tree_len, tree_pos)
            #print t
            prob = p * float(t)

            t, tree_pos = get_token(tree, tree_len, tree_pos)

            if t == ')':
                return prob
            else:
                result1 = do_tree(prob)
                result2 = do_tree(prob)
                _, tree_pos = get_token(tree, tree_len, tree_pos)

                if t in features:
                    return result1
                else:
                    return result2
            

        def process():
            global features, tree_pos, tree, tree_len
            t, tree_pos = get_token(tree, tree_len, 0)
            t, tree_pos = get_token(tree, tree_len, tree_pos)
            prob = float(t)
            
            t, tree_pos = get_token(tree, tree_len, tree_pos)

            if t == ')':
                return prob
            else:
                if t in features:
                    return do_tree(prob)
                else:
                    do_tree(prob)
                    return do_tree(prob)


        #print features
        p = process()

        print "%.7f" % (p)

    # doit...   

    #t, p = get_token(tree, tree_len, 0 )
    #while t != None:
    #    print "Token: ", t
    #    t, p = get_token(tree, tree_len, p )






