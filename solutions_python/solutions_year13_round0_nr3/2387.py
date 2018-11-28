from math import floor, ceil, sqrt

def is_palindrome(w):
    return w == w[::-1]

def decide(line):
    low, high = line.split()
    lower_bound = int(ceil(sqrt(int(low))))
    upper_bound = int(floor(sqrt(int(high))))+1
    result = 0
    for i in range(lower_bound, upper_bound):
        if is_palindrome(str(i)) and is_palindrome(str(i*i)):
            result += 1
    return str(result)
            
filename = 'input.in'
f = open(filename)
o = open('solution.out', 'w')

n = int(f.readline().strip())

count = 1
sols = []
for line in f.readlines():
    line = line.strip()
    sols.append("Case #" + str(count) + ": " + decide(line))
    count += 1
f.close()
o.write('\n'.join(sols))
o.close()
