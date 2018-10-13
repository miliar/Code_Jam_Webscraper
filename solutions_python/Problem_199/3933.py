from multiprocessing import  Queue
from threading import Thread

try:
    input = raw_input
except NameError:
    pass


def checkEqual2(iterator):
    return len(set(iterator)) <= 1


def calculate(val,ret,  cas):

    s, k = val
    s = str(s)
    k = int(k)
    choices = []

    choicesRange = len(s) - k + 1

    for i in range(choicesRange):
        flip = i, i + k
        choices.append(flip)

    pat = [[s, None, 0, s.count("+")]]

    while len(pat) != 0:

        if len(pat[-1][0]) == pat[-1][3]:
            ret[cas] = (cas, len(pat) - 1)
            print("1 Thread end")
            return

        if pat[-1][2] == pat[-1][1]:
            pat[-1][2] += 1
            if pat[-1][2] == len(choices):
                pat.pop()
            continue

        c = choices[pat[-1][2]]

        pat[-1][2] += 1

        pat.append([pat[-1][0], c, 0, pat[-1][3]])

        for i in range(c[0], c[1]):
            if pat[-1][0][i] == '+':
                pat[-1][3] -= 1
                pat[-1][0] = pat[-1][0][:i] + "-" + pat[-1][0][i + 1:]
            else:
                pat[-1][3] += 1
                pat[-1][0] = pat[-1][0][:i] + "+" + pat[-1][0][i + 1:]

        for i in range(len(pat) - 1):
            if pat[i][0] == pat[-1][0]:
                while len(pat) != i + 1:
                    pat.pop()
                break
        if pat[-1][2] == len(choices):
            pat.pop()
    ret[cas] = (cas, "IMPOSSIBLE")
    print(cas ," Thread end")

q = Queue()
def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    threads = [None] * t
    results = [None] * t
    ret = ''



    for i in range(t):
        m = [s for s in input().split(" ")]
        threads[i] = Thread(target=calculate, args=(m,results,i))
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()


    for i in results:

        new = 'Case #{}: {}'.format(i[0] + 1, i[1])
        print(new)
        ret += new + "\n"

    open('output.txt', 'w').write(ret)


if __name__ == '__main__':
    main()
