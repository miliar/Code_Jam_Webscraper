n_cases = int(input())

def my_max(sizes):
    m = -1
    arg = -1
    for i, size in enumerate(sizes):
        if m < size:
            m = size
            arg = i
    return m, arg

for i in range(1, n_cases + 1):
    n, k = [int(s) for s in input().split(' ')]
    chosen = [(n-1) // 2]
    sizes = [chosen[0], n - chosen[0] - 1]
    if k == 1:
        print('Case #{}: {} {}'.format(i, max(sizes), min(sizes)))
        continue
    for j in range(k - 2):
        m, arg_m = my_max(sizes)
        new_chosen = (m-1) // 2
        if arg_m > 0:
            real_chosen = chosen[arg_m - 1] + 1 + new_chosen
        else:
            real_chosen = new_chosen
        chosen.append(real_chosen)
        chosen = sorted(chosen)
        sizes[arg_m] = new_chosen
        sizes.insert(arg_m + 1, m - new_chosen - 1)

    m, arg_m = my_max(sizes)
    new_chosen = (m-1) // 2
    max_lr = max([new_chosen, m - new_chosen - 1])
    min_lr = min([new_chosen, m - new_chosen - 1])
    print('Case #{}: {} {}'.format(i, max_lr, min_lr))
