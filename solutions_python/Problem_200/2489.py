
input_dir = 'inputs/'
output_dir = 'outputs/'
problem = 'B'
size = 'large'


def is_tidy(n):
    u = 9
    while n > 0:
        if n % 10 > u:
            return False
        u = n % 10
        n /= 10
    return True


fin = open(input_dir + problem + "-" + size + '.in')
fout = open(output_dir + problem + "-" + size + '.out', "w")

T = int(fin.readline())
for t in xrange(1, T + 1):
    N = int(fin.readline().strip())
    while True:
        last = '9'
        sum = 0
        n = N
        ex = 1
        while n > 0:
            if n % 10 > last:
                N -= sum + 1
                #print "Sum: {} N: {}".format(sum + 1, N)
                break
            else:
                sum += ex * (n % 10)
                ex *= 10
                last = n % 10
                n /= 10
        else:
            fout.write("Case #{}: {}\n".format(t, N))
            break
fout.close()
