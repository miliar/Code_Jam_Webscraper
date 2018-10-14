def _istidy(n):
    prev = 0
    for i in range(len(n)):
        cur = int(n[i])
        if int(n[i]) < prev:
            return False

        prev = cur
    return True

def istidy(n):
    prev = 9
    order = 1
    # print('----- {} ------'.format(n))
    while(True):
        cur = int((n % (10 * order))/order)
        # print('cur: {}, prev: {}'.format(cur, prev))
        if cur == 0 and int(n/order) == 0:
            return True
        elif cur > prev:
            return False
        else:
            order = order * 10
            prev = cur

def search(num):
    for i in range(num):
        if istidy(num-i):
           return num-i 


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    num = int(input())
    ans = search(num)

    print("Case #{}: {}".format(i, ans))
