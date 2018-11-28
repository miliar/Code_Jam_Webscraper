IN_FILE = 'B-large'

def tidy(x):

    if len(x) == 1:
        return -1

    last = int(x[len(x)-1])
    for i in range(len(x)-2, -1, -1):
        if int(x[i]) > last:
            return i

        last = int(x[i])

    return -1

def tidy_left(x):

    if len(x) == 1:
        return -1

    last = int(x[0])
    for i in range(1, len(x)):
        if int(x[i]) < last:
            return i-1

        last = int(x[i])

    return -1

def break_tie(x, i):

    for j in range(i-1, -1, -1):
        if x[j] != x[i]:
            return j+1
    return 0

def decrement(x, i):

    if x[i] == '0':
        x[i] = '9'
        return decrement(x, i-1)

    x[i] = str(int(x[i]) - 1)

    return x


with open(IN_FILE+'.in', 'r') as infile, open(IN_FILE+'.out', 'w') as outfile:

    T = int(infile.readline().strip())

    for exp_no in range(T):
        N = list(infile.readline().strip())

        i_wrong = tidy_left(N)

        if i_wrong >= 0:
            i_wrong = break_tie(N, i_wrong)

            N = decrement(N, i_wrong)

            for j in range(i_wrong+1, len(N)):
                N[j] = '9'


        # conv to int
        N_int = int(''.join(N))

        outfile.write('Case #'+str(exp_no+1)+': ')
        outfile.write(str(N_int)+'\n')
