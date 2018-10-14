PROBLEM_LENGTH = 2
import sys
lines = map(lambda line:line.strip(),sys.stdin.readlines())
n = int(lines[0])
problem_cases = map(lambda line:line.split(), lines[1:])
assert n*PROBLEM_LENGTH == len(problem_cases)
##
class qua(object):
    def __init__(self,sign,num):
        self.num=num
        self.sign=sign
    def __mul__(self,other):
        a=self.num
        sa=self.sign
        b=other.num
        sb=other.sign
        
        s=sa*sb
        
        if a==b:
            if a=='1':
                return qua(s,'1')
            else:
                return qua(-s,'1')
        elif a=='1' or b=='1':
            if a=='1':
                return qua(s,b)
            else:
                return qua(s,a)
        else:
            if (a,b) in [('i','j'),('j','i')]:
                if a=='i':
                    return qua(s,'k')
                else:
                    return qua(-s,'k')
            elif (a,b) in [('k','j'),('j','k')]:
                if a=='j':
                    return qua(s,'i')
                else:
                    return qua(-s,'i')
            else:
                if a=='k':
                    return qua(s,'j')
                else:
                    return qua(-s,'j')    
    def __repr__(self):
        return str((self.sign,self.num))
##
class quab(object):
    def __init__(self,sign,num):
        self.num=num
        self.sign=sign
    def __mul__(self,other):
        a=self.num
        sa=self.sign
        b=other.num
        sb=other.sign
        s=sa*sb
        if a==b:
            if a=='1':
                return quab(s,'1')
            else:
                return quab(-s,'1')
        elif a=='1' or b=='1':
            if a=='1':
                return quab(s,b)
            else:
                return quab(s,a)
        else:
            if (a,b) in [('i','j'),('j','i')]:
                if a=='i':
                    return quab(-s,'k')
                else:
                    return quab(s,'k')
            elif (a,b) in [('k','j'),('j','k')]:
                if a=='j':
                    return quab(-s,'i')
                else:
                    return quab(s,'i')
            else:
                if a=='k':
                    return quab(-s,'j')
                else:
                    return quab(s,'j')    
    def __repr__(self):
        return str((self.sign,self.num))
##


def prob_solver(*prob_args):
    s1=prob_args[1][0]
    n=int(prob_args[0][1])
    s=s1*n
    t=map(lambda x:qua(1,x),list(s))

    e=qua(1,'1')
    for i in range(len(t)):
        e=e*t[i]
        if e.sign==1 and e.num=='i':
            break
    if i==len(t):
        return 'NO'
    else:
        e=quab(1,'1')
        tb=map(lambda x:quab(1,x),list(s))
        for j in range(len(tb))[::-1]:
            e=e*tb[j]
            if e.sign==1 and e.num=='k':
                break
        if i>=j:
            return 'NO'
        else:
            e=qua(1,'1')
            for n in range(i+1,j):
                e=e*t[n]
            if e.sign==1 and e.num=='j':
                return 'YES'
            else:
                return 'NO'
        
for case_i in range(n):
    print "Case #{case_i}: {solution}".format(case_i=case_i+1,
                                              solution=prob_solver(*problem_cases[PROBLEM_LENGTH*case_i:PROBLEM_LENGTH*case_i+PROBLEM_LENGTH]))