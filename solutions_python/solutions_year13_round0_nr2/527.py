import sys

DEBUG = True

def check_possible(row, col, lawn, checked, n, m):
    # check if we could have mowed this row
    if checked[row][col]:
        return True
    ok = []
    for i in range(n):
        if lawn[i][col] > lawn[row][col]:
            ok = []
            break
        elif lawn[i][col] == lawn[row][col]:
            ok.append((i, col))
    if ok:
        for ok_square in ok:
            checked[ok_square[0]][ok_square[1]] = True
        return True
    for j in range(m):
        if lawn[row][j] > lawn[row][col]:
            ok = []
            break
        elif lawn[row][j] == lawn[row][col]:
            ok.append((row, j))
    if ok:
        for ok_square in ok:
            checked[ok_square[0]][ok_square[1]] = True
        return True
    return False

def solver(n, m, lawn):
    checked = [[False]*m for i in range(n)]
    for row in range(n):
        for col in range(m):
            if not check_possible(row, col, lawn, checked, n, m):
                return 'NO'
    return 'YES'

def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())

def rl():
    return sys.stdin.readline()

def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')

def main():
    # open input file
    # input_file = open('infile.txt')
    
    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c+1))
        n, m = ssi(rl())
        lawn = []
        for i in range(n):
            lawn.append(ssi(rl()))
        answer = solver(n, m, lawn)
        output.append('Case #%d: %s\n' % (c+1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()



if __name__=='__main__':
    main()
