word = 'welcome to code jam'

def countoccur(i, test):
    if i == 19:
        return 1
    count = 0
    while True:
        j = test.find(word[i])
        if j != -1:
            count += countoccur(i + 1, test[j + 1:]) % 10000
            test = test[j + 1:]
            continue
        break
    return count

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        count = str(countoccur(0, raw_input()))
        print 'Case #%d: %s' % (i + 1, '0000'[:4 - len(count)] + count)

