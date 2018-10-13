import multiprocessing
import sys
import itertools
import re


def reader(f):
    return f.readlines()


def writer(f, data):
    f.write(data)


def chunks(l, n, k=0):
    for i in xrange(0, len(l), n):
        yield l[i:i+(n-k)]

def split(data):
    return [[str(x).strip() for x in y] for y in chunks(data, 5, 1)]


def transform(queue, i, workset):
    #check possible wins
    positions = [zip(range(4), itertools.repeat(x)) for x in range(4)] + [zip(itertools.repeat(x), range(4)) for x in range(4)]
    positions.append(zip(range(4), range(4)))
    positions.append(zip(range(3, -1, -1), range(4)))

    r = "Case #%d: " % i
    for p in ["X", "O"]:
        for win_str in ["%s%s%s%s" % (workset[a[0]][a[1]], workset[b[0]][b[1]], workset[c[0]][c[1]], workset[d[0]][d[1]]) for a, b, c, d in positions]:
            if len(re.findall("^([%s|T]{4})$" % p, win_str)) > 0:
                queue.put(r + "%s won" % p)
                return
    for i in range(4):
        if "." in workset[i]:
            queue.put(r + "Game has not completed")
            return

    queue.put(r + "Draw")
    return

if __name__ == "__main__":
    #read
    data = reader(sys.stdin)

    #extract something
    num_jobs = int(data[0].strip())

    #split
    worksets = split(data[1:])
    if num_jobs != len(worksets):
        sys.stderr.write("Size mismatch: %d, %d\n" % (num_jobs, len(worksets)))
        sys.exit(-1)

    #transform
    queue = multiprocessing.Queue()
    worker = []
    for i, workset in enumerate(worksets):
        p = multiprocessing.Process(name="Worker %d" % i, target=transform, args=(queue, i+1, workset))
        p.start()
        worker.append(p)

    #wait
    for w in worker:
        w.join()

    #accumulate results
    r = []
    for w in worker:
        r.append(queue.get())

    #write
    for x in sorted(r, key=lambda s: int(s[s.find("#")+1:s.find(":")])):
        writer(sys.stdout, x+"\n")
