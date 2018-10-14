from math import ceil, floor, sqrt

def is_palindrome(x):
    num = str(x)
    l = len(num)
    if l == 1:
        return True
    i = 0
    limit = l/2
    while i < limit:
        if num[i] != num[-(i+1)]:
            return False
        i += 1
    return True

def fair_and_square_cases(x, y):
    cases = 0
    limit_below = int(ceil(sqrt(x)))
    limit_above = int(floor(sqrt(y)))
    i = limit_below

    while i <= limit_above:
        if is_palindrome(i) and is_palindrome(i**2):
            cases += 1
        i += 1

    print limit_below, limit_above
    return cases

def main():
#    print is_palindrome(1335331)
#    print is_palindrome(335331)
#    print is_palindrome(3333)
#    print is_palindrome(3)
#    print is_palindrome(13)
#    print is_palindrome(1331)
#    print fair_and_square_cases(1, 4)
#    print fair_and_square_cases(10, 120)
#    print fair_and_square_cases(100, 1000)
    
    with open("input.txt", "r") as f:
        with open("output.txt", "w") as output:
            lines = f.readline()
            i = 1
            for l in f:
                x, y = l.split()
                cases = fair_and_square_cases(int(x), int(y))
                output.write("Case #" + str(i) + ": " + str(cases) + "\n")
                i += 1

main()
