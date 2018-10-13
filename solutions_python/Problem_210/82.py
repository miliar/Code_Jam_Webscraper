import sys

def bprint(*things):
    return  # Disable `bprint` function
    for thing in things:
        print >> sys.stderr, thing,
    print >> sys.stderr, ""


def read_input():
    acts = []
    minutes = {'j': 720, 'c': 720}

    C_N, J_N = map(int, raw_input().split())

    for _ in xrange(C_N):
        s, e = map(int, raw_input().split())
        acts.append((s, e, 'j'))  # J takes care of the baby
        minutes['j'] -= (e - s)

    for _ in xrange(J_N):
        s, e = map(int, raw_input().split())
        acts.append((s, e, 'c'))  # C takes care of the baby
        minutes['c'] -= (e - s)

    return acts, minutes

def get_int_of_str(obj):
    if isinstance(obj, int):
        bprint("!ERROR!!", obj)
        return obj
    if isinstance(obj, tuple):
        if not isinstance(obj[0], int):
            bprint("!!ERROR!!", obj)
        return obj[0]
    if isinstance(obj, str):
        return 5000  # max int in this problem
    bprint("ERROR!!", obj)
    return obj

SH = "shift"
MG = "merged"
IN = "inter-shift"

def calculate(input_args):
    acts, minutes = input_args
    acts.sort()
    bprint("\n>>", acts)
    len_acts = len(acts)
    if len_acts == 1:
        return 2  # one activity, shift twice

    ### Calculate buffers
    buffers = []
    # 0 ~ -1
    for idx in xrange(len_acts - 1):
        _, e, p1 = acts[idx]
        s, _, p2 = acts[idx + 1]
        if p1 != p2:
            buffers.append(SH)
        else:
            if s == e:
                buffers.append(MG)
                #buffers.append((MG, p1))
            else:
                buffers.append((s - e, p1))
    # -1, 0
    _, e, p1 = acts[-1]
    s, _, p2 = acts[0]
    if p1 != p2:
        buffers.append(SH)
    else:
        if (s == e) or (e == 1440 and s == 0):
            buffers.append(MG)
            #buffers.append((MG, p1))
        else:
            buffers.append((s + (1440 - e), p1))

    bprint(buffers)

    ### Merge
    while True:
        #if (minutes['c'] == 0) or (minutes['j'] == 0):
        #    break
        to_merge_idx, to_merge_tuple = min(enumerate(buffers), key=lambda x:get_int_of_str(x[1]))
        if isinstance(to_merge_tuple, str):
            bprint("<<", buffers)
            break
        time, person = to_merge_tuple
        bprint("||", time, person, minutes[person])
        if minutes[person] <= time:
            if minutes[person] == time:
                buffers[to_merge_idx] = MG
            # not enough time to merge, but still exists `person`'s tuple
            minutes[person] = 0
            for idx in xrange(len(buffers)):
                if buffers[idx][1] != person:
                    continue
                buffers[idx] = IN
        else:
            minutes[person] -= time
            buffers[to_merge_idx] = MG

    ### Calculate shifts
    ans = 0
    for bf in buffers:
        if bf == MG:
            continue
        elif bf == SH:
            ans += 1
        elif bf == IN:
            ans += 2
        else:
            bprint("NO!!!!!", bf)
    bprint(ans)
    return ans

def to_formated_string(result_tokens):
    if (result_tokens == 0) or (result_tokens % 2 != 0):
        bprint("error!", result_tokens)
    return result_tokens

if __name__ == '__main__':
    T = int(raw_input())
    case = 1
    while case <= T:
        input_args = read_input()
        result = calculate(input_args)
        answer = to_formated_string(result)
        print 'Case #%d:' % case, answer
        case += 1

