"""Google Code Jam 2015 First Exercise.

The first line of the input gives the number of test cases, T.
T test cases follow.

Each consists of one line with _Smax_, the maximum shyness level of the
shyest person in the audience, followed by a string of _Smax_ + 1 single
digits.
The _kth_ digit of this string (counting starting from 0) represents
how many people in the audience have shyness level k.
For example, the string "409" would mean that there were four audience
members with Si = 0 and nine audience members with Si = 2 (and none with
    Si = 1 or any other value).
Note that there will initially always be between 0 and 9 people with each
shyness level.

Limits

1 <= T <= 100.

Small dataset: 0 <= Smax <= 6.

Large dataset: 0 <= Smax <= 1000.
"""

from __future__ import print_function

with open("A-large.in") as f:
    data = [line for line in f]

for case, line in enumerate(data[1:]):
    datums = line.split()
    smax = datums[0]
    people = datums[1]
    total = 0
    needed = 0
    for i, p in enumerate(people):
        p = int(p)
        if p == 0:
            continue
        while total < i:
            needed += 1
            total += 1
        total += p
    print("Case #{0}: {1}".format(case + 1, needed))
