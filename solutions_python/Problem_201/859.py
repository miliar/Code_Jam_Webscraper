import collections

def solve(n, k):
    if n == k: return (0, 0)
    i = 0
    dic = collections.defaultdict(int)
    interval = [n]
    dic[n] = 1
    while interval:
        inte = interval.pop(0)
        if inte%2 == 0:
            minimum = inte//2 - 1
            maximum = inte//2
            dic[minimum] += dic[inte]
            dic[maximum] += dic[inte]
            if maximum not in interval:
                interval.append(maximum)
            if minimum not in interval:
                interval.append(minimum)
        else:
            minimum = maximum = (inte-1)//2
            dic[minimum] += dic[inte] * 2
            if minimum not in interval:
                interval.append(minimum)
        if i + dic[inte] >= k:
            return (maximum, minimum)
        else:
            i += dic[inte]

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        minimum, maximum = solve(n, k)
        print("Case #{}: {} {}".format(i, minimum, maximum))