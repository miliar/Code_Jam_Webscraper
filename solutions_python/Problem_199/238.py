#coding: utf-8

def openfile(path):
    in_ = open(path)
    case_num = int(in_.readline())
    data = []
    K = []
    for i in range(case_num):
        s = in_.readline().strip('\n').split(' ')
        data.append(s[0])
        K.append(int(s[1]))
    in_.close()
    return case_num, data, K

def _reverse(char):
    if char == '-':
        return '+'
    if char == '+':
        return '-'

def calculate(cake_str, K):
    str_list = list(cake_str)
    str_length = len(cake_str)
    regu_cake_str = []
    count = 0
    _reverse_start = 0
    while True:
        _index = -1
        if '-' in str_list:
            _index = str_list.index('-', _reverse_start)
        print 'index; ', _index
        if _index<0:
            return count
        if (_index + K) > str_length:
            return 'IMPOSSIBLE'
        for i in range(K):
            str_list[i+_index] = _reverse(str_list[i+_index])
        _reverse_start = _index + 1
        count+=1

if __name__ == '__main__':
    filepath = 'A-large.in'
    case_num, data, Ks = openfile(filepath)
    out = open('A-large-out', 'w')
    for i in range(case_num):
        print i
        _data = data[i]
        K = Ks[i]

        tmp_num = calculate(_data, K)
        out.write('Case #' + str(i + 1) + ': ' + str(tmp_num) + '\n')
    out.close()


