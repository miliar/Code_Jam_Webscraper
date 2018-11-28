import os
from copy import copy
from collections import Counter, defaultdict

PROB_NAME = 'treasure'
INPUT_TYPE = 'small2'


class Chest(object):
    def __init__(self, index, lock, keys):
        self.index = index
        self.keys = keys
        self.lock = lock
        self.open = False


def open_chest(keys, chest):
    keys.subtract(Counter({chest.lock: 1}))
    keys.update(chest.keys)


def move(keys, chests, result):
    for key in keys:
        compatible_chests = [chest for chest in chests
                             if chest.lock == key]
        if keys[key] >= len(compatible_chests):
            for chest in compatible_chests:
                if chest.index in result:
                    continue
                result.append(chest.index)
                open_chest(keys, chest)
                return True

    for key in keys:
        for chest in chests:
            if chest.index in result:
                continue
            if key == chest.lock and key in chest.keys:
                result.append(chest.index)
                open_chest(keys, chest)
                return True

    for chest in chests:
        if chest.index in result:
            continue
        if chest.lock in keys:
            result.append(chest.index)
            open_chest(keys, chest)
            return True

    return False


def solve(case):
    """break 'case', solve and return the solution"""
    keys, chests = case
    print_prob(keys, chests)
    total_locks = Counter(chest.lock for chest in chests)
    total_keys = Counter()
    total_keys.update(keys)
    for chest in chests:
        total_keys.update(chest.keys)
    for key in total_locks:
        if total_keys[key] < total_locks[key]:
            return 'IMPOSSIBLE'

    result = solve2(keys, chests)
    if result is None:
        print 'IMPOSSIBLE'
        return 'IMPOSSIBLE'
    print ' '.join(str(index) for index in result)
    return ' '.join(str(index) for index in result)
    # result = []
    # while move(keys, chests, result):
        # pass

    # if len(result) == len(chests):
        # return ' '.join(str(index) for index in result)


def print_prob(keys, chests):
    print 'keys: ', keys
    for chest in chests:
        print 'Chest #{0.index}: open={0.open}, lock={0.lock}, '\
              'keys={0.keys}'.format(chest)


def solve2(keys, chests):
    def unlockable(chest):
        return chest.lock in keys and keys[chest.lock] > 0

    locked = [chest for chest in chests if chest.open is False]
    if not locked:
        return []


    for chest in locked:
        if unlockable(chest):
            new_keys, new_chests = copy(keys), copy(chests)
            new_keys.subtract(Counter({chest.lock: 1}))
            new_keys.update(chest.keys)
            chest.open = True
            result = solve2(new_keys, new_chests)
            if result is not None:
                return [chest.index] + result
            chest.open = False
            if chest.lock in chest.keys:
                return None
            locked_by = [chest2 for chest2 in locked if
                         chest2.lock == chest.lock and chest2 is not chest]
            if len(locked_by) == 0 or len(locked_by) < keys[chest.lock]:
                return None

    return None


def read_file(filepath):
    """Read the input file and return a list of cases in a tuple format."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for case in range(num_cases):
            # read each case here
            k, n = [int(num) for num in lines.pop(0).split()]
            keys = Counter(int(num) for num in lines.pop(0).split())
            chests = []
            for i in range(n):
                nums = [int(num) for num in lines.pop(0).split()]
                lock = nums[0]
                chest_keys = Counter(nums[2:])
                chests.append(Chest(i + 1, lock, chest_keys))
            cases.append((keys, chests))
    return cases


def write_results(results, outfile):
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


def main(infile, outfile):
    cases = read_file(infile)
    results = [solve(case) for case in cases]
    write_results(results, outfile)

main(os.path.join('io', '{}_{}.in'.format(PROB_NAME, INPUT_TYPE)),
     os.path.join('io', '{}_{}.out'.format(PROB_NAME, INPUT_TYPE)))
