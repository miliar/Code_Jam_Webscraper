# -*- coding: utf-8 -*-

# Problem A. Magic Trick

INPUT = 'A-small-attempt0.in'
OUTPUT = 'output-a-small.txt'


def check(caseno, card1, card2):
    msg = ''

    answer = set(card1) & set(card2)    
    count = len(answer)
    if count == 1:
        # 見つけた！
        answer = list(answer)
        msg = answer[0]
    elif count > 1:
        # 失敗
        msg = 'Bad magician!'
    else:
        # チートしやがった
        msg = 'Volunteer cheated!'

    result(caseno, msg)

def result(caseno, msg):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %s\n' % (caseno, msg))
    output.close()

def main():
    input = open(INPUT, 'r')

    case = int(input.readline().replace('\n',''))    # 1行目問題数
    for caseno in range(1, case+1):
        # 1回目
        row1 = int(input.readline().replace('\n',''))
        card1 = []
        for j in range(1,5):
            line = input.readline().replace('\n','')
            if j == row1:
                card1 = line.split(' ')

        # 2回目
        row2 = int(input.readline().replace('\n',''))
        card2 = []
        for j in range(1,5):
            line = input.readline().replace('\n','')
            if j == row2:
                card2 = line.split(' ')

        # チェック！
        check(caseno, card1, card2)

    input.close()


if __name__ == '__main__':
    main()
