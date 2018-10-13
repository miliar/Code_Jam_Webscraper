def get_cruise_speed(distance, horses):
    times = []
    for horse in horses:
        dist = horse[0]
        speed = horse[1]
        times.append((distance - dist) * 1.0 / speed)
    t_max = max(times)
    return distance / t_max

#
# print(get_cruise_speed(2525, [(2400, 5)]))
# print(get_cruise_speed(300, [(120, 60), (60, 90)]))
# print(get_cruise_speed(100, [(80, 100), (70, 10)]))


test_cases = int(input())
for i in range(1, test_cases + 1):
    input_str = input()
    D_str, N_str = input_str.split(' ')
    D = int(D_str)
    N = int(N_str)
    horses = []
    for _ in range(N):
        row = input()
        K_str, S_str = row.split(' ')
        K = int(K_str)
        S = int(S_str)
        horses.append((K, S))
    # print("Case #{}: D={}, N={}, horses: {}".format(i, D, N, horses))
    speed = get_cruise_speed(D, horses)
    print("Case #{}: {}".format(i, speed))


# test_cases = int(input())
# for i in range(1, test_cases + 1):
#     input_str = input()
#     params = input_str.split(' ')
#     Hd = int(params[0])
#     Ad = int(params[1])
#     Hk = int(params[2])
#     Ak = int(params[3])
#     B = int(params[4])
#     D = int(params[5])
#     n = get_min_win_turns(Hd, Hd, Ad, Hk, Ak, B, D)
#     if n == float('inf'):
#         answer = 'IMPOSSIBLE'
#     else:
#         answer = str(n)
#     print("Case #{}: {}".format(i, answer))
