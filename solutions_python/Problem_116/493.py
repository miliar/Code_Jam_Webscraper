import array

xwin = 88*4
xwin2 = 88*3 + 84

owin = 79*4
owin2 = 79*3 + 84

def winsum(a):
    return (
        # rows
        a[0] + a[1] + a[2] + a[3],
        a[4] + a[5] + a[6] + a[7],
        a[8] + a[9] + a[10] + a[11],
        a[12] + a[13] + a[14] + a[15],
        # cols
        a[0] + a[4] + a[8] + a[12],
        a[1] + a[5] + a[9] + a[13],
        a[2] + a[6] + a[10] + a[14],
        a[3] + a[7] + a[11] + a[15],
        # diags
        a[0] + a[5] + a[10] + a[15],
        a[3] + a[6] + a[9] + a[12]
    )

def main(case, input):
    ar = array.array('b', map(ord, list(input)))
    winsum_r = winsum(ar)
    if xwin in winsum_r or xwin2 in winsum_r:
        print "Case #"+str(case)+": X won"
    elif owin in winsum_r or owin2 in winsum_r:
        print "Case #"+str(case)+": O won"
    elif '.' in input:
        print "Case #"+str(case)+": Game has not completed"
    else:
        print "Case #"+str(case)+": Draw"

if __name__ == '__main__':
    f = open("input.txt", "r")
    num_samples = int(f.readline().strip())

    for i in range(num_samples):
        input = []
        for j in range(4):
            input.append(f.readline().strip())

        main(i+1, ''.join(input))
        f.readline()
