

case_prefix = 'Case #'

def build_result_string(case_num, verdict):
    return case_prefix + str(case_num) + ': ' + str(verdict)


class Value:
    def __init__(self):
        self.vals = dict()
    
    def put(self, val, result):
        self.vals[val] = result
        
    def contains(self, val):
        if val in self.vals:
            return True
        return False
    
    def get(self, val):
        if val in self.vals:
            return self.vals[val]
        return None
    
    def __str__(self):
        return str(self.vals)


def format(ist):
    s = '['
    l = len(ist)
    for i,c in enumerate(ist):
        s += c
        if not i == l-1:
            s += ', '
    s += ']'
    return s


def add_cur_op(c, cur_op, opp):
    if c in opp:
        opps = opp[c]
        for o in opps:
            if o not in cur_op:
                cur_op[o] = 1
            else:
                cur_op[o] += 1
    #print 'add cur_o',c,cur_op
    return cur_op

def rem_cur_op(c, cur_op, opp):
    if c in opp:
        opps = opp[c]
        for o in opps:
            if o in cur_op:
                cur_op[o] -= 1
                if cur_op[o] == 0:
                    del cur_op[o]
    #print 'rem cur_o',c,cur_op
    return cur_op
    

def handle_seq(seq, com, opp):
    stack = list()
    cur_op = dict()
    
    for c in seq:
        l = len(stack)
        if l == 0:
            stack.append(c)
            cur_op = add_cur_op(c, cur_op, opp)
            continue

        added = False
        top = stack[-1]
        if c in com:
            comb = com[c].get(top)
            if comb is not None:
                stack[-1] = comb
                cur_op = add_cur_op(comb, cur_op, opp)
                cur_op = rem_cur_op(top, cur_op, opp)
                added = True

        if not added and c in cur_op:
            stack = list()
            cur_op = dict()
            added = True

        if not added:
            stack.append(c)
            cur_op = add_cur_op(c, cur_op, opp)
    return format(stack)
        
    
    
            

f = open('B-large.in', 'r')
num_tests = int(f.readline().strip())

for case in range(num_tests):
    tokens = f.readline().strip().split()
    if len(tokens) == 0:
        continue
    opposed = dict()
    combine = dict()
    seq = list()
    
    c = int(tokens[0])
    num_combine = 0
    idx = 1
    while num_combine < c:
        all3 = tokens[idx]
        base1 = all3[0]
        base2 = all3[1]
        non_base = all3[2]

        if base1 not in combine:
            combine[base1] = Value()
        if base2 not in combine:
            combine[base2] = Value()
        combine[base1].put(base2, non_base)
        combine[base2].put(base1, non_base)
        
        num_combine += 1
        idx += 1

    d = int(tokens[idx])
    num_opp = 0
    idx += 1
    while num_opp < d:
        both = tokens[idx]
        base1 = both[0]
        base2 = both[1]

        if base1 not in opposed:
            opposed[base1] = set()
        if base2 not in opposed:
            opposed[base2] = set()
        opposed[base1].add(base2)
        opposed[base2].add(base1)
        
        num_opp += 1
        idx += 1

    n = int(tokens[idx])
    idx += 1
    for i in range(n):
        seq.append(tokens[idx][i])

    print build_result_string(case + 1, handle_seq(seq, combine, opposed))

f.close()
