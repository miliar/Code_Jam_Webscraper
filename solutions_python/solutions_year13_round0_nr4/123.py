#!/usr/bin/env python3
import argparse
import itertools
from collections import deque

parser = argparse.ArgumentParser(description="google code jam practice all your base")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open(args.inputfile + ".out", "w")

def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        K, N = (int(i) for i in f.readline().strip().split(" "))
        keys = [int(i) for i in f.readline().strip().split(" ")]
        keys_in_chest = {}
        chests = {}
        for i in range(N):
            l = f.readline().strip().split(" ")
            T_i = l[0]
            chests[i] = int(T_i)
            K_i = l[1]
            keys_in_chest[i] = [int(i) for i in l[2:]]


        yield K,N,keys,chests,keys_in_chest


def output(n, s):
    outstring = "Case #{}: {}\n".format(n+1, s)
    print(outstring, end="")
    outfile.write(outstring)


# def open_chest(i, keys,chests, keys_in_chest):
#     key_type = chests[i]
#     keys.remove(key_type)
#     keys.extend(keys_in_chest[i])
#     del chests[i]
#     del keys_in_chest[i]

def open_chest(i, keys,chests, keys_in_chest):
    # print_state(keys,chests, keys_in_chest)
    try:
        newkeys = list(keys)
        newchests = chests.copy()
        newkeys_in_chest = keys_in_chest.copy()
        key_type = chests[i]
        newkeys.remove(key_type)
        newkeys.extend(keys_in_chest[i])
        del newchests[i]
        del newkeys_in_chest[i]
        return newkeys, newchests, newkeys_in_chest
    except KeyError:
        print("tried to open", i)
        print_state(keys,chests, keys_in_chest)
        exit()

def print_state(keys,chests, keys_in_chest):
    print("My keys", keys)
    print("Chests", chests)
    print("keys in them", keys_in_chest)

def test_trial(trial, keys, chests, keys_in_chest):
    # print("Doing trial", trial)
    try:
        for i in trial:
            # print_state(keys, chests, keys_in_chest)
            keys, chests, keys_in_chest = open_chest(i, keys, chests, keys_in_chest)
    except ValueError as e:
        # print("Did not have correct key")
        return False
    else:
        # print("Trial is good!", trial)
        return True

def safe_to_open(i, keys, chests, keys_in_chest):
    print("Is it safe to open", i)
    newkeys, newchests, newkeys_in_chest = open_chest(i,keys, chests, keys_in_chest)
    possible = is_possible(newkeys, newchests, newkeys_in_chest)
    print_state(newkeys, newchests, newkeys_in_chest)
    print(possible)
    # input("possibility checked")
    return possible

def get_next(keys, chests, keys_in_chest):
    possible = []
    for i, t in chests.items():
        if t in keys:
            if keys.count(t) == 1 and (list(chests.values()).count(t) > 1 and all(t not in c for c in keys_in_chest.values())):
                continue
#            if keys.count(t) == 1 and (list(chests.values()).count(t) > 1 and t not in keys_in_chest[i]):
                # print( "skipping")
            if keys.count(t) == 1 and list(chests.values()).count(t) > 1:
                if(not safe_to_open(i, keys, chests, keys_in_chest)):
                    continue
            possible.append(i)
    return sorted(possible, reverse=True)

def is_possible(keys, chests, keys_in_chest):
    for keytype in range(1,200):
        total_keys = keys.count(keytype) + sum([x.count(keytype) for x in keys_in_chest.values()])

        if list(chests.values()).count(keytype) > total_keys:
            print("keytype {}, total_keys {}, chests {}".format(keytype, total_keys, list(chests.values()).count(keytype)))
            return False
        if(keys.count(keytype) == 0):
            chest_indexes_requiring_keytype = frozenset([i for i,v in chests.items() if v == keytype])
            chest_indexes_containing_keytype = frozenset([i for i,v in keys_in_chest.items() if keytype in v])
            if chest_indexes_containing_keytype and chest_indexes_containing_keytype <= chest_indexes_requiring_keytype:
                print("chest_indexes_containing_keytype <= chest_indexes_requiring_keytype", chest_indexes_containing_keytype , chest_indexes_requiring_keytype)
                return False
    return True

solutions = []

