
def read(file_name):
    with open(file_name, 'r') as ifile:
        lines = ifile.readlines()
    return [line.strip() for line in lines]

def solver(D, input):
    test = []
    for line in input:
        row = line.split()
        test.append([int(cell) for cell in row])
    runtimes = [float(D-t[0])/t[1] for t in test]
    return D/max(runtimes)
    

def main():
    file_name = 'q1large0'
    lines = read(file_name)
    T = int(lines[0])
    r = 1
    for i in range(0, T):
        fl = lines[r].split()
        D = int(fl[0])
        N = int(fl[1])
        test = lines[r+1:r+N+1]
        r += N+1
        res = solver(D, test)
        print 'Case #{}: {}'.format(i+1, res)

if __name__=='__main__':
    main()