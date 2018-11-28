import sys

def is_tidy(n):
    last = 0
    for c in str(n):
        if int(c) < last:
            return False
        last = int(c)
    return True

def last_tidy(n):
    str_n = str(n)
    last = str_n[0]

    # for i in range(1, len(str_n)):
    #     if str_n[i] == last and str_n[i:] != last * (len(str_n[i:])):
    #         last = str_n[i]
    #         str_n = str_n[:i] + "0" + str_n[i+1:] 
    #     else:
    #         last = str_n[i]
    # print(n, str_n)
    n = int(str_n)

    for i in range(n, 0, -1):
        if is_tidy(i):
            return i
    return 0

def parser(filename):
    with open(filename.replace('in','out'), 'w') as o:
        with open(filename) as f:
            cases = int(f.readline())
            print("{} cases".format(cases))

            for i in range(cases):
                n = f.readline().replace('\n','')
                o.write('Case #{}: {}\n'.format(i+1, last_tidy(int(n))))


if __name__ == "__main__":
    parser(sys.argv[1])
