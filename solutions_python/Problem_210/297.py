# def flip(n):
#     return (n + 720) % 1440
#
#
# def check_free(good, start, end):
#     for time in good:
#         if start <= time[0] <= end or start <= time[1] <= end:
#             return True
#     return False
#
#
# def run():
#     Ac, Aj = [int(x) for x in input().strip().split()]
#     bad_times = []
#     for t in range(Ac + Aj):
#         bad_times.append([int(x) for x in input().strip().split()])
#     bad_times.sort()
#
#     good_times = [item for sublist in bad_times for item in sublist]
#     good_times.insert(0, 0)
#     good_times.append(1440)
#     good_times = [[good_times[i], good_times[i+1]] for i in range(0, len(good_times), 2)]
#
#     for time in good_times:
#         start, end = [flip(t) for t in time]
#         if start > end:
#             if check_free(good_times, 0, end) or check_free(good_times, start, 1440):
#                 return True
#         else:
#             if check_free(good_times, start, end):
#                 return True
#
#     return False


def total_time(time):
    return time[1] - time[0]


def check(times):
    if len(times) >= 2 and total_time(times[0]) + total_time(times[-1]) >= 720:
        return True

    for time in times:
        if total_time(time) >= 720:
            return True

    return False


def run():
    Ac, Aj = [int(x) for x in input().strip().split()]

    Ac_times = []
    for t in range(Ac):
        Ac_times.extend([int(x) for x in input().strip().split()])
    Ac_times.sort()
    Ac_times.insert(0, 0)
    Ac_times.append(1440)
    Ac_times = [[Ac_times[i], Ac_times[i + 1]] for i in range(0, len(Ac_times), 2)]

    Aj_times = []
    for t in range(Aj):
        Aj_times.extend([int(x) for x in input().strip().split()])
    Aj_times.sort()
    Aj_times.insert(0, 0)
    Aj_times.append(1440)
    Aj_times = [[Aj_times[i], Aj_times[i + 1]] for i in range(0, len(Aj_times), 2)]

    return check(Ac_times) and check(Aj_times)

for case in range(int(input())):
    print("Case #{}: {}".format(case+1, 2 if run() else 4))
