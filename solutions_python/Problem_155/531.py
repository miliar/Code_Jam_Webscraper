f = open('A-large.in')
#f = open('test.in')
count = int(f.readline())
output = ''
for x in xrange(1, count + 1):
    arr = f.readline().split()
    smax = int(arr[0])
    audience = arr[1]
    needFriends = 0
    total = 0
    for y in xrange(0, smax + 1):
        if total >= y:
            total += int(audience[y])
        else:
            needFriends += y - total
            total = y + int(audience[y])
    output += 'Case #' + str(x) + ': ' + str(needFriends) + '\n'
print(output)
newf = open('output.txt','w')
newf.write(output)
