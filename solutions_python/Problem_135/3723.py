def main():
    T = int(raw_input())
    i = 1
    while T:
        arr_1 = []
        arr_2 = []
        ans_1 = int(raw_input())
        insert_arr(arr_1)
        ans_2 = int(raw_input())
        insert_arr(arr_2)
        answer = find_num(arr_1[ans_1 - 1], arr_2[ans_2 - 1])
        if answer[0] == 0:
            print 'Case #{0}: Volunteer cheated!'.format(i)
        elif answer[0] == 1:
            print 'Case #{0}: {1}'.format(i, arr_1[ans_1 - 1][answer[1][0][0]])
        else:
            print 'Case #{0}: Bad magician!'.format(i)
        i += 1
        T -= 1


def find_num(l_1, l_2):
    counter = 0
    pos = []
    for i in range(len(l_1)):
        for j in range(len(l_2)):
            if l_1[i] == l_2[j]:
                pos.append([i, j])
                counter += 1
    return (counter, pos)
        

def insert_arr(l):
    for i in range(4):
        l.append([int(j) for j in raw_input().split(' ')])


if __name__ == '__main__':
    main()
