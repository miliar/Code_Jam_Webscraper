def find_best(a, b):
    if(b == a+1): return -1, -1, -1, -1, -1
    s = (a + b)/2
    return b-s-1, s-a-1, a, s, b

def insert_sort(wait_list, s, count):
    for i, e in enumerate(wait_list):
        if(e[0] < s):
            wait_list.insert(i, (s, count))
            return wait_list
        if(e[0] == s):
            wait_list[i] = (e[0], e[1]+count)
            return wait_list
    wait_list.append((s, count))
    return wait_list

with open('C-large.out', 'w') as output:
    with open('C-large.in') as input:
        m = int(input.readline(-1).strip())
        for i in range(m):
            print i
            n, k = [int(x) for x in input.readline(-1).strip().split()]
            min_l = 0
            max_l = 0
            wait_list = [(n, 1)]

            while(k > 0):
                s, count = wait_list[0]
                del wait_list[0]
                if s%2 == 0:
                    s0 = (s+1)/2; s1 = (s-1)/2
                else:
                    s0 = s1 = (s-1)/2
                if k <= count:
                    min_l = s1; max_l = s0
                    break
                else:
                    k -= count
                if s0 != 0:
                    insert_sort(wait_list, s0, count)
                if s1 != 0:
                    insert_sort(wait_list, s1, count)
            output.write("Case #%d: %d %d\n" % (i+1, max_l, min_l))




