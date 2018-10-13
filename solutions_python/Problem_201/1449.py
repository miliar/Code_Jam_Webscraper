import math

nums = []

with open('C-small-2-attempt0.in', 'r') as f:
    T = int(f.readline())
    for i in range(T):
        nums.append(f.readline().strip().split(' '))

case = 1


with open('output.out', 'w') as f:
    case = 1
    for Nstr, Kstr in nums:
        N = int(Nstr)
        K = int(Kstr)

        sizes = {N: 1}
        power = 1
        while K - power > 0:
            K -= power
            power *= 2
            new_sizes = {}
            for s, times in sizes.items():
                s-=1
                if int(math.ceil(s/2)) not in new_sizes:
                    new_sizes[int(math.ceil(s/2))] = 0
                new_sizes[int(math.ceil(s / 2))] += times
                if int(math.floor(s/2)) not in new_sizes:
                    new_sizes[int(math.floor(s/2))] = 0
                new_sizes[int(math.floor(s / 2))] += times
            sizes = new_sizes

        final_sizes = list(sizes.items())
        final_sizes.sort(reverse=True)
        print(final_sizes)
        print(K)

        for obj in final_sizes:
            size, count = obj
            if count >= K:
                f.write("Case #%d: %d %d\n" % (case, int(math.ceil((size - 1)/2)), int(math.floor((size - 1)/2))))
                break
            K -= count


        case += 1