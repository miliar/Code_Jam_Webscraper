import pandas as pd
import numpy as np
import time


def stall_occ(Stalls):
    S = [1]
    S.extend([0]*Stalls)
    S.extend([1])
    return S


def L_s(S, i):
    i_L = i
    while S[i_L] != 1:
        i_L = i_L - 1
    return i - i_L-1


def R_s(S, i):
    i_R = i
    while S[i_R] != 1:
        i_R = i_R + 1
    return i_R-i-1


def S_df(S):
    Stall = []
    for i in range(1, len(S)-1):
        L = L_s(S, i)
        R = R_s(S, i)
        Stall.append([i,S[i],L,R,min(L,R),max(L,R)])
    # df_stall = pd.DataFrame(Stall, columns=['Stall','Occ','L_S','R_S','S_min','S_max'])
    arr_stall = np.asarray(Stall)
    return arr_stall


def choose_stall(df_stall):
    df_stall = df_stall[df_stall[:, -2] == max(df_stall[:,-2])]
    # df_S_min = df_stall[df_stall['S_min] == max(df_stall['S_min'])]
    stall_shortlist = df_stall[:, 0]
    if len(stall_shortlist) > 1:
        df_stall= df_stall[df_stall[:, -1] == max(df_stall[:,-1])]
        # df_S_min_max = df_S_min[df_S_min['S_max'] == max(df_S_min['S_max'])]
        stall_shortlist = df_stall[:,0]
        if len(stall_shortlist) > 1:
            stall_chosen = min(stall_shortlist)
        else:
            stall_chosen = stall_shortlist[0]
    else:
        stall_chosen = stall_shortlist[0]
    return stall_chosen


def S_update(S, chosen_stall):
    if S[chosen_stall] == 0:
        S[chosen_stall] = 1
    else:
        print 'Chosen stall already occupied!'
    return S


def person_coming(S):
    df_stall = S_df(S)
    df_stall = df_stall[df_stall[:,1]==0]
    # df_stall = df_stall[df_stall['Occ']==0]
    # print np.delete(df_stall, df_stall[:,1], axis=1)
#     print df_stall.head()
    C_s = choose_stall(df_stall)
    S_min = int(df_stall[df_stall[:,0]==C_s,4])
    S_max = int(df_stall[df_stall[:,0]==C_s,5])
    S[C_s] = 1
    return S, S_min, S_max


def all_people(i, Stalls, People):
    S = stall_occ(Stalls)
#     print S
    C_list = []
    for i in range(People):
        S, S_min, S_max= person_coming(S)
    return S, S_min, S_max


tick = time.clock()
f_o = open('Output_4.txt', 'w')
with open('Cs_final_4.txt', 'r') as f:
    dat = f.readlines()

dat = [n.split('\n')[0] for n in dat[1:]]

Stalls = [int(n.split(' ')[0]) for n in dat]
People = [int(n.split(' ')[1]) for n in dat]
# i = 5
C_list = []
for i in range(0, len(dat)):
# i = 2

    S_final, S_min, S_max = all_people(i, Stalls[i], People[i])

    f_o.writelines("Case #{}: {} {}\n".format(i+1, S_max, S_min))
    # print S_final
    print (i, S_max, S_min)
    # text_file.write("Case #{}: {} {}\n".format(i+1, S_max, S_min))

# print C_list[:5]
# C_list = np.asarray(C_list)
#
# with open("Output_3.txt", "w") as f:
#     # np.savetxt(f, C_list, newline = " ", fmt='%d')
#     # for i in C_list:
#     #     f.writelines(i)
#     C_list.tofile(f)
# text_file.close()

tock = time.clock()
print tock-tick
