import copy

def tidyNumbers(filename):
    with open(filename, 'r') as f:
        numTests = f.readline()
        output = open('output.txt', 'w')
        for idx in range(1, int(numTests)+1):
            num = f.readline()[:-1]
            if int(num) < 10 or isTidy(num):
                output.write('Case #%d: %s\n' % (idx, num))
            else:
                nli = list(str(num))
                nnli = []
                if nli[-1] == '0' and nli[-2] > '1':
                    nli[-1] = '9'
                    nli[-2] = str(int(nli[-2])-1)
                    print nli
                for i in range(len(nli)-1):
                    start = nli[i]
                    end = nli[i+1]
                    if end < start:
                        nli[i] = str(int(nli[i])-1)
                        back = 1
                        while nli[i-back] > nli[i]:
                            nli[i-back] = nli[i]
                            back += 1
                        for j in range(i+1, len(nli)):
                            nli[j] = '9'
                        nnli = copy.deepcopy(nli)
                        nnli[i] = '9'
                        otidy = ''.join(nnli)
                        break

                tidy = ''.join(nli)

                if num > otidy:
                    output.write('Case #%d: %s\n' % (idx, str(int(otidy))))
                else:
                    output.write('Case #%d: %s\n' % (idx, str(int(tidy))))

def isTidy(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

tidyNumbers('B-large.in.txt')
