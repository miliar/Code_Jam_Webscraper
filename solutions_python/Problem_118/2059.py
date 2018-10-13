import math

def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

def calculate(case):
    a, b = raw_input().split()
    start, end = int(a), int(b) 
    ans = 0
    for c in range(start, end+1):
        if isPalindrome(c): 
            root = int(math.sqrt(c))
            if abs(root**2 - c) < 0.0001 and isPalindrome(root):
                ans += 1
    return ans

@memo
def ReverseNumber(n):
    return int(str(n)[::-1])

@memo
def isPalindrome(n):
    return ReverseNumber(n) == n

if __name__ == '__main__':
    t = int(raw_input())
    for case in range(1, t+1):
        print("Case #{0}: {1}".format(case, calculate(case)))


