import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

fin = open("input.txt")
fout = open("output.txt", "w")

n = int(fin.readline())
cases = list()
for i in range(n):
    cases.append(list(fin.readline().split()[1]))


for i in range(1,len(cases)+1):
    lst = list(map(int, cases[i-1]))
    cur_state = 0
    need_state = 0
    for j in range(len(lst)):

        if j > cur_state:
            need_state += 1
            cur_state += 1

        cur_state += lst[j]
    fout.write("Case #" + i.__str__() + ": " + need_state.__str__() + "\n")
fin.close()
fout.close()
