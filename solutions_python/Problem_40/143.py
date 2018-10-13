import sys
input = open(sys.argv[1] + ".in")
output = open(sys.argv[1] + ".out", "w")

import re

class Node:
    def __init__(self, w):
        self.w = w
        self.f = None;
    
    def setup(self, f, l, r):
        self.f = f
        self.l = l
        self.r = r
        return self
    
    def leaf(self):
        return self.feature is None
    
    def eval(self, ff):
        if self.f is None:
            return self.w
        elif self.f in ff:
            return self.w * self.l.eval(ff)
        else:
            return self.w * self.r.eval(ff)
            
    
def parse(s):
    return iparse (s, [])
    
def iparse(s, st):
    for token in re.split("([()])|\s", s):
        if token is None or len(token.strip())==0: continue
        print ">" + token + "<\n"
        if token=='(':
            wc = True
        elif token==')':
            last = st.pop()
            if isinstance(last, Node):
                l2 = st.pop()
                f = st.pop()
                w = st.pop()
                st.append(Node(w).setup(f, l2, last))
            else:
                st.append(Node(last))
        elif wc==True:
            st.append(float(token))
            wc = False
        else:
            st.append(token)
        
    return st.pop()
            
                


cases = int (input.readline())
for i in range(1, cases + 1):
    output.write("Case #" + str(i) + ":\n")
    lines = int(input.readline())
    desc = []
    for j in range(lines):
        desc.append(input.readline())
    tree = parse(''.join(desc))
    ans = int(input.readline())
    for a in range (ans):
        ff = input.readline().split()[2:]
        output.write("%.7f\n" % tree.eval(ff))
        
        