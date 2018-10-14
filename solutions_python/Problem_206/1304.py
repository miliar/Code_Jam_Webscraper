#coding: utf-8
import math
import copy
def openfile(path):
    in_ = open(path)
    case_num = int(in_.readline())
    D_list = []
    N_list = []
    N_K_S = []
    for i in range(case_num):
        D_str, N_str = in_.readline().strip('\n').split(' ')
        D = int(D_str)
        N = int(N_str)
        N_list.append(N)
        D_list.append(D)

        _K_S = []
        for j in range(N):
            K_str, S_str = in_.readline().strip('\n').split(' ')
            _tmp = [0, 0]
            _tmp[0] = int(K_str)
            _tmp[1] = int(S_str)
            _K_S.append(_tmp)
        N_K_S.append(_K_S)
    in_.close()
    return case_num, D_list, N_list, N_K_S

if __name__ == '__main__':
    filepath = 'A-large.in'
    case_num, D_list, N_list, N_K_S = openfile(filepath)
    out = open('A-large-out', 'w')
    for i in range(case_num):
        print 'i=',i
        _N = N_list[i]
        _D = D_list[i]
        _K_S = N_K_S[i]
        print '_N', _N
        print '_D', _D
        print '_K_S'
        print _K_S

        max_time = 0.
        for j in range(_N)[::-1]:
            _K = _K_S[j][0]
            _S = _K_S[j][1]

            dis = _D - _K
            print 'dis', dis
            max_time = max(max_time, float(dis)/_S)
        print 'max_time', max_time
        res = _D/max_time

        out.write('Case #' + str(i + 1) + ': ' + str(res) + '\n')
    out.close()