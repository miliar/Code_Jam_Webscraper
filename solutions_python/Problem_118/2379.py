import math
seen = set()

data = map(lambda x: x.strip(), open('C-small-attempt0.in', 'r').readlines()[1:])
output = open('output.txt', 'a')
def is_palindrome(num):
    stringed = str(num)
    return stringed in seen or stringed == stringed[::-1]

case_cnt = 0
for case_line in data:
    case_cnt += 1
    case = case_line.split()
    count = 0
    for i in range(int(case[0]), int(case[1]) + 1):
        if is_palindrome(i):
            sqrt = math.sqrt(i)
            if sqrt.is_integer() and is_palindrome(int(sqrt)):
                seen.add(i)
                count += 1
    output.write("Case #%i: %i\n" % (case_cnt, count))