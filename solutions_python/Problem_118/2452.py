import math

def is_fair(x):
    return str(x) == str(x)[::-1]

def is_square(x):
    x = math.sqrt(x)
    if x != int(x): return False
    if not is_fair(int(x)):
        return False
    return True

def main():
    num_of_tests = int(raw_input())
    for test_i in range(num_of_tests):
        a, b = map(int, raw_input().split(' '))
        ans = 0
        for i in range(a, b + 1):
            if is_fair(i) and is_square(i):
               ans += 1
        print "Case #%d: %s" % (test_i + 1, ans)

if __name__ == "__main__":
    main()