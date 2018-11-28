import sys, math

def is_palindrome(s):  
    return s == s[::-1]

def get_fair_and_sq(start, end):
    count = 0
    for i in range(start, end + 1):
        if not is_palindrome(str(i)):
            continue
        square = math.sqrt(i)
        if 0.99999 > square % 1 > .000001:
            continue

        if is_palindrome(str(int(round(square)))):
            count += 1
        
    return count

if __name__ == '__main__':
    f = open(sys.argv[1])

    for i in range(int(f.readline())):
        line = f.readline().split()
        print('Case #' + str(i + 1) + ': ' + str(get_fair_and_sq(int(line[0]), int(line[1]))))
