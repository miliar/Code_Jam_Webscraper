line_count = int(raw_input())

def flipPancake(pancake):
    return ''.join(map(lambda s: '-' if s == '+' else '+', pancake))

data = []

def processPancake(pancake, flipperLength, count):
    temp_pancake = pancake
    leftMostNegative = pancake.find('-')

    # print temp_pancake, flipperLength
    if leftMostNegative < 0:
        data.append(count)
        return temp_pancake
    elif leftMostNegative + flipperLength <= len(pancake):
        count += 1
        head = temp_pancake[:leftMostNegative]
        flipPancakes = flipPancake(temp_pancake[leftMostNegative:leftMostNegative + flipperLength])
        tail = temp_pancake[leftMostNegative + flipperLength:]
        return head + processPancake(flipPancakes + tail, flipperLength, count)
    else:
        data.append(count-1)
        return temp_pancake

for i in range(line_count):
    pancakes, flipperLength = raw_input().split(' ')
    flipperLength = int(flipperLength)
    count = 0
    # print pancakes, flipperLength
    result = processPancake(pancakes, flipperLength, count)
    if result.find('-') > 0:
        data[i] = 'IMPOSSIBLE'
    # print i + 1, result, data[i]
    # print '########'
for i, value in enumerate(data):
    print 'Case #{}: {}'.format(i + 1, str(value))

# print processPancake(data[0]['pancakes'], data[0]['flipperLength'])
