import string

def numofsets():
    fro = long(sets[0])
    too = long(sets[1])
    if too <= 10:
        return 0
    count = 0
    comb = {}
    temp = ''
    digit = 0
    for i in range(fro, too + 1):
        temp = str(i)
        for k in range(1, len(temp)):
            digit = long(temp[-k:] + temp[0:len(temp) - k])
            itemp = long(temp)
            if itemp == digit or digit in comb.keys():
                continue
            if comb.get(itemp) != digit and digit in range(fro, too + 1):
                comb[itemp] = digit
                count += 1
    return count


fname = 'C-large'
objfile = open('/Users/lovekumar/Desktop/%s.in' % fname, 'r')
result = []
output = ''
num = 0
counter = 0

for line in objfile.readlines():
    if not num:
        num = long(line.replace('\n', ''))
        continue
    counter += 1
    sets = [i for i in line.replace('\n', '').split(' ')]
    output = numofsets()
    result.append('Case #%s: %s' % (counter, output))
 
  
objfile.close()
objfile = open('/Users/lovekumar/Desktop/%s.out' % fname, 'w')
objfile.write(string.join(result, '\n'))
objfile.close()
print string.join(result, '\n')
