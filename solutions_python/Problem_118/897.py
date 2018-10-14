import os
import pickle

__author__ = 'saimanoj'


def preprocess():
    fair_sq_file_name = './fair-n-sq'
    if os.path.exists(fair_sq_file_name):
        fair_sq_file = open(fair_sq_file_name)
        fair_sq_list = pickle.load(fair_sq_file)
    else:
        fair_sq_file = open(fair_sq_file_name, 'w')
        fair_sq_list = []
        start = 1
        stop = 10 ** 14
        i = start
        i_sq = start ** 2
        while i_sq <= stop:
            i_str = str(i)
            if i_str == i_str[::-1]:  # Palindrome check
                i_sq_str = str(i_sq)
                if i_sq_str == i_sq_str[::-1]:
                    # Palindrome check after squaring
                    fair_sq_list.append(i_sq)
            i_sq = i_sq + 2 * i + 1
            i += 1
        pickle.dump(fair_sq_list, fair_sq_file)

    fair_sq_file.close()
    return fair_sq_list


def find_count(A, B, fair_sq_list):
    relevant_range = [int(A <= x <= B) for x in fair_sq_list]
    return sum(relevant_range)


def main():
    fair_sq_list = preprocess()
    T = int(raw_input())
    for i in range(1, T + 1):
        A, B = map(int, raw_input().split())
        print 'Case #' + str(i) + ': ' + str(find_count(A, B, fair_sq_list))


if __name__ == '__main__':
    main()

