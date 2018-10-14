import os
from operator import itemgetter

def get_samples():
    return [os.path.join('in', filename) for filename in os.listdir('in')]

def get_input(path):
    with open(path, 'r') as f:
        return f.readlines()

def write_file(filename, content):
    path = os.path.join('out', filename[3:] + '.out')
    with open(path, 'w+') as f:
        return f.writelines(content)

def parse_input(ar):
    res = []
    i = 1
    for _ in range(int(ar[0])):
        d, n = map(int, ar[i].split())
        tab = [map(int, x.split()) for x in ar[i + 1: i + 1 + n]] # kilometer, speed
        res.append({'d': d, 'n': n, 'ar': tab})
        i += n + 1
    return res


def algo(data):
    return [algo_(**testcase) for testcase in data]


def algo_(d, n, ar):
    ar = sorted(ar, key=itemgetter(0), reverse=True)
    finished_times = [finished_time(d - k, s) for k, s in ar] # calc time of finished for each
    # pick best
    best = finished_times[0]
    for v in finished_times[1:]:
        if v > best:
            best = v
    # calc result
    return d / best

def finished_time(d, s):
    return float(d) / s

def format(result):
    return ["Case #%d: %6f\n" % (i+1, x) for i, x in enumerate(result)]

def main():

    for file_ in get_samples():
        input_ = get_input(file_)
        data = parse_input(input_)
        result = algo(data)
        write_file(file_, format(result))

if __name__ == '__main__':
    main()
