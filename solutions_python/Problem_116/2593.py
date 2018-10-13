
def read_input(filename):
    f = open(filename)
    line = f.readline().strip()
    num_cases = int(line)
    for case in range(num_cases):
        lines_sum = [0] * 4
        col_sum = [0] * 4
        diag_sum = [0] * 2
        empty_spaces = False
        for i in range(4):
            line = f.readline().strip()
            line = list(line)
            for j in range(4):
                if line[j] == 'X':
                    lines_sum[i] += 10
                    col_sum[j] += 10
                    if i == j:
                        diag_sum[0] += 10
                    if i == 3 - j:
                        diag_sum[1] += 10
                if line[j] == 'O':
                    lines_sum[i] += 50
                    col_sum[j] += 50
                    if i == j:
                        diag_sum[0] += 50
                    if i == 3 - j:
                        diag_sum[1] += 50
                if line[j] == 'T':
                    lines_sum[i] += 1
                    col_sum[j] += 1
                    if i == j:
                        diag_sum[0] += 1
                    if i == 3 - j:
                        diag_sum[1] += 1
                if not empty_spaces and line[j] == '.':
                    empty_spaces = True

        answer = 0
        for l in lines_sum:
            if l == 31 or l == 40:
                answer = answer | 1 << 1
            if l == 151 or l == 200:
                answer = answer | 1 << 0
        for col in col_sum:
            if col == 31 or col == 40:
                answer = answer | 1 << 1
            if col == 151 or col == 200:
                answer = answer | 1 << 0
        for diag in diag_sum:
            if diag == 31 or diag == 40:
                answer = answer | 1 << 1
            if diag == 151 or diag == 200:
                answer = answer | 1 << 0

        if answer == 0:
            if empty_spaces:
                #not completed
                print "Case #%d: Game has not completed" % (case+1)
            else:
                #draw
                print "Case #%d: Draw" % (case+1)
        elif answer == 1:
            # O won
            print "Case #%d: O won" % (case+1)
        elif answer == 2:
            # X won
            print "Case #%d: X won" % (case+1)
        elif answer == 3:
            # Draw
            print "Case #%d: Draw" % (case+1)

        # Read empty line
        f.readline()


if __name__=='__main__':
    filename = 't1.in'
    read_input(filename=filename)
