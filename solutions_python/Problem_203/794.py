#coding=utf-8
#author=godpgf
import fileinput

def get_res(data_list, n):
    pos_list = list()
    for r in range(len(data_list)):
        for c in range(len(data_list[r])):
            if data_list[r][c] != '?':
                pos_list.append((r,c))
                n -= 1
    return cake(data_list, pos_list, 0, n)

def write_row(data_list, r, c, is_clean = False):
    n = 0
    target = '?'
    fill = data_list[r][c]
    if is_clean:
        target, fill = fill, target
    left = True
    right = True
    left_id = c
    right_id = c
    for i in range(1, len(data_list[r])):
        if right and c + i < len(data_list[r]) and data_list[r][c+i] == target:
            data_list[r][c + i] = fill
            n += 1
            right_id = c+i
        else:
            right = False
        if left and c - i >= 0 and data_list[r][c-i] == target:
            data_list[r][c - i] = fill
            n += 1
            left_id = c - i
        else:
            left = False

    left = True
    right = True
    if left_id != right_id:
        for i in range(1, len(data_list)):
            if right and r + i < len(data_list) and check_row_empty(data_list,r+i,left_id,right_id,target,fill):
                n += (right_id + 1 - left_id)
            else:
                right = False
            if left and r - i >= 0 and check_row_empty(data_list,r-i,left_id,right_id,target,fill):
                n += (right_id + 1 - left_id)
            else:
                left = False

    return n

def check_row_empty(data_list, r, left_id, right_id, target, fill):
    for i in range(left_id, right_id+1):
        if data_list[r][i] != target:
            return False
    for i in range(left_id, right_id + 1):
        data_list[r][i] = fill
    return True


def write_column(data_list, r, c, is_clean = False):
    n = 0
    target = '?'
    fill = data_list[r][c]
    if is_clean:
        target, fill = fill, target
    left = True
    right = True
    left_id = r
    right_id = r
    for i in range(1, len(data_list)):
        if right and r + i < len(data_list) and data_list[r+i][c] == target:
            data_list[r+i][c] = fill
            n += 1
            right_id = r+i
        else:
            right = False
        if left and r - i >= 0 and data_list[r-i][c] == target:
            data_list[r-i][c] = fill
            n += 1
            left_id = r-i
        else:
            left = False

    left = True
    right = True
    if left_id != right_id:
        for i in range(1, len(data_list[r])):
            if right and c + i < len(data_list[r]) and check_column_empty(data_list,c+i,left_id,right_id,target,fill):
                n += (right_id + 1 - left_id)
            else:
                right = False
            if left and c - i >= 0 and check_column_empty(data_list,c-i,left_id,right_id,target,fill):
                n += (right_id + 1 - left_id)
            else:
                left = False

    return n



def check_column_empty(data_list, c, left_id, right_id, target, fill):
    for i in range(left_id, right_id+1):
        if data_list[i][c] != target:
            return False
    for i in range(left_id, right_id + 1):
        data_list[i][c] = fill
    return True

def copy_list(data_list):
    return [data[:] for data in data_list]


def cake(data_list, pos_list, index, remain_cell):
    #尝试把一行都填上
    n = write_row(data_list,pos_list[index][0], pos_list[index][1])
    if index == len(pos_list) - 1:
        if remain_cell - n == 0:
            return [data[:] for data in data_list]
        else:
            write_row(data_list,pos_list[index][0], pos_list[index][1], True)
    else:
        new_data_list = cake(data_list, pos_list, index+1,remain_cell-n)
        if new_data_list:
            return new_data_list
        else:
            write_row(data_list, pos_list[index][0], pos_list[index][1], True)

    #尝试把一列都填上
    n = write_column(data_list,pos_list[index][0], pos_list[index][1])
    if index == len(pos_list) - 1:
        if remain_cell - n == 0:
            return [data[:] for data in data_list]
        else:
            write_column(data_list,pos_list[index][0], pos_list[index][1], True)
    else:
        new_data_list = cake(data_list, pos_list, index+1,remain_cell-n)
        if new_data_list:
            return new_data_list
        else:
            write_column(data_list, pos_list[index][0], pos_list[index][1], True)

    return None




if __name__ == '__main__':
    input = fileinput.input('A-small-attempt2.in')
    t = int(input.readline())
    for i in range(t):
        r_c = input.readline()[:-1]
        r = int(r_c.split(' ')[0])
        c = int(r_c.split(' ')[1])
        data_list = list()
        for j in range(r):
            data = input.readline()[:-1]
            data_list.append(list(data))

        print "Case #%d:" %(i + 1)

        """
        for data in data_list:
            print ''.join(data)
        print ""
        """

        data_list = get_res(data_list, r * c)
        if data_list is None:
            print "eee"

        for data in data_list:
            print ''.join(data)