"""
shyness = [n, m, k, ...]

1) sort in ascending order of shyness
2) find first person who won't stand and add enough people to make him/her stand
   and iterate
   - accumulate number of standing people as you pass down the sorted list

"""


def solve(shyness_counts):
    "return number of friends added"
    n_standing = 0
    n_friends_added = 0

    for shyness,count in enumerate(shyness_counts):
        if count != 0:
            if shyness <= n_standing:
                # then those people stand
                n_standing += count
            else:
                # then we add the minimal number of friends to get them standing
                n_more_friends_to_add = (shyness - n_standing)
                n_friends_added += n_more_friends_to_add
                n_standing += (n_more_friends_to_add + count)

    return n_friends_added


def std_in():
    while True:
        yield raw_input()


def main():
    STD_IN = std_in()

    T = int(next(STD_IN).strip())

    for t in xrange(T):
        s_max, shyness_counts = next(STD_IN).strip().split()
        solution = solve(map(int, shyness_counts))
        print 'Case #{}: {}'.format(t+1, solution)


if __name__ == '__main__':
    main()
