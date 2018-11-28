def parse_input(inp_file):
    with open(inp_file) as f:
        num_cases = int(f.readline()[:-1])
        cases = []
        for i in range(num_cases):
            d = int(f.readline()[:-1])
            cases.append(map(int, f.readline()[:-1].split(" ")))
    return cases


def mushroom_monster(cases):
    with open('data.out','w') as f:
        for i in range(len(cases)):
            a,b = execute_case(cases[i])
            print a,b
            f.write('Case #%d: %d %d\n' %( (i+1),a,b) )

def execute_case(case):
    a = 0
    b = 0
    max_diff = 0
    for i in range(1, len(case)):
        tt = case[i-1] - case[i]
        if tt>0:
            a = a + tt
            if tt > max_diff:
                max_diff=tt
    #print max_diff
    rate = max_diff/10.0
    
    for i in range(1, len(case)):
        if case[i-1] < max_diff:
            #print "case", case[i-1]
            b = b + case[i-1]
        else:
            #print "max ", max_diff
            b = b + max_diff
    
    return a,b


if __name__ == '__main__':
    cases = parse_input('data.in')
    #print cases
    #execute_case([10,5,15,5])
    mushroom_monster(cases)
