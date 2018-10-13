from math import sqrt
from Queue import Queue, Empty


def isp(a):
    n = len(a)
    for i in xrange(n/2+1):
        if a[i] != a[n-i-1]:
            return False
    return True

top_limit = 10**100

pals = set()
upper_limit = 10000000 + 1
for i in xrange(upper_limit):
    s = str(i)
    if isp(s):
        sq = i**2
        if isp(str(sq)):
            pals.add(sq)

# Deal with big numbers now
q = Queue()
add_to_pals = set()
for num in pals:
    sq = num**2
    if sq not in pals and isp(str(sq)) and sq <= top_limit:
        q.put(sq)
        add_to_pals.add(sq)

pals.update(add_to_pals)
while True:
    try:
        num = q.get_nowait()
        sq = num**2
        if isp(str(sq)) and sq <= top_limit:
            q.put(sq)
            pals.add(sq)
    except Empty:
        break


def main(case, b_limit, u_limit):
    n = 0
    for i in pals:
        if i >= b_limit and i <= u_limit:
            n += 1

    print "Case #" + str(case) + ": " + str(n)


if __name__ == '__main__':
    f = open('input.txt', 'r')
    samples_count = int(f.readline().strip())

    for i in range(samples_count):
        b_limit, u_limit = map(int, f.readline().strip().split(' '))
        main(i+1, b_limit, u_limit)
