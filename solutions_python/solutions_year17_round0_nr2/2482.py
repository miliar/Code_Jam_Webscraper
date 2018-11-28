with open('input.txt', 'rU') as fin:
    with open('output.txt', 'w') as fout:
        ipt = fin.readlines()
        for i, num in enumerate(ipt):
            if i > 0 and num != '':
                fout.write('Case #')
                fout.write(str(i))
                fout.write(': ')
                j = 0
                length = len(num)
                while num[j] <= num[j+1]:
                    j += 1
                if j != length - 2:
                    while num[j] == num[j-1] and j > 0:
                        j -= 1
                    num = num[0:j] + str(int(num[j])-1) + '9' * (length - j - 2) + "\n"
                fout.write(num.strip("0"))
