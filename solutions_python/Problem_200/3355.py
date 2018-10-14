
def tidy(num):
    if num < 10:
        return num
    elif num == 10:
        return 9
    else:
        reversed_num_list = [int(i) for i in str(num)][::-1]
        num_len = len(reversed_num_list) - 1
        for index in range(num_len):
            if reversed_num_list[index] < reversed_num_list[index+1]:
                if index > 0 and reversed_num_list[index] <= reversed_num_list[index-1]:
                    for i in range(index+1):
                        reversed_num_list[i] = 9
                    reversed_num_list[index+1] -= 1
                else:
                    reversed_num_list[index] = 9
                    reversed_num_list[index+1] -= 1
        return int(''.join([str(i) for i in reversed_num_list[::-1]]))

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        print('Case #{}: {}'.format(i, tidy(n)))
