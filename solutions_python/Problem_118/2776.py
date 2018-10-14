import math

file = open("C-small-attempt5.in", 'r') #Open the local file input
case = 0
case = file.readline()
lines = []

def palindrome(x):
    mainInt = str(x)
    inversed = str(x)[::-1]
    if int(mainInt) == int(inversed):
        return True
    return False


count = 1
for cases in range(int(case)):
    A = 0
    B = 0
    check = 0
    howMany = 0
    for x in file.readline().split():
        if check == 0: A = int(x)
        if check == 1: B = int(x)
        check += 1
    for y in range(A, B+1):
        if palindrome(y) and math.sqrt(y).is_integer() and palindrome(int(math.sqrt(y))):
            howMany += 1
    lines.append('Case #%s: %s' % (count, howMany))
    count += 1
    howMany = 0

lines = '\n'.join(lines)
print lines

out = open('output.txt', 'w')
out.write(lines)
out.close()

file.close()