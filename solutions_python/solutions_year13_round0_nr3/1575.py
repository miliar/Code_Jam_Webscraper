import math

def get_fair_and_square(max_number):
    i = 1
    result = []
    while(i < math.sqrt(max_number)):
        if is_fair(i):
            if is_fair(i*i):
                result.append(i*i)
        i = i + 1
    return result

def is_fair(number):
    return number == int(str(number)[::-1])

if __name__ == '__main__':
    square_and_fair = get_fair_and_square(10**14)
    f = open("C-large-1.in", "r")
    cases = f.readline().strip()
    for i in range(int(cases)):
        [a, b] = f.readline().split()
        res = len([x for x in square_and_fair if x >= int(a) and x <= int(b)])
        print("Case #%d: %d" % (i + 1, res))
