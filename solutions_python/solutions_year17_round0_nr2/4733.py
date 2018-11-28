from multiprocessing import Process, Queue
import re

try:
    input = raw_input
except NameError:
    pass

num = '123456789'


def calculate(val, que):
    ret = que.put

    val = val[0]
    last_num = ''

    for val in range(1, int(val) + 1):
        ordered = True
        val = str(val)

        for chr_i, ch in enumerate(str(val)):

            if chr_i != 0:

                if ord(ch) < ord(val[chr_i - 1]):
                    ordered = False

        if ordered:

            last_num = val
    ret(last_num)


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    thre = []
    ret = ''
    for i in range(t):
        m = [s for s in input().split(" ")]

        q = Queue()
        thre.append(Process(target=calculate, args=(m, q,)))
        thre[-1].start()

        new = 'Case #{}: {}'.format(i + 1, q.get())
        print(new)
        ret += new + "\n"

    for x in thre:
        x.join()

        open('output.txt', 'w').write(ret)


if __name__ == '__main__':
    main()
