## QUESTION 4

def calc_perm_lengths(perm_lst,number):
    perm_lst = [(x - 1) for x in perm_lst]
    been_here = [False] * number
    perm_lengths = []
    for i in range(number):
        if been_here[i] == False:
            hoop_length = 1
            x = perm_lst[i]
            while(x != i):
                been_here[x] = True
                x = perm_lst[x]
                hoop_length +=1

            perm_lengths.append(hoop_length)

    perm_lengths = [l for l in perm_lengths if l > 1]

    return sum(perm_lengths)
            
def calc_perm_lengths_ver2(perm_lst,number):
    positioned = 0
    for i in range(number):
        if i == perm_lst[i] - 1:
            positioned += 1
    return number - positioned

def solve(filename, out_file):
    lines = [x[:-1] for x in open(filename).readlines()]
    out = open(out_file, 'a')
    times = int(lines[0])
    for i in range(1, times + 1):
        out.writelines('Case #%d: %d\n' % (i, calc_perm_lengths([int(x) for x in lines[2*i].split(' ')], int(lines[2*i - 1]))))
