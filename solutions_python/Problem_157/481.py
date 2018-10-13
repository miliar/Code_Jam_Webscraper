
INPUT = "C-small-attempt1.in"
OUTPUT = "C-small-attempt1.out"

mul = {('1','1'):'1',('1','-1'):'-1', ('-1','1'):'-1',('-1','-1'):'1',
     ('1','i'):'i', ('-1','i'):'-i',('1','-i'):'-i',('-1','-i'):'i',
     ('1','j'):'j', ('-1','j'):'-j',('1','-j'):'-j',('-1','-j'):'j',
     ('1','k'):'k', ('-1','k'):'-k',('1','-k'):'-k',('-1','-k'):'k',
     ('i','1'):'i', ('i','-1'):'-i',('-i','1'):'-i',('-i','-1'):'i',
     ('i','i'):'-1',('i','-i'):'1',('-i','i'):'1',('-i','-i'):'-1',
     ('i','j'):'k',('i','-j'):'-k',('-i','j'):'-k',('-i','-j'):'k',
     ('i','k'):'-j',('i','-k'):'j',('-i','k'):'j',('-i','-k'):'j',
     ('j','1'):'j',('j','-1'):'-j',('-j','1'):'-j',('-j','-1'):'j',
     ('j','i'):'-k',('j','-i'):'k',('-j','i'):'k',('-j','-i'):'-k',
     ('j','j'):'-1',('j','-j'):'1',('-j','j'):'1',('-j','-j'):'-1',
     ('j','k'):'i',('j','-k'):'-i',('-j','k'):'-i',('-j','-k'):'i',
     ('k','1'):'k',('k','-1'):'-k',('-k','1'):'-k',('-k','-1'):'k',
     ('k','i'):'j',('k','-i'):'-j',('-k','i'):'-j',('-k','-i'):'j',
     ('k','j'):'-i',('k','-j'):'i',('-k','j'):'i',('-k','-j'):'-i',
     ('k','k'):'-1',('k','-k'):'1',('-k','k'):'1',('-k','-k'):'-1'
     }

def find_k(S):
    if (len(S)<1):
        return False
    if (len(S) == 1):
        if (S[0] == 'k'):
            return True
        else:
            return False
    m = mul[(S[0],S[1])]
    index = 2
    while (index < len(S)):
        m = mul[(m,S[index])]
        index+=1
    if (m == 'k'):
        return True
    else:
        return False

def find_jk(S):
    if (len(S)<2):
        return False
    if (len(S)==2):
        return (S[0]=='j' and S[1]=='k')
    m = mul[(S[0],S[1])]
    index = 2
    while (index < (len(S)-1)):
        m = mul[(m,S[index])]
        if (m == 'j'):
            if (find_k(S[index+1:])):
                return True
        index+=1
    return False

def calc_seq_mul(seq):
    if (len(seq) == 1):
        return seq
    m = mul[(seq[0],seq[1])]
    index = 2
    while (index < len(seq)):
        m = mul[(m,seq[index])]
        index+=1
    return m

def calc_power(base,power):
    pass

def solve(L,X,S):
    data = X * S
    if (len(data)<3):
        return "NO"
    if (calc_seq_mul(data) != '-1'):
        return "NO"
    if (data[0] == 'i'):
        if find_jk(data[1:]):
            return "YES"
    
    m = mul[(data[0],data[1])]
    index = 2
    while (index < (len(data) -1) ) :
        m = mul[(m,data[index])]
        if (m == 'i'):
            if find_jk(data[index+1:]):
                return "YES"
        index+=1
    return "NO"

if __name__=="__main__":
    f_in = open(INPUT)
    f_out = open(OUTPUT,"w")
    lines = f_in.readlines()
    output = []
    cases = int(lines[0].strip())
    for i in range(cases):
        data = lines[2*i+1].strip().split(" ")
        L = data[0]
        X = int(data[1])
        S = lines[2*i+2].strip()
        output += "Case #%d: %s\n" % (i+1,solve(L,X,S))
        print i
        
    f_out.writelines(output)
    f_out.close()
    f_in.close()
    print 'done.'

