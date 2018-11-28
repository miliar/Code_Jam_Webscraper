import fileinput
import functools

@functools.lru_cache(maxsize=1000)
def wp(line):
    total = line.count('0')+line.count('1')
    return float(line.count('1'))/total

@functools.lru_cache(maxsize=1000)
def wpi(line, you):
    total = line.count('0')+line.count('1')
    if line[you] != '.':
        total -= 1
    wins = line.count('1')
    if line[you] == '1':
        wins -= 1
    return float(wins)/total


@functools.lru_cache(maxsize=1000)
def owp(schedule, you):
    wps = 0.0
    c = 0
    for op, s in enumerate(schedule[you]):
        if s != '.':
            wps += wpi(schedule[op], you)
            c += 1
    return wps/c

@functools.lru_cache(maxsize=1000)
def oowp(schedule, you):
    owps = 0.0
    c = 0
    for op, s in enumerate(schedule[you]):
        if s != '.':
            owps += owp(schedule, op)
            c += 1
    return owps/c


def solve(schedule):
    for you, line in enumerate(schedule):
        yield 0.25 * wp(line) + 0.50 * owp(schedule, you) + 0.25 * oowp(schedule, you)

readline = fileinput.input().readline
case_count = int(readline())
for case_no in range(case_count):
    count = int(readline())
    schedule = []
    for i in range(count):
        schedule.append(readline().strip())
    answer = '\n'.join('%f'% x for x in solve(tuple(schedule)))
    print("Case #%d:\n%s" % (case_no+1, answer))
