
def get_wt(tree):
    #print tree
    return tree.split(None,2)[1]
        
def get_feature(tree):
    t = tree.split(None,3)[2]
    if t == ')':
        return None
    return t    

def get_children(tree):
    rem = tree.split(None,3)[3]
    list = rem[0:len(rem)-1]    
    count = 0
    index = 0
    ret = [1,2]
    for i in list:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count == 0:
            ret[0] = list[0:index+1]
            ret[1] = list[index+1:]
            return ret
        index += 1
    return None

def get_prob(features, prob, tree):
    wt = get_wt(tree)
    #print wt
    prob *= float(wt)
    c_f = get_feature(tree)
    if c_f == None:
        return prob
    if c_f in features:
        return get_prob(features, prob, get_children(tree)[0])
    else:
        return get_prob(features, prob, get_children(tree)[1])

def fix_tree(tree):
    ret = ""
    for i in tree:
        if i == ')':
            ret += ' '
        ret += i
        if i == '(':
            ret += ' '
    return ret


if __name__ == "__main__":    
    T = int(raw_input())
    for kase in range(0,T):
        L = int(raw_input())
        tree = ""
        for i in range(0,L):
            tree += raw_input() + " "
        tree = fix_tree(tree)
        #print tree
        ###print raw_input()
        A = int(raw_input())
        print "Case #%s:" % str(kase+1)
        for ii in range(0,A):
            features = []
            input = raw_input()

            N = int(input.split()[1])
            features = input.split()[2:]
            
            print "%.7f" % float(get_prob(features, 1.0, tree))
            
            
