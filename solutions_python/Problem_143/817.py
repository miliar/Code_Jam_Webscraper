def input():
    line = raw_input()
    return line.split(' ')

def solve():
    TESTS = map(int, input())[0]
    for x in range(1, TESTS + 1):
        line = map(int, input())
        machine_1 = line[0]
        machine_2 = line[1]
        key = line[2]

        count = 0
        hashmap = {}
        for y in range(0, machine_1):

            for z in range(0, machine_2):
                result = y & z
                if result < key:
                    hashmap.update({(y, z) : 1})
        kkk = len(hashmap)
        print "case #{}: {}".format(x, kkk)
        count = 0

if __name__ == '__main__':
    solve()