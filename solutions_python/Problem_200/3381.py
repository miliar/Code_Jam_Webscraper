def last_tidy(N):
    assert(type(N) == list)
    
    if len(N) == 1:
        return N
    
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            if N[i+1] == '0':
                print('yes')
                N.pop()
            N[i] = str(int(N[i]) - 1)
            for j in range(i+1,len(N)):
                N[j] = '9'
            return last_tidy(N)
    return(N)

if __name__ == '__main__':
    import sys,re
    data = iter(sys.stdin.read().splitlines())
    next(data)
    
    for (case_num, case) in enumerate(data):
        print('Case #{}: {}'.format(case_num+1, int(''.join(last_tidy(list(case))))))
