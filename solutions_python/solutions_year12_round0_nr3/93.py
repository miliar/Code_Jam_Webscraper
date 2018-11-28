if __name__ == '__main__':
    f = open('C-large.in')
    output = open('C-large.out', 'w')
    test_case = int(f.readline())
    for i in range(test_case):
        line = f.readline()
        poss = 0
        l = line.split()
        A = int(l[0])
        B = int(l[1])
        length = len(str(A))
        for n in range(A, B):
            l_num = []
            str_n = str(n)
            for j in range(1, length):
                num = int(str_n[j:] + str_n[:j])
                if (num <= B) and (num > n) and not (num in l_num):
                    l_num.append(num)
                    poss += 1
        output.write('Case #%s: %s\n' %(i+1, poss))
    f.close()
    output.close()