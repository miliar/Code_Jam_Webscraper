def cc(d, n, input_horses):
    horse_functions = {}
    for (k, s) in input_horses:
        horse_functions[k] = make_horse_f(d, k, s)
    horse_starting_points = horse_functions.keys()
    horse_starting_points.sort(reverse=True)
    for start_index in range(len(horse_starting_points) - 1):
        top_horse = horse_functions[horse_starting_points[start_index]]
        bot_horse = horse_functions[horse_starting_points[start_index + 1]]
        (new_top_horse, new_bot_horse) = intersect_horses(top_horse, bot_horse)
        horse_functions[horse_starting_points[start_index + 1]] = new_bot_horse
    last_horse_arriving_t = get_arriving_time(horse_functions[horse_starting_points[-1]], d)
    return float(d) / last_horse_arriving_t


# Single function is dist = K + S * t
# Single function is stored as a tuple (K, S)
# Full horse function is dict with starting times as keys and the corresponding functions as values
def make_horse_f(d, k, s):
    horse_func = {0: (k, s)}
    cte_func = make_cte_f(d)
    (horse_func, _) = intersect_horses(horse_func, cte_func)
    return horse_func


def make_cte_f(d):
    return {0: (d, 0)}


# Intersects the two horse functions & returns the newly altered ones
def intersect_horses(h1, h2):
    keys1 = h1.keys()
    keys2 = h2.keys()
    keys_comb = keys1 + list(set(keys2) - set(keys1))
    keys_comb.sort()
    for keys_index in range(len(keys_comb)):
        key = keys_comb[keys_index]
        next_key = keys_comb[keys_index + 1] if keys_index != len(keys_comb) - 1 else float("inf")
        (k1, s1) = get_closest_func(h1, key)
        (k2, s2) = get_closest_func(h2, key)
        intersect_t = intersect_func(k1, s1, k2, s2)
        if 0 < intersect_t <= next_key:
            h1_pos_prev = get_pos(h1, intersect_t - 1)
            h2_pos_prev = get_pos(h2, intersect_t - 1)
            orig_order = h1_pos_prev >= h2_pos_prev
            htop = h1 if orig_order else h2
            hbot = h2 if orig_order else h1
            hbot = update_horse_func(htop, hbot, intersect_t)
            if orig_order:
                return htop, hbot
            else:
                return hbot, htop
    return h1, h2


def get_closest_func(horse_func, t):
    horse_keys = horse_func.keys()
    horse_keys.sort()
    for key_index in range(len(horse_keys)):
        cur_key = horse_keys[key_index]
        next_key = horse_keys[key_index + 1] if key_index != len(horse_keys) - 1 else float("inf")
        if cur_key <= t <= next_key:
            return horse_func[cur_key]


# Intersects two single functions
# Returns -1 if they do not intersect, returns the intersection point t otherwise
def intersect_func(k1, s1, k2, s2):
    delta_s = s2 - s1
    if delta_s == 0:
        return -1
    res_t = float(k1 - k2) / delta_s
    if res_t < 0:
        return -1
    return res_t


# Updates the bottom horse function, by making it follow the top one, starting from the intersection
def update_horse_func(htop, hbot, intersect_t):
    for key in hbot.keys():
        if key >= intersect_t:
            hbot.pop(key, None)
    top_keys = htop.keys()
    top_keys.sort()
    for key_index in range(len(top_keys)):
        if key_index == len(top_keys) - 1:
            hbot[intersect_t] = htop[top_keys[key_index]]
            break
        cur_key = top_keys[key_index]
        next_key = top_keys[key_index + 1]
        if cur_key < intersect_t <= next_key:
            hbot[intersect_t] = htop[top_keys[cur_key]]
            break
    for key in htop.keys():
        if key >= intersect_t:
            hbot[key] = htop[key]
    return hbot


# Gets the current position of the given horse func at the given time
def get_pos(horse_func, t):
    keys = horse_func.keys()
    keys.sort()
    for key_index in range(len(keys)):
        if key_index == len(keys) - 1:
            return get_pos_i(horse_func[keys[key_index]], t)
        if keys[key_index] < t <= keys[key_index + 1]:
            return get_pos_i(horse_func[keys[key_index]], t)


def get_pos_i((k, s), t):
    return k + s * t


def get_arriving_time(horse_func, d):
    keys = horse_func.keys()
    keys.sort()
    last_func = horse_func[keys[-2]]
    (k, s) = last_func
    return float(d - k) / s


input_t = int(raw_input())
for i in xrange(1, input_t + 1):
    input_d, input_n = [int(st1) for st1 in raw_input().split(" ")]
    input_hs = []
    for j in xrange(1, input_n + 1):
        input_k, input_s = [int(st2) for st2 in raw_input().split(" ")]
        input_hs.append((input_k, input_s))
    result = cc(input_d, input_n, input_hs)
    print "Case #{}: {}".format(i, result)
