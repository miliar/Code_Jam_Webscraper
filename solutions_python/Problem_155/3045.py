# Standing Ovation
# _janellaa

def main()-> None:
    outfile = open('output.out', 'w')
    name = input()
    cases = open(name, 'r')
    caselist = cases.readlines()
    tests = int(caselist[0])
    count = 0
    for c in caselist[1:]:
        count += 1
        outfile.write('Case #{}: {}\n'.format(count, case_s(c)))
    cases.close()
    outfile.close()

def case_s(case: str):
    case = case.strip().split()
    smax = int(case[0])
    aud = list(case[1])
    standing = 0
    invite = 0
    for shylevel in range(smax+1):
        if shylevel <= standing:
            standing += int(aud[shylevel])
        else:
            while shylevel > standing:
                standing += 1
                invite += 1
            standing += int(aud[shylevel])
    return invite

def case_in(cases: int):
    result = [] # list of cases
    for i in range(int(cases)):
        result.append(input())
    return result

main()
