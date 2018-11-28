# -*- coding: utf-8 -*-

# Problem D. Deceitful War

#INPUT = 'problem-d-test.in'
#INPUT = 'D-small-attempt0.in'
#OUTPUT = 'output-d-small.txt'
INPUT = 'D-large.in'
OUTPUT = 'output-d-large.txt'


def check(caseno, N, naomi, ken):
    y_win = z_win = 0

    #対戦数が1回ならそのまま比較
    if N == 1:
        if naomi[0] > ken[0]:
            y_win = z_win = 1
    else:
        # Deceitful War
        _NAOMI = naomi[:]
        _KEN = ken[:]
        for n_data in _NAOMI:
            for idx, k_data in enumerate(_KEN):
                if k_data < n_data:
                    y_win += 1
                    _KEN.pop(idx)
                    break

        # War
        _NAOMI = naomi[:]
        _KEN = ken[:]
        for n_data in _NAOMI:
            if _KEN[0] > n_data:
                _KEN = _KEN[1:]
            else:
                z_win += 1
                _KEN = _KEN[:-1]

    result(caseno, y_win, z_win)

def result(caseno, y, z):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %d %d\n' % (caseno, y, z))
    output.close()

def main():
    input = open(INPUT, 'r')

    case = int(input.readline().replace('\n',''))    # 1行目問題数
    for caseno in range(1, case+1):
        # 対戦数
        N = int(input.readline().replace('\n',''))
        
        # Naomi
        data = input.readline().replace('\n','')
        naomi = map(float, data.split(' '))
        naomi.sort()
        naomi.reverse()

        # Ken
        data = input.readline().replace('\n','')
        ken = map(float, data.split(' '))
        ken.sort()
        ken.reverse()

        # チェック！
        check(caseno, N, naomi, ken)


if __name__ == '__main__':
    main()
