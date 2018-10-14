from __future__ import division
palindromes = set([1, 4, 9, 121, 484,
                   10201, 12321, 14641, 40804, 44944,
                   1002001, 1234321, 4008004,
                   100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404,
                   10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L,
                   1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L])
possible_ends = set(['1', '4', '9'])


def generate_palindrome(pal_len):
    if pal_len == 0:
        yield ''
    elif pal_len == 1:
        for i in xrange(10):
            yield str(i)
    else:
        for i in xrange(10):
            for pal in generate_palindrome(pal_len - 2):
                yield str(i) + pal + str(i)


def square_root(number):
    if number == 1:
        return 1
    x = number // 2
    seen = set([x])
    while x * x != number:
        x = (x + (number // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return x

a = []
def test_pal():
    for x in generate_palindrome(13):
        str_i = x
        if int(x[0]) > 5:
            break
        if len(str_i) % 2 == 0:
            continue
        if str_i[-1] not in possible_ends or str_i[0] not in possible_ends:
            continue
        # check if it has a square
        sq = square_root(long(x))
        if not sq:
            continue
        elif str(sq) == str(sq)[::-1]:
            a.append(int(x))
            print x

lines = open('data.txt').read()
output = open('output.txt', 'w')

lines = lines.splitlines()
cases_num = int(lines[0])
lines = lines[1:]

for i in range(cases_num):
    m, n = lines[i].split()
    m = int(m)
    n = int(n)
    number = len([x for x in palindromes if m <= x <= n])
    output.write('Case #{0}:'.format(i+1) + ' ' + str(number) + '\n')
    print 'Case #{0}:'.format(i+1), number

