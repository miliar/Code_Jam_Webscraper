# def remove_superposition(D, K, S, idx):
#     """
#
#     :param D:
#     :param K:
#     :param S:
#     :param idx: horse idx and idx+1 superpose
#     :return: the new time at position idx
#     """
#
#
#
# def find_time(D, K, S):
#     """
#
#     :param D: total distance
#     :param K:
#     :param S:
#     :return: arrival time of the last horse
#     """
#     N = len(K)
#     T = [(D-K[i])/S[i] for i in range(N)]
#     if N==1:    # just one horse
#         return T[0]
#
#     T_diff = [T[i] - T[i-1] for i in range(1, N)]
#     superpose = [dt > 0 for dt in T_diff]
#     if not any(x for x in superpose):   # no horse superposition
#         return T[0]
#
#     while any(x for x in superpose):
#         idx = superpose[::-1].index(True)  # IT IS BACKWARDS!!
#         idx = N-idx-1
#         T[idx] = remove_superposition(D, K, S, idx)
#         T_diff[idx] = T[idx + 1] - T[idx]
#         superpose[idx] = T_diff[idx] > 0
#         if idx > 0:
#             T_diff[idx-1] = T[idx] - T[idx-1]
#             superpose[idx-1] = T_diff[idx-1] > 0
#
#     return T[0]
#
#
#


with open("./A-large.in", "r") as fin:
    with open("./A-large.out", "w+") as fout:
        T = int(fin.readline().strip("\n"))

        for i in range(T):
            D, N = fin.readline().strip("\n").split()
            D, N = int(D), int(N)
            K, S = [], []
            T = []
            for j in range(N):
                k, s = fin.readline().strip("\n").split()
                k, s = int(k), int(s)
                K.append(k)
                S.append(s)
                T.append((D-k)/s)
            # time = find_time(D,K,S)

            Tf = max(T)
            speed = D/Tf

            fout.write("Case #%d: %f\n" % (i+1, speed))
