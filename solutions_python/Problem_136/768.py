# -*- coding: utf-8 -*-

# Problem B. Cookie Clicker Alpha
#INPUT = 'problem-b-test.in'
#INPUT = 'B-small-attempt0.in'
#OUTPUT = 'output-b-small.txt'
INPUT = 'B-large.in'
OUTPUT = 'output-b-large.txt'


def check(caseno, C, F, X):
    total = 0
    p = 2.0

    if X <= C:
        # X <= C ならfarmを作る前に目的の数に到達する
        total = X/p

    else:
        while True:
            # farmを買えるようになるまでの時間
            f_time = C/p

            # 買わずにX-Cの時間(case1)とfarmを買ってXを作る時間(case2)のどっちが早いか
            case1 = (X-C)/p
            case2 = X/(p+F)
            if case1 < case2:
                total += f_time + case1
                break
            else:
                # farm買ったのでCookie作れる量が増える
                total += f_time            
                p += F

    result(caseno, total)

def result(caseno, total):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %9.7f\n' % (caseno, total))
    output.close()

def main():
    input = open(INPUT, 'r')

    input.readline()    # 1行目無視
    caseno = 0
    for line in input:
        caseno += 1
        line = line.replace('\n', '')
        data = line.split(' ')
        C = float(data[0])
        F = float(data[1])
        X = float(data[2])
        check(caseno, C, F, X)

    input.close()


if __name__ == '__main__':
    main()
