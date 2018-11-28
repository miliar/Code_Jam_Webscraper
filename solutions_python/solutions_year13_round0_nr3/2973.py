import math

# dictionary maps fair and square number to its fair and square square-root.
cache = {}

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_sq(num):
    return num == int(math.sqrt(num)) ** 2 

def fair_square(num):
    if is_palindrome(num) and is_sq(num):
        return is_palindrome(int(math.sqrt(num)))
    return False

def fair_square_interval(a, b):
    count = 0
    for num in range(a, b + 1):
        if num in cache:
            count += 1
        elif fair_square(num):
            cache[num] = int(math.sqrt(num))
            count += 1
    #print cache
    return count

if __name__ == '__main__':
    case = 0
    with open('C-small-attempt0.in') as f:
        next(f)
        for line in f:
            case += 1
            a, b = line.split()
            a, b = int(a), int(b)
            count = fair_square_interval(a, b)
            with open('output.txt', 'a') as g:
                g.write('Case #{}: {}\n'.format(case, count))
