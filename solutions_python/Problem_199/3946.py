from collections import deque

flip = {
    '+': '-',
    '-': '+'
}


def flip_cakes(cakes, index, length):
    begin = cakes[:index]
    middle = cakes[index:index + length]
    end = cakes[index + length:]
    if '-' in middle:
        middle = ''.join([flip[x] for x in middle])
        return begin + middle + end
    return None



def legal_flips(cake_length, flipper_length):
    return range(0, cake_length - flipper_length + 1)


def happify(cakes, flipper_length):
    target = '+' * len(cakes)
    if cakes == target: return 0
    results = {cakes: 0}
    queue = deque([(0, cakes)])
    local_legal_flips = list(legal_flips(len(cakes), flipper_length))

    while queue:
        cur = queue.popleft()
        cur_cake = cur[1]
        cur_dist = cur[0] + 1
        new_cakes = [flip_cakes(cur_cake, i, flipper_length) for i in local_legal_flips]
        if target in new_cakes:
            return str(cur_dist)
        really_new_cakes = [new_cake for new_cake in new_cakes if new_cake and new_cake not in results]
        for cake in really_new_cakes:
            results[cake] = cur_dist

        queue.extend([(cur_dist, cake) for cake in really_new_cakes])
    return 'IMPOSSIBLE'


def process(file):
    file = file.split('\n')[1:]
    ct = 1
    for line in file:
        cake, flipper = line.split(' ')
        flipper = int(flipper)
        happy_time = happify(cake, flipper)
        print('CASE #{}: {}'.format(ct, happy_time))
        ct += 1

process('''100
---+-++- 3
+++++ 4
-+-+- 4
++-- 3
-+-+ 3
-+-+ 2
-+- 2
-+++++++-- 2
+++------- 7
--+---++- 6
++-+ 3
--+-+-+--+ 3
-- 2
+--+ 2
+-+-+-+-+- 2
+-+- 3
-+++++++++ 2
-++ 2
---+ 3
++-- 2
++++ 2
+++- 2
---------- 10
--------+ 8
---------- 3
--++- 2
--++ 2
++++ 3
++------- 4
--++++-- 4
-++ 3
+-++ 2
---+--- 3
+-+-+-+-+ 3
--+ 2
---++ 3
+-+-+-+- 3
+- 2
+-- 2
-++- 3
--+++--- 5
--- 2
-++++++++- 8
-++- 2
-+-- 3
++- 2
+++- 3
-++-+--+-- 7
---+ 2
-+++ 2
--- 3
-+ 2
+++ 2
-++++++++- 10
-+-+-+-+-+ 2
---------- 2
+-+ 3
++--+-- 2
+-+- 2
-+++ 3
+---+-++ 5
-+++-- 3
+++ 3
++-++- 2
--+- 2
-+-- 2
----+ 2
+--- 3
---------- 5
+-++ 3
+-+-+-+-+- 3
++- 3
+-+ 2
-+++++++-+ 2
-++++++++- 9
-++++++++- 2
---+----++ 4
++ 2
++++++ 6
--+ 3
++-+ 2
--+-+++ 4
---- 3
+-- 3
----+ 3
--++ 3
++--++++- 5
---- 2
--+- 3
++++++++++ 10
-++++- 5
-+- 3
--------- 3
---+++--- 6
+--+ 3
+-+-+-+ 3
+++++++++ 9
+---+ 4
+-++- 2
+--- 2''')