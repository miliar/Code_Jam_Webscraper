
import math

def solve(a, b):

    result = 0
    d = int(math.sqrt(b))

    while True:
        while not palindrome(d):
            d -= 1
        
        if d*d < a:
            break
        elif palindrome(d*d):
            result += 1

        d -= 1

    return result

def palindrome(n):

    if n < 10:
        return True
    else:
        digits = list(str(n))
        result = True
        for i in range(0, int(len(digits)/2)):
            if digits[i] != digits[len(digits) - i - 1]:
                result = False
                break
        return result

# def main():
#     print solve(1, 4)
#     print solve(10, 120)
#     print solve(100, 1000)

def main():
    f = open('input.txt', 'r')
    read_data = f.read()

    process(read_data)


def process(data):

    rows = data.split('\n')
    i = 0

    for row in rows:
        if row == '':
            continue

        if i > 0:
            row_parts = row.split(' ')
            a = float(row_parts[0])
            b = float(row_parts[1])
            print 'Case #' + str(i) + ': ' + str(solve(a, b))

        i += 1    

main()