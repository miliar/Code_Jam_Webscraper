# Google Code Jam 2017 Round 2
# Problem B. Tidy Numbers

def tidy(N):
    length = len(N)
    for i in range(1, length):
        if int(N[i]) < int(N[i - 1]):
            x = [N[j] for j in range(i - 1)]
            x += [str(int(N[i - 1]) - 1)]
            x += (length - i)*['9']
            for j in range(i - 1):
                first = x[i - (j + 2)]
                second = x[i - (j + 1)]
                if first > second:
                    x[i - (j + 2)] = str(int(first) - 1)
                    x[i - (j + 1)] = '9'
            if x[0] == '0':
                x = x[1:]
            y = ''
            for i in x:
                y += i
            return y
    return N

def clean():
    f = open('tidy.txt', 'r')
    g = open('cleaned.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            g.write('Case #' + str(line) + ': ')
            g.write(tidy(i[:-1]) + (line != T)*'\n')
            line += 1
    f.close()
    g.close()
