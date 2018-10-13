
def solve(d, k, s):
    longest_time_seen_so_far = 0

    for i in range(len(k)):
        t = (d-k[i])/float(s[i])
        longest_time_seen_so_far = max(longest_time_seen_so_far, t)

    return d/float(longest_time_seen_so_far)

if __name__ == "__main__":
    # with open('A-small-attempt0.in') as f:
    #     input = f.read().splitlines()

    # t = int(input[0])
    t = int(input())

    # output = ''

    for case_no in range(t):
        d, n = [int(a) for a in input().split(' ')]
        # print(d)
        # print(n)
        k, s = [], []
        for horse_no in range(n):
            new_k, new_s = [int(a) for a in input().split(' ')]
            k.append(new_k)
            s.append(new_s)

        # print('\n')
        # print(d)
        # print(n)
        # print(str(k))
        # print(str(s))
        print("Case #{}: {}".format(case_no + 1, solve(d, k, s)))
        # output += "Case #{}: {}\n".format(case_no + 1, solve(pancakes, k, cycles))

    # with open('solution_cycles.out', 'w') as f:
    #     f.write(output)