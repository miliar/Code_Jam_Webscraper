import sys

if __name__ == '__main__':
    cases = int(input())
    for c in range(1, cases + 1):
        print('Case #%d: ' % c, end='')
        row_no_1 = int(input())
        row_1 = [input() for idx in range(4)][row_no_1 - 1]
        set_1 = set(int(x) for x in row_1.split())
        row_no_2 = int(input())
        row_2 = [input() for idx in range(4)][row_no_2 - 1]
        set_2 = set(int(x) for x in row_2.split())
        inter_set = set_1.intersection(set_2)
        if len(inter_set) == 1:
            print(inter_set.pop())
        elif len(inter_set) > 1:
            print('Bad magician!')
        else:
            print('Volunteer cheated!')