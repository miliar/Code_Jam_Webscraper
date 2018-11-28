

with open('A-large.in') as fl:
    input_content = fl.read()

stokenizer = iter(input_content.split())


def next_token():
    return stokenizer.next()


def next_int():
    return int(next_token())


n_tc = next_int()

outp = open('output.txt', 'w')

for tc_num in range(1, n_tc + 1):
    a = next_int()
    b = next_token()

    ans = 0
    standing = 0

    for i in range(0, len(b)):
        if standing < i:
            ans += i - standing
            standing = i

        standing += int(b[i])

    outp.write('Case #%i: %i\n' % (tc_num, ans))

outp.close()
