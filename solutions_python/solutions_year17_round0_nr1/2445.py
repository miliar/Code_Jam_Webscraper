# -*- coding: utf-8 -*-

# QR A. Oversized Pancake Flipper

#INPUT = 'A-small-attempt0.in'
#INPUT = 'qr_a-small.in'
#OUTPUT = 'qr_a-small.out'
INPUT = 'A-large.in'
OUTPUT = 'qr_a-large.out'


def result(caseno, msg):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %s\n' % (caseno, msg))
    output.close()


def main():
    input = open(INPUT, 'r')

    case = int(input.readline().replace('\n',''))    # 1行目問題数
    
    for caseno in range(1, case+1):
        pancake, flip = input.readline().replace('\n','').split(' ')
        flip_count = int(flip)

        pancake_list = list(pancake)
        count = 0
        while True:
            try:
                i = pancake_list.index('-')
            except:
                result(caseno, count)
                break

            if i+flip_count > len(pancake_list):
                result(caseno, 'IMPOSSIBLE')
                break

            count += 1
            for n in range(i,i+flip_count):
                if pancake_list[n] == '+':
                    pancake_list[n] = '-'
                else:
                    pancake_list[n] = '+'

if __name__ == '__main__':
    main()
