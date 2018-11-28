from collections import defaultdict

def gen_tidy():
    lens = defaultdict(list)
    lens[1] = list('123456789')
    for i in range(1, 18):
        prev = lens[i]
        for s in prev:
            last = int(s[-1])
            for u in range(last, 10):
                lens[i+1].append(s + str(u))
    nums = []
    for d in lens:
        for x in lens[d]:
            nums.append(int(x))
    return list(sorted(nums))

def is_tidy(n):
    num = str(n)
    return ''.join(sorted(num)) == num

def solve_brute(num):
    for i in reversed(range(1, num + 1)):
        if is_tidy(i): 
            return i

def solve(num, all_tidy):
    for i in reversed(all_tidy):
        if i <= num:
            return i

all_tidy = gen_tidy()

t = input()
for i in range(1, t+1):
    num = int(raw_input().strip())
#    print 'Case #{}: {}'.format(i, solve_brute(num))
    print 'Case #{}: {}'.format(i, solve(num, all_tidy))
