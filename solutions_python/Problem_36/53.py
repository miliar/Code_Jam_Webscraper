# Code Jam Qualifier
# 2/9/2009
# C

inname = 'E:\C.in'

fin = open(inname, 'r')
fout = open('E:\C.out.txt', 'w')

def pad(i):
    if i < 10:
        return '000' + str(i)
    elif i < 100:
        return '00' + str(i)
    elif i < 1000:
        return '0' + str(i)
    return str(i)

N = int(fin.readline().strip())

what = 'welcome to code jam'

for i in range(1, N + 1):
    print(i)
    text = fin.readline().strip()
    memoz = []
    for j in range(0, len(what) + 1):
        memoz.append([0] * len(text))

    count = 0
    for j in range(0, len(text)):
        if text[j] == what[0]:
            count += 1
        memoz[1][j] = count

    for j in range(2, len(what) + 1):
        for k in range(0, len(text)):
            if k != 0:
                memoz[j][k] = memoz[j][k - 1]
                if text[k] == what[j - 1]:
                    memoz[j][k] += memoz[j - 1][k - 1]

#    print(text)
#    for k in range(0, len(memoz)):
#        print(str(k) + ' ' + str(memoz[k]))

    fout.write('Case #' + str(i) + ': ' + pad(memoz[-1][-1] % 10000) + '\n')

fin.close()
fout.close()
