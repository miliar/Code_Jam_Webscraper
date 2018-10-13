import sys

with open('B-large.in') as fl:
#with open('input.txt') as fl:
    input_content = fl.read()

stokenizer = iter(input_content.split())


def next_token():
    return stokenizer.next()


def next_int():
    return int(next_token())

outp = open('output.txt', 'w')
#outp = sys.stdout
n_tc = next_int()


for tc_num in range(1, n_tc + 1):
    diners = []

    n = next_int()
    for i in range(n):
        diners.append(next_int())

    ans = 10000

    for target in range(1, 1001):
        summ = target

        for x in diners:
            if x > target:
                summ += x / target - 1
                if x % target != 0:
                    summ += 1

        ans = min(ans, summ)

    outp.write('Case #%i: %i\n' % (tc_num, ans))
