mul = {
    ('1','1'): '1',
    ('1','i'): 'i',
    ('1','j'): 'j',
    ('1','k'): 'k',
    
    ('i','1'): 'i',
    ('i','i'): '-1',
    ('i','j'): 'k',
    ('i','k'): '-j',
    
    ('j','1'): 'j',
    ('j','i'): '-k',
    ('j','j'): '-1',
    ('j','k'): 'i',
    
    ('k','1'): 'k',
    ('k','i'): 'j',
    ('k','j'): '-i',
    ('k','k'): '-1'
}

mem = {}

def reduce_quat(exp):
    if exp in mem:
        return mem[exp]
    result = '1'
    for v in exp:
        if('-' in result):
            result = mul[(result[1],v)]
            if('-' in result): #two negations
                result = result[1]
            else:
                result = '-' + result
        else:
            result = mul[(result,v)]
    mem[exp] = result
    return result

def solve(exp):
    if(reduce_quat(exp) != '-1'):
        return False
    len_exp = len(exp) #L*X
    if(len_exp<3):
        return False
    for first in range(len_exp): #search for i
        e1 = exp[:first+1]
        if reduce_quat(e1) == 'i':
            tmp = exp[first+1:]
            if reduce_quat(tmp) == 'i': #j*k
                for second in range(first+1,len_exp):
                    e2 = exp[first+1:second+1]
                    e3 = exp[second+1:]
                    if(reduce_quat(e2) == 'j' and reduce_quat(e3) == 'k'):
                        return True
    return False

T = int(input())
for case in range(T):
    L,X = [int(e) for e in input().split(' ')]
    line = input()*X #small dataset only
    print("Case #",case+1,': ',sep='',end='')
    if(solve(line)):
        print('YES')
    else:
        print('NO')
