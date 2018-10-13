from collections import deque

MAX = 99999


def get_number_of_flips(s, k):
    a = [c == "+" for c in s]

    visited = set([])
    queue = deque([(a, 0)])
    min_count = MAX
    while queue:
        cur_a, count = queue.popleft()

        # optimization: if all 0 and divisible by k
        if not any(cur_a) and len(cur_a) % k == 0:
            cur_count = count + len(cur_a) // k
            if cur_count < min_count:
                min_count = cur_count
            continue

        # if solved, check the min count and don't continue
        if all(cur_a):
            if count < min_count:
                min_count = count
            continue

        visited.add(str(cur_a))
        for index in range(len(cur_a) - k + 1):
            sub_a = cur_a[index: index + k]
            if all(sub_a):  # don't flip if all +
                continue

            # flip
            flipped_a = cur_a[:index] + [not item for item in sub_a] + cur_a[index + k:]
            if str(flipped_a) in visited:
                continue

            queue.append((flipped_a, count + 1))

    return min_count if min_count != MAX else "IMPOSSIBLE"


# std in
for index in range(1, int(input()) + 1):
    s, k = input().split(" ")
    print("Case #%s: %s" % (index, get_number_of_flips(s, int(k))))
