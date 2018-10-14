__author__ = 'jakub.bibro'


def solve(platess):
    # print platess
    biggest = max(platess)
    if biggest <= 3:
        return biggest

    biggest_pos = platess.index(biggest)
    new_lst = [pp for pp in platess]
    new_lst2 = [pp for pp in platess]
    new_lst[biggest_pos] = biggest/2
    new_lst2[biggest_pos] = biggest/3
    return 1 + min(solve([p - 1 if p > 1 else 0 for p in platess]), solve(new_lst + [biggest - (biggest/2)]), solve(new_lst2 + [biggest - (biggest/3)]))


if __name__ == '__main__':
    test_cases = int(raw_input().strip())
    for i in range(0, test_cases):
        num_of_diners = int(raw_input().strip())
        plates = raw_input().strip().split(' ')
        plates = [int(p) for p in plates]
        # print plates
        solution = solve(plates)
        print('Case #{}: {}'.format(i + 1, solution))