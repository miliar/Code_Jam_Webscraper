t = int(input())


def problem(i):
    sample = input()
    while not is_tidy(sample):
        index = get_untidy_index(sample)
        sample = fix_at_index(sample, index)
    return int(sample)


def fix_at_index(inp, index):
    return inp[0:index] + str(int(inp[index])-1) + '9' * len(inp[index+1:])


def get_untidy_index(inp):
    ind = 0
    prev = inp[0]
    for x in inp:
        if x < prev:
            return ind - 1
        prev = x
        ind += 1


def is_tidy(inp):
    prev = inp[0]
    for x in inp:
        if x < prev:
            return False
        prev = x
    return True


for i in range(1, t + 1):
    print("Case #{}: {}".format(i, problem(i)))
