
t = int(input())

def is_tidy(num):
    last = 9

    nums = [int(x) for x in str(num)]
    nums.reverse()

    for t in nums:
        if t > last:
            return False
        else:
            last = t

    return True

def make_tidyier(num):
    
    return num - 1



for i in range(1, t + 1):
    n = int(input())

    while not is_tidy(n):
        n = make_tidyier(n)

    print("Case #{}: {}".format(i, n))

