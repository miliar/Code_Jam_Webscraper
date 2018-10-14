
def check(case):
    for idx, val in enumerate(case):
        if (idx > 0):
            if case[idx] < case[idx-1]:
                return False
    return True


def tidy(case):
    done = False
    tidy_case = case
    while not done:
        for idx, val in enumerate(case):
            if (idx > 0):
                if case[idx] < case[idx-1]:
                    tidy_case[idx-1] = str(int(tidy_case[idx-1])-1)
                    tidy_case[idx:] = len(tidy_case[idx:])*'9'
                    # print(tidy_case)
        done = check(tidy_case)
        case = tidy_case

    return tidy_case

ff = 'B-large'
with open(ff+'.in') as fi, open(ff+'.out','w') as fo:
    cases = int(fi.readline())
    for t in range(cases):
        case = list(fi.readline())[:-1]
        print(case)
        tidy_case = tidy(case)
        fo.writelines('Case #{}: '.format(t+1)+str(int(''.join(tidy_case)))+'\n')
