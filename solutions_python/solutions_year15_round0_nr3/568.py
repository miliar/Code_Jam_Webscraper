
PROBLEM_LENGTH = 2

import sys
lines = map(lambda line:line.strip(),sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n*PROBLEM_LENGTH == len(problem_cases)

product_table = {
    "": (1, ""),
    "ii": (-1, ""),
    "jj": (-1, ""),
    "kk": (-1, ""),
    "i": (1, "i"),
    "j": (1, "j"),
    "k": (1, "k"),
    "ij": (1, "k"),
    "ji": (-1, "k"),
    "ik": (-1, "j"),
    "ki": (1, "j"),
    "jk": (1, "i"),
    "kj": (-1, "i")
    
}

class QNum(object):
    
    def __init__(self, name="", sign=1):
        self._sign = sign
        self._name = name
        
    
    def __neg__(self):
        self._sign = -self._sign
        return self
    
    def __mul__(self, qn):
        #print "self.__dict__ = ", self.__dict__
        #print "qn.__dict__ = ", qn.__dict__
        
        assert type(qn) == type(self)
        #print "self._name + qn._name = ",self._name + qn._name
        assert (self._name + qn._name) in product_table.keys()
        
        name_product = product_table[self._name + qn._name]
        #print "name_product = ",name_product
        return type(self)(name=name_product[1], sign=self._sign*qn._sign*name_product[0])
        
    def __eq__(self, qn):
        assert type(qn) == type(self)
        return (qn._name == self._name) and (qn._sign == self._sign)
        


i = QNum("i")
j = QNum("j")
k = QNum("k")
one = QNum("",1)
neg_one = QNum("",-1)


def prob_solver(*prob_args):
    #print "~~~~~~~~~~~~~~~~~~~~~~~~"
    #print "prob_args = ",prob_args
    word_len = int(prob_args[0][0])
    repeat_n = int(prob_args[0][1])
    word_pattern = prob_args[1][0]
    
    #print "word_len = ", word_len
    #print "repeat_n = ", repeat_n
    #print "word_pattern = ", word_pattern
    
    assert word_len == len(word_pattern)
    total_string = word_pattern*repeat_n
    
    #print "total_string = ", total_string
    
    break_points = []
    check_position = 0
    accumulate_product_res = one
    
    while check_position < len(total_string):            
        accumulate_product_res = accumulate_product_res*QNum(total_string[check_position])
        #print "accumulate_product_res = ", accumulate_product_res.__dict__
        
        if len(break_points) == 0:
            
            if accumulate_product_res == i:
                #print "accumulate_product_res == i"
                break_points.append(check_position)
                accumulate_product_res = one
            
        elif len(break_points) == 1:
            
            if accumulate_product_res == j:
                #print "accumulate_product_res == j"
                break_points.append(check_position)
                accumulate_product_res = one
        
        
        elif len(break_points) == 2:
            
            if accumulate_product_res == k:
                #print "accumulate_product_res == k"
                break_points.append(check_position)
                accumulate_product_res = one
                
        
        check_position = check_position + 1
    
    
    #print "break_points = ",break_points
    
    if len(break_points) == 0:
        yes_or_no = False
    else:
        if len(break_points) == 3:
            if break_points[-1]+1 < len(total_string):
                yes_or_no = accumulate_product_res == one
            else:
                yes_or_no = True
            
        else:    
            yes_or_no = False
    
    return "YES" if yes_or_no else "NO"


for case_i in range(n):
    print "Case #{case_i}: {solution}".format(case_i=case_i+1,
                                              solution=prob_solver(*problem_cases[PROBLEM_LENGTH*case_i:PROBLEM_LENGTH*case_i+PROBLEM_LENGTH]))