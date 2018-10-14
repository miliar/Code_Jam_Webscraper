#coding: utf-8
import math
def openfile(path):
    in_ = open(path)
    case_num = int(in_.readline())
    N = []
    K = []
    for i in range(case_num):
        _t = in_.readline().strip('\n').split(' ')
        N.append(int(_t[0]))
        K.append(int(_t[1]))
    in_.close()
    return case_num, N, K

def calculate(N, K):
    bin_K = bin(K)[2:]
    bin_len = len(bin_K)

    already_live = int(math.pow(2, bin_len-1)) - 1
    print 'already live:', already_live
    _mean = (N - already_live)/int(math.pow(2, bin_len-1))
    print 'mean: ', _mean
    _moreThanMean_num = (N - already_live) - _mean * int(math.pow(2, bin_len-1))
    print 'more than mean num: ', _moreThanMean_num
    if (K-already_live) > _moreThanMean_num:
        _d = _mean
    else:
        _d = _mean + 1
    print '_d: ', _d
    left = int((_d-1)/2)
    right = int((_d)/2)
    res_min = min(left, right)
    res_max = max(left, right)
    return res_min, res_max


if __name__ == '__main__':
    filepath = 'C-large.in'
    case_num, Ns, Ks = openfile(filepath)
    out = open('C-large-out', 'w')
    for i in range(case_num):
        print 'i=',i
        _N = Ns[i]
        _K = Ks[i]

        _min, _max = calculate(_N, _K)
        print '***************'

        out.write('Case #' + str(i + 1) + ': ' + str(_max) + ' '+ str(_min) + '\n')
    out.close()