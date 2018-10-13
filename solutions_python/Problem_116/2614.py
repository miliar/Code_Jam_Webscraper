ifile = open('input.txt')
ofile = open('output.txt', 'w')
t =  int(ifile.readline())
for tst in range(t):
    answer = None
    try:
        s = [ifile.readline().strip() for i in range(4)]
        def check_line(s):
            a = b = c = 0
            for i in s:
                if i == '.':
                    return None
                if i == 'X':
                    a += 1
                elif i == 'T':
                    c += 1
                else:
                    b += 1
            if a != 0 and b != 0 or c > 1:
                return None
            if a == 0:
                return 'O'
            else:
                return 'X'
        def combine(a, b):
            if a is None:
                return b
            return a
        def check_field(field):
            for i in field:
                r = check_line(i)
                if r is not None:
                    return r
            return combine(check_line(field[i][i] for i in range(4)), check_line(field[i][3 - i] for i in range(4)))
        r = combine(check_field(s), check_field(list(zip(*s))))
        if r is None:
            for i in s:
                for j in i:
                    if j == '.':
                        answer = 'Game has not completed'
                        raise ValueError()
            answer = 'Draw'
        else:
            answer = '{} won'.format(r)
    except ValueError:
        pass
    finally:
        print('Case #{}: {}'.format(tst  + 1, answer), file=ofile)
    ifile.readline()