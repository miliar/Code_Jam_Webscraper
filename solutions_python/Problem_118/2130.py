import math

with open('in.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

output = []

n = int(lines[0])

def is_palindrome(num):
    num = str(num)
    return (num == num[::-1])

for i in xrange(0,n):
    count = 0
    case = lines[i+1]
    case = case.split(" ")
    start = int(case[0])
    end = int(case[1])

    start_sq = int(math.ceil(math.sqrt(start)))
    end_sq = int(math.floor(math.sqrt(end)))

    for num_sq in xrange(start_sq, end_sq+1):
        if is_palindrome(num_sq) and is_palindrome(int(math.pow(num_sq,2))):
            count += 1

    text = 'Case #' + str(i+1) + ': ' + str(count)
    #print text
    output.append(text)

with open('out.txt', 'w') as f:
    f.write('\n'.join(output)+'\n')
