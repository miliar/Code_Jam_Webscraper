__author__ = 'deniskrut'

import sys

def buildRouteDetail(chests, route, current_keys, selfKeysCount, needed_keys, have_keys, chestWithSelfKeys):
    if len(route) == len(chests):
        return route
    for chest_num in range(0, len(chests)):
        if chest_num not in route:
            cur_chest = chests[chest_num]
            key_needed = cur_chest[0]
            if key_needed in current_keys:
                if key_needed in selfKeysCount and selfKeysCount[key_needed] > 0:
                    cur_count_self_keys = 0
                    for cur_key_2 in cur_chest[1]:
                        if cur_key_2 == key_needed:
                            cur_count_self_keys += 1
                    cur_count_self_keys_2 = 0
                    for cur_key_3 in current_keys:
                        if cur_key_3 == key_needed:
                            cur_count_self_keys_2 += 1
                    visited_selfcont = False
                    for cur_chest_2 in chestWithSelfKeys[key_needed]:
                        visited_selfcont = visited_selfcont or cur_chest_2 in route
                    if len(route) + 1 != len(chests) and have_keys[key_needed] == 2 and needed_keys[key_needed] == 2 and cur_count_self_keys == 0 and cur_count_self_keys_2 == 1 and not visited_selfcont:
                        continue
                new_route = list(route)
                new_route.append(chest_num)
                new_keys = list(current_keys)
                new_keys.remove(key_needed)
                cur_chest_keys = cur_chest[1]
                new_keys = new_keys + cur_chest_keys
                res_route = buildRouteDetail(chests, new_route, new_keys, selfKeysCount, needed_keys, have_keys, chestWithSelfKeys)
                if res_route != False:
                    return res_route
    return False

def buildKeysNeededAndHave(chests, start_keys):
    needed_keys = {}
    have_keys = {}
    for key in start_keys:
        if key in have_keys:
            have_keys[key] += 1
        else:
            have_keys[key] = 1
    for chest in chests:
        needed_key = chest[0]
        if needed_key in needed_keys:
            needed_keys[needed_key] += 1
        else:
            needed_keys[needed_key] = 1
        have_keys_cur = chest[1]
        for key in have_keys_cur:
            if key in have_keys:
                have_keys[key] += 1
            else:
                have_keys[key] = 1
    return needed_keys, have_keys

def solvable(needed_keys, have_keys):
    for key in needed_keys:
        if key not in have_keys or have_keys[key] < needed_keys[key]:
            return False
    return True

def selfContainingKeysCount(chests):
    selfKeysCount = {}
    chestWithSelfKeys = {}
    for i in range(0, len(chests)):
        chest = chests[i]
        count = 0
        key = chest[0]
        contains_keys = chest[1]
        for cur_key in contains_keys:
            if cur_key == key:
                count += 1
        if key in selfKeysCount:
            selfKeysCount[key] += count
        else:
            selfKeysCount[key] = count
        if count > 0:
            if key in chestWithSelfKeys:
                chestWithSelfKeys[key].append(i)
            else:
                chestWithSelfKeys[key] = [i]
    return selfKeysCount, chestWithSelfKeys

def buildRoute(chests, start_keys):
    str_route = "IMPOSSIBLE"
    needed_keys, have_keys = buildKeysNeededAndHave(chests, start_keys)
    if not solvable(needed_keys, have_keys):
        return str_route
    selfKeysCount, chestWithSelfKeys = selfContainingKeysCount(chests)
    route = buildRouteDetail(chests, [], start_keys, selfKeysCount, needed_keys, have_keys, chestWithSelfKeys)
    if route != False:
        str_one_based_route = [str(x + 1) for x in route]
        str_route = ' '.join(str_one_based_route)
    return str_route

t = int(sys.stdin.readline())
res = []

for i in range(0, t):
    kn = sys.stdin.readline().split()
    k = int(kn[0])
    n = int(kn[1])
    start_keys = [int(x) for x in sys.stdin.readline().split()]
    chests = []
    for j in range(0, n):
        chest_line = sys.stdin.readline().split()
        key_type = int(chest_line[0])
        num_keys = int(chest_line[1])
        keys_inside = []
        if num_keys > 0:
            keys_inside = [int(x) for x in chest_line[2:]]
        chests.append((key_type, keys_inside))
    print "Task " + str(i)
    route = buildRoute(chests, start_keys)
    res.append(route)

for i in range(0, t):
    print "Case #" + str(i + 1) + ": " + res[i]