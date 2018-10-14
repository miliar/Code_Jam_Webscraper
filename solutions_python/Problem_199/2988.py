""" CodeJam 2017 """

def read(file_name):
    with open(file_name, 'r') as ifile:
        return ifile.readlines()

def solver(cakes, k):
    new_cakes = [1 if x == '+' else 0 for x in cakes]
    i = 0
    c = 0
    while i < len(new_cakes):
        if new_cakes[i] == 0:
            if i+k > len(new_cakes):
                return 'IMPOSSIBLE'
            j = i
            c += 1
            while j < i+k:
                new_cakes[j]= 1-new_cakes[j]
                j += 1
        i += 1
    return c
    
def main():
    file_name = '/Users/lliu/Downloads/A-large.in'
    lines = read(file_name)
    tests = lines[1:]
    for i, test in enumerate(tests):
        testcase = test.split()
        if len(testcase) < 2:
            r = 'IMPOSSIBLE'
            continue
        r = solver(testcase[0], int(testcase[1]))
        print 'Case #{}: {}'.format(i+1, r)

if __name__=='__main__':
    main()