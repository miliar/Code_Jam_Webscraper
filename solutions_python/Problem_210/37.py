def start(x):
    return x[0]
def stop(x):
    return x[1]

def color(x):
    return x[2]

def construct_edges(sequence):
    res = {'cj': [], 'c': [], 'j': []}

    for event_a, event_b in zip(sequence, sequence[1:]):
        if color(event_a) == color(event_b):
            res[color(event_a)].append(start(event_b) - stop(event_a))
        else:
            res['cj'].append(start(event_b) - stop(event_a))

    first, last = sequence[0], sequence[-1]
    distance_last_first = start(first) - stop(last) + 24 * 60
    if color(first) == color(last):
        res[color(first)].append(distance_last_first)
    else:
        res['cj'].append(distance_last_first)

    res['c'] = sorted(res['c'])
    res['j'] = sorted(res['j'])
    res['cj'] = sorted(res['cj'])
    return res
        
# def gen_edges_from_calendar(C_event, J_events):
#     # C_event events by C must be taken by J, J - events by J must be taken by C

#     C_event_col = [(a, b, 'j') for (a, b) in C_event]
#     J_event_col = [(a, b, 'c') for (a, b) in J_events]

#     return sorted(C_event_col + J_event_col)


def solve(edges, time_J, time_C):
    swaps = 0

    # fill edges['j'] with time_J:
    edges_J = []
    for e in edges['j']:
        if time_J > 0:
            take_this = min(time_J, e)
            time_J -= take_this
            e -= take_this
        if e > 0:
            edges_J.append(e)
    edges['j'] = edges_J


    edges_C = []
    for e in edges['c']:
        if time_C > 0:
            take_this = min(time_C, e)
            time_C -= take_this
            e -= take_this
        if e > 0:
            edges_C.append(e)
    edges['c'] = edges_C
    swaps = len(edges['cj']) + 2 * len(edges['c']) + 2 * len(edges['j'])
    return swaps

n_cases = int(input())
for test_case_no in range(1, n_cases+1):
    C, J = [int(x) for x in input().split()]
    events = []
    time_C, time_J = 0, 0
    for _ in range(C):
        sta, sto = [int(x) for x in input().split()]
        events.append((sta, sto, 'j'))
        time_J += sto - sta
    for _ in range(J):
        sta, sto = [int(x) for x in input().split()]
        events.append((sta, sto, 'c'))
        time_C += sto - sta

    time_J = 12 * 60 - time_J
    time_C = 12 * 60 - time_C
    edges = construct_edges(sorted(events))

    # solve(edges, time_J, time_C)
    # print()
    # print(edges)
    # print("J:", time_J, "C: ", time_C)
    # print("-------")

    print("Case #{}: {}".format(test_case_no, solve(edges, time_J, time_C)))
