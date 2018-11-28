import sys

in_name = 'A-small-0.in'
out_name = 'A-small-0.out'

fin = open(in_name, 'r')
fout = open(out_name, 'w')

class inout:
    IN = fin
    
    @classmethod
    def line(cls, type=str):
        return type(cls.IN.readline().strip())
        
    @classmethod 
    def splitline(cls, type=str):
        return [type(x) for x in cls.IN.readline().split()]


T = inout.line(int)
result = []

for test in range(int(T)):
    #Read input
    A, B = inout.splitline(int)
    strategy = [0] * (A + 2)
    probs = inout.splitline(float)
    prob_correct =  1
    for i in range(A):
        prob_correct *= probs[i]
        
    strategy[0] = (B - A + 1) * (prob_correct) + (2*B - A + 2) * (1 - prob_correct)
    strategy[len(strategy) - 1] = B + 2
    for i in range(1, len(strategy) - 1):
        prob_last_i_wrongs = [x if idx < (A - i) else (1 - x) for idx, x in enumerate(probs)]
        prob_last_i_wrong = 1
        for  j in range(A):
            prob_last_i_wrong *= prob_last_i_wrongs[j]
        strategy[i] = (B - A + 1 + i*2) * (prob_correct + prob_last_i_wrong) \
                        + (2*B - A + 2 + i*2)*(1 - prob_correct - prob_last_i_wrong)
    print strategy
    result.append("Case #%d: %s\n" % (test+1, min(strategy)))

fout.writelines(result)
fout.close()
fin.close()