def next_step(keys, chests, keys_in_chest, steps_done, foo):
    # print("steps done. steps to go", steps_done, len(chests), foo)
    # print_state(newkeys, newchests, newkeys_in_chest)
    # print(list(get_next(newkeys, newchests, newkeys_in_chest)))
    found = False
    if len(chests) == 0:
        # print("\n\nFound solution!!!!\n\n", steps_done)
        return steps_done
    for i in get_next(keys, chests, keys_in_chest):
        newkeys, newchests, newkeys_in_chest = list(keys), chests.copy(), keys_in_chest.copy()
        # print("get next gave", i)
        try:
            newkeys, newchests, newkeys_in_chest = open_chest(i, newkeys, newchests, newkeys_in_chest)
        except ValueError:
            # print("error, continuing")
            continue
        rvalue = next_step(newkeys, newchests, newkeys_in_chest, steps_done + [i], foo+1)
        if rvalue:
            solutions.append(rvalue)
            found = True
    if found:
        return True

    # print("end", steps_done)

def breadth_first_search(keys, chests, keys_in_chest):
    newkeys, newchests, newkeys_in_chest = list(keys), chests.copy(), keys_in_chest.copy()
    q = deque()
    parent = {}
    opened_so_far = ()
    for i in get_next(keys, chests, keys_in_chest):
        q.append((i,opened_so_far))
    print("init q",q)
    state = {}
    state[opened_so_far] = newkeys, newchests, newkeys_in_chest
    first = -1
    while q:
        # print("State", state)
        to_be_opened, opened_so_far = q.pop()
        if opened_so_far == ():
            first = to_be_opened
        print("opening", to_be_opened, "opened_so_far", opened_so_far)
        if(opened_so_far in state.keys()):
            tmpkeys, tmpchests, tmpkeys_in_chest = state[opened_so_far]
            # print_state(tmpkeys, tmpchests, tmpkeys_in_chest)
            newkeys, newchests, newkeys_in_chest = list(tmpkeys), tmpchests.copy(), tmpkeys_in_chest.copy()
        # print_state(newkeys, newchests, newkeys_in_chest)
        newkeys, newchests, newkeys_in_chest = open_chest(to_be_opened, newkeys, newchests, newkeys_in_chest)
        opened_so_far += (to_be_opened,)
        print("opened so far", opened_so_far)
        state[opened_so_far] = list(newkeys), newchests.copy(), newkeys_in_chest.copy()
         # input("Press ENTER to exit")
        if len(newchests) == 0:
            print("done!!")
            print(to_be_opened)
            print (opened_so_far)
            # return backtrace(parent,first,to_be_opened)
            return opened_so_far
        for n in get_next(newkeys, newchests, newkeys_in_chest):
            parent[n] = to_be_opened
            q.append((n,opened_so_far))

def trace_path(parent, end):
    counter = 0
    path = [end]
    while counter < 10:
        path.append(parent[path[-1]])
        counter += 1
        print(path)
    print(path)

def backtrace(parent, start, end):
    print(parent)
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def main():
    for n,case in enumerate(read_input()):
        outstring = "IMPOSSIBLE"
        _, _, keys, chests, keys_in_chest = case
        result = None
        if is_possible(keys, chests, keys_in_chest):
            result = breadth_first_search(keys, chests, keys_in_chest)
            print(result)
            if(result):
                outstring = outstring = " ".join(str(t+1) for t in result)
        else:
            print("is impossible")
            outstring = "IMPOSSIBLE"
        # mytrial = (i for i in (0, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
        # print(test_trial(mytrial, keys, chests, keys_in_chest) )
        # print(list(reversed(backtrace(r,1,2))))
        # print(list(backtrace(r,1,0)))
        # trace_path(r,0)
        # exit(1)

        # mytrial = (i-1 for i in (1,3,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
        # print(test_trial(mytrial, keys, chests, keys_in_chest) )
        # if is_possible(keys, chests, keys_in_chest):
        #     # print("possible, trying")
        #     result = next_step(keys, chests, keys_in_chest, [], 0)

        #     if result:
        #         print(solutions)
        #         # assert(test_trial(result, keys, chests, keys_in_chest) )
        #         # outstring = " ".join(str(t+1) for t in result)
        # else:
        #     print("is impossible")
        #     outstring = "IMPOSSIBLE"

        output(n,outstring)

if __name__ == "__main__":
    main()
