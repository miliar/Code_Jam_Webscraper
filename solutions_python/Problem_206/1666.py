from collections import namedtuple

##########################

PosSpeed = namedtuple('PosSpeed', ['pos', 'speed'])
PosSpeedTime = namedtuple('PosSpeedTime', ['pos', 'speed', 'time'])

##########################

t = int(input())  # read a line with a single integer


def input_start_pos_speed():
    ks_inputs = []
    for _ in range(N):
        k, s = [s for s in input().split()]
        ks_inputs.append(PosSpeed(pos=float(k), speed=float(s)))
    return ks_inputs


# s=vt
def cal_eta(destination, cur_pos, speed):
    return (destination - cur_pos) / speed


for i in range(1, t + 1):
    D, N = [int(s) for s in input().split()]

    input_ks_array = input_start_pos_speed()
    sorted_ks_array = sorted(input_ks_array, key=lambda ks_i: ks_i.pos, reverse=True)

    if N == 1:
        ks = sorted_ks_array[0]
        time_pass = cal_eta(D, ks.pos, ks.speed)
    else:
        # pos1 > pos2
        # 1 is in front of 2
        ks1 = sorted_ks_array[0]
        ks2 = sorted_ks_array[1]
        if ks2.speed > ks1.speed:  # 2 is faster than 1
            x = ((ks1.pos - ks2.pos) * ks1.speed) / (ks2.speed - ks1.speed)
            delta_t = x / ks1.speed
            new_pos = ks1.pos + x
            if new_pos <= D:
                time_pass = cal_eta(D, new_pos, ks1.speed) + delta_t
            else:  # 1 will reach D before 2 reach 1, so 2 will reach D later
                time_pass = cal_eta(D, ks2.pos, ks2.speed)
        else:   # 1 is faster than 2
            time_pass = cal_eta(D, ks2.pos, ks2.speed)

    # sorted_ks_array = sorted(input_ks_array, key=lambda ks: ks.pos, reverse=True)

    # max_speed = resolve_annie_max_speed(sorted_ks_array, D)

    ans = D / time_pass

    print("Case #%d: %.6f" % (i, ans))
