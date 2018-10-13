import math

def split_digits(n):
    digits = []
    while n>0:
        digits.append(n % 10)
        n = math.floor(n/10)
    return digits

def is_palindrome(n):
    digit_array = split_digits(n)
    for i in range(int(len(digit_array) / 2)):
        if digit_array[i] != digit_array[len(digit_array) - 1 - i]:
            return False
    return True


f = open('C-small-attempt0.in', 'r')

set_count = int(f.readline())
results = []
for i in range(set_count):
    words = f.readline().split(' ')
    elements = [[0] for x in range(len(words))]
    for j in range(len(words)):
        elements[j] = int(words[j])
    print(elements)
    
    count = 0
    for k in range(math.ceil(math.sqrt(elements[0])), math.floor(math.sqrt(elements[1])) + 1):
        if k*k < elements[0] or k*k > elements[1]:
            break
        if is_palindrome(k) and is_palindrome(k*k):
#             print(k)
            count += 1
    results.append("Case #" + str(i+1) + ": " + str(count))
    
f = open('C-small-attempt0.out', 'w')            

for line in results:
    f.write(line + '\n')
print(set_count)