import sys, re




def solve(row1, row2):
    diff = set(row1).intersection(set(row2))
    if len(diff) == 0:
        return 'Volunteer cheated!'
    elif len(diff) == 1:
        return list(diff)[0]
    else:
        return 'Bad magician!'


def main(filename):
    with open(filename) as f_in:
        total = int(f_in.readline())
        for i in range(1, total+1):
            guess1 = int(f_in.readline())
            for j in range(1, 5):
                if j == guess1:
                    row1 = map(int, f_in.readline().strip().split(' '))
                else:
                    f_in.readline()
            guess2 = int(f_in.readline())
            for j in range(1, 5):
                if j == guess2:
                    row2 = map(int, f_in.readline().strip().split(' '))
                else:
                    f_in.readline()
            #print guess1, row1, guess2, row2
            print 'Case #{0}: {1}'.format(i, solve(row1, row2))
            

if __name__ == "__main__":
    main(sys.argv[1])
