#coding: utf-8

def openfile(path):
    in_ = open(path)
    case_num = int(in_.readline())
    data = []
    for i in range(case_num):
        data.append(in_.readline().strip('\n'))
    in_.close()
    return case_num, data

def calculate(num_str):
    if len(num_str) == 1:
        return int(num_str)
    num_list = ['0' for i in range(len(num_str))]
    num_list[0] = (num_str[0])
    equal_start_map = [i for i in range(len(num_str))]
    for i in range(1, len(num_str)):
        if int(num_str[i]) >= int(num_str[i-1]):
            num_list[i] = num_str[i]
            if(int(num_str[i]) == int(num_str[i-1])):
                equal_start_map[i] = min(i-1, equal_start_map[i-1])
            continue
        else:
            for j in range(equal_start_map[i-1] + 1, len(num_str)):
                num_list[j] = '0'
            break
    print num_list
    if '0' in num_list:
        res = int(''.join(num_list))-1
    else:
        res = int(''.join(num_list))
    print res
    return res


if __name__ == '__main__':
    filepath = 'B-large.in'
    case_num, data = openfile(filepath)
    out = open('B-large-out', 'w')
    for i in range(case_num):
        print i
        _data = data[i]

        tmp_num = calculate(_data)
        out.write('Case #' + str(i + 1) + ': ' + str(tmp_num) + '\n')
    out.close()