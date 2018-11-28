
import sys

lines = map(lambda line:line.strip(), sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n*2 == len(problem_cases)

if n==5:
    test_prob_sol = [ "NO","YES","NO","YES","NO"]
else:
    test_prob_sol = [ "NO","YES","NO","YES","NO"]

class qn:
    
    def __init__(self, char, sign = 1):
        assert char in ["1","i","j","k"]
        
        self.char = char
        self.sign = sign
    def __mul__(self, other):
        
        sign = self.sign *other.sign
        
        table = {
            "ij":qn("k", sign),
            "ik":qn("j",-sign),
            "ji":qn("k",-sign),
            "jk": qn("i",sign),
            "ki": qn("j",sign),
            "kj": qn("i",-sign)
        }
        
        if self.char == "1":
            return qn(other.char, sign)
        elif other.char == "1":
            return qn(self.char, sign)
        elif self.char == other.char:
            return qn("1", -1*sign)
        else:
            return table["%s%s" % (self.char, other.char)]
    
    def __neg__(self):
        return qn(self.char, self.sign * -1)
    
    def __eq__(self,other):
        return  (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        if self.sign == 1:
            return self.char
        else:
            return "-%s" % self.char

    

def evaluate(X, word):
    
    if L == 1:
        return False
    else:
        Iget = False
        Jget = False
        Kget= False
        product = qn("1")
        for i in range(X):
            for s in word:
                #print "%s * %s = %s " % (product, qn(s), qn(s) *product)
                product = product* qn(s) 
                if (not Iget) and product.char == "i":
                    Iget = True
                    product = qn("1",product.sign)
                    #print "got i "
                if (Iget and not Jget) and product.char == "j":
                    Jget = True
                    product = qn("1",product.sign)
                    #print "got j "
                if (Iget and Jget and not Kget) and product.char == "k":
                    Kget = True
                    product = qn("1",product.sign)
                    #print "got k "
                
            #print product==qn("1")
                
        return Iget and Jget and Kget and product ==qn("1")

for case_i in range(n):
    solution = "YES"
    L, X = map(int, problem_cases[case_i*2])
    word = problem_cases[case_i*2+1][0]
    
    solution=  "YES" if evaluate(X, word) else "NO"
    
    
    #print "Case #{0}: {1} {2} {3}".format(case_i, test_prob_sol[case_i] , solution, test_prob_sol[case_i] ==solution)
    print "Case #{0}: {1}".format(case_i+1, solution )
    #print "Case #{0}: {1}, {2}, {3},{4},{5}".format(case_i+1, solution,L,X,word, test_prob_sol[case_i]==solution )