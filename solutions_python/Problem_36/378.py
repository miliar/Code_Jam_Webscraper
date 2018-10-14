word = 'welcome to code jam'

def countoccur(i, test, offset):
    if i == 19:
        return 1
    if i in cache and offset in cache[i] and cache[i][offset] != -1:
        return cache[i][offset]
    count = 0
    j = offset
    while True:
        j = test.find(word[i], j)
        if j != -1:
            count = (count + countoccur(i + 1, test, j + 1)) % 10000
            j += 1
            continue
        break
    if i in cache:
        cache[i][offset] = count
    else:
        cache[i] = {offset: count}
    return count

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        cache = {}
        count = str(countoccur(0, raw_input(), 0))
        print 'Case #%d: %s' % (i + 1, '0000'[:4 - len(count)] + count)
    
