f_in = 'D-small-attempt0.in'
f_out = 'D-small-attempt0.out'

w1 = 'GABRIEL'
w2 = 'RICHARD'

f = open(f_in, 'r')
o = open(f_out, 'w')

T = int(f.readline())

def main():
    """ Brute force taking advantage of limitations: X, R, C <= 4 """
    with f:
        data = f.readlines()

    winner = w1
    for case_num_minus1, line in enumerate(data):
        case = [int(i) for i in line.split()]   # [X, R, C]
        x = case[0]
        r = case[1]
        c = case[2]

        if (x == 4 and (r < 3 or c < 3)) or (x > r and x > c) or ((r*c)%x != 0):
            winner = w2
        elif (x == 3 and (r < 2 or c < 2)):
            winner = w2
        else:
            pass

        o.write(("Case #{0}: {1}\n").format(str(case_num_minus1 + 1), winner))
        winner = w1     # Reset

if __name__ == "__main__":
    main()
