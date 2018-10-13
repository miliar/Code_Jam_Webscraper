import sys

char_mapping = {'.' : 0, 'X' : 1, 'O' : 2, 'T' : 3}

def read_case_line(fileobj):
    line = fileobj.readline().strip()
    mapping = map(lambda c: char_mapping[c], line)
    return list(mapping)
    
def solve(case):
    empty_count = 0
    # row case
    for row in case:
        empty_count += row.count(0)
        x_count = row.count(1)
        o_count = row.count(2)
        t_count = row.count(3)
        
        if x_count+t_count is 4:
            return 0 # x won
        elif o_count + t_count is 4:
            return 1
    
    # col case
    for c in xrange(4):
        col = [case[r][c] for r in xrange(4)]
        x_count = col.count(1)
        o_count = col.count(2)
        t_count = col.count(3)
        
        if x_count+t_count is 4:
            return 0 # x won
        elif o_count + t_count is 4:
            return 1
    
    diag1 = [case[i][i] for i in xrange(4)]
    x_count = diag1.count(1)
    o_count = diag1.count(2)
    t_count = diag1.count(3)
    
    if x_count+t_count is 4:
        return 0 # x won
    elif o_count + t_count is 4:
        return 1
    
    diag2 = [case[i][3-i] for i in xrange(4)]
    x_count = diag2.count(1)
    o_count = diag2.count(2)
    t_count = diag2.count(3)
    
    if x_count+t_count is 4:
        return 0 # x won
    elif o_count + t_count is 4:
        return 1
    
    if empty_count > 0:
        return 2
    return 3

def main(args):
    test_filename = args[1]
    with open(test_filename) as test_file:
        num_cases =  int(test_file.readline().strip())
        for i in xrange(1,num_cases+1):
            case = [read_case_line(test_file) for j in xrange(4)]
            winner = solve(case)
            if winner is 3:
                print "Case #{0}: Draw".format(i,)
            elif winner is 2:
                print "Case #{0}: Game has not completed".format(i,)
            else:
                print "Case #{0}: {1} won".format(i,["X", "O"][winner])
            
            test_file.readline()

if __name__ == "__main__":
    main(sys.argv)
