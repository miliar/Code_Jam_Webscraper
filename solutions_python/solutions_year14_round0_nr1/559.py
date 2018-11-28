__author__ = 'Antariksh Bothale'
import sys

if __name__ == '__main__':
    total = map(lambda x: x.strip(), sys.stdin.readlines())
    N = int (total[0])
    i = 1
    case_num = 0
    while (True):
        P1 = int(total[i])
        i += 1
        arr = total[i:i+4]
        arr_num = [map(int, elem.split()) for elem in arr]
        i += 4
        cand_set1 = set(arr_num[P1-1])
        P2 = int(total[i])
        i += 1
        arr = total[i:i+4]
        arr_num = [map(int, elem.split()) for elem in arr]
        i += 4
        cand_set2 = set(arr_num[P2-1])
        result = cand_set1.intersection(cand_set2)
        len_result = len(result)
        ans_string = str(list(result)[0]) if len_result == 1 else 'Volunteer cheated!' if len_result == 0 else 'Bad magician!'
        case_num += 1
        print ('Case #{0}: {1}'.format(case_num, ans_string))
        if case_num == N:
            break