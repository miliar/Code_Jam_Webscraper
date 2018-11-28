reader = open('C-large.in')
writer = open('output-C-large', 'w')
    
test_cases = int(reader.readline())

for kount in range(test_cases):
    n = int(reader.readline())
    candies = map(int, reader.readline().split(' '))
    
    m = candies[0]
    pile = 0
    for item in candies:
        pile ^= item
        if item < m:
            m = item

    if pile == 0:
        writer.write('Case #%s: %s' % (str(kount+1), sum(candies) - m) + '\n')
    else:
        writer.write('Case #%s: NO' % (str(kount+1)) + '\n')

reader.close()
writer.close()
        
