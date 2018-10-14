from sys import stdout, stderr, stdin

def read_line():
    return stdin.readline().rstrip('\r\n')

def read_ints():
    line = read_line()
    return map(int, line.rstrip('\r\n').split(' '))

def last_one(n, row):
    #print >> stderr, "last one", n, row
    for i in xrange(n-1, -1, -1):
        if row[i] == '1':
            #print >> stderr, "is", i
            return i
    #print >> stderr, "none"
    return -1

def solve_case(no_rows, rows):
    cur_depth = 0
    to_solve = set()
    blacklist = set()
    to_solve.add(rows)
    blacklist.add(rows)

    while len(to_solve) > 0:
        to_solve_new = set()
        for check_rows in to_solve:
            blacklist.add(check_rows)
            #print >> stderr, "solving", check_rows.rows
            # check if ok
            solved = True
            for i in xrange(no_rows):
                if check_rows[i].rfind('1') > i:
                    solved = False
                    break

            if solved:
                return cur_depth

            # insert sub-solutions there
            for i in xrange(no_rows-1):
                # swap i and i+1
                new_rows = list(check_rows)
                temp = new_rows[i]
                new_rows[i] = new_rows[i+1]
                new_rows[i+1] = temp
                #print >> stderr, "sub-solution", new_rows
                new_rows = tuple(new_rows)

                if new_rows not in blacklist:
                    to_solve_new.add(new_rows)

        to_solve = to_solve_new
        cur_depth += 1

if __name__ == '__main__':
    no_cases = read_ints()[0]
    print >> stderr, "No of cases", no_cases
    for case in xrange(no_cases):
        no_rows = read_ints()[0]
        rows = [0] * no_rows
        for row_ix in xrange(no_rows):
            row = read_line()
            #print >> stderr, row
            rows[row_ix] = row
        print >> stderr, "Solving case", (case+1)
        under_progress = set()
        sol = solve_case(no_rows, tuple(rows))
        print "Case #%d: %d" % (case+1, sol)
        
