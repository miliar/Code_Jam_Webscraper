import sys

def solve(initial, contents):
    chests = {}
    for i in range(len(contents)):
        chests[i + 1] = (contents[i][0], contents[i][1])
    keys = {}
    for key in initial:
        if key in keys:
            keys[key] += 1
        else:
            keys[key] = 1
    answer = explore(chests, keys, [], set())
    if answer:
        s = ''
        for i in answer:
            s += str(i) + ' '
        return s[:-1]
    else:
        return 'IMPOSSIBLE'

def explore(chests, keys, path, dead):
    dk = (tuple(sorted([x[0] for x in chests.values()])), tuple(sorted(keys.items())))
    if dk in dead:
        return None
    if not chests:
        return path
    elif not keys:
        dead.add(dk)
        return None
    else:
        for (chest, (lock, contents)) in sorted(chests.items()):
            if lock in keys:
                new_keys = dict(keys)
                for key in contents:
                    if key in new_keys:
                        new_keys[key] += 1
                    else:
                        new_keys[key] = 1
                new_keys[lock] -= 1
                if new_keys[lock] == 0:
                    del new_keys[lock]
                new_chests = dict(chests)
                del new_chests[chest]
                path.append(chest)
                answer = explore(new_chests, new_keys, path, dead)
                if answer:
                    return answer
                else:
                    path.pop()
    dead.add(dk)
    return None

n = input()

for i in range(n):
    [k, chest_count] = [int(x) for x in raw_input().split()]
    initial = [int(x) for x in raw_input().split()]

    chests = []
    all_keys = set()
    for j in range(chest_count):
        split = [int(x) for x in raw_input().split()]
        lock = split[0]
        num_keys = split[1]
        contents = split[2:]
        chests.append((lock, contents))
    print('Case #{}: {}'.format(i + 1, solve(initial, chests)))
