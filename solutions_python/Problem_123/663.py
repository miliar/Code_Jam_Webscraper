import sys


def problem_instances(filename):
    f = open(filename)
    num_instances = int(f.readline())
    for i in range(num_instances):
        a_mote, num_enems = map(int, f.readline().split())
        enem_sizes = sorted(map(int, f.readline().split()), reverse=True)
        yield a_mote, enem_sizes


def consume_lesser(a_mote, enems):
    while enems and a_mote > enems[-1]:
        a_mote += enems.pop()
    return a_mote, enems


def iterate(a_mote, enems, steps=0):
    a_mote, enems = consume_lesser(a_mote, enems)
    if not enems:
        return steps

    return min(iterate(2 * a_mote - 1, enems[:], steps + 1),
               iterate(a_mote, enems[:][:-1], steps + 1))


def solve(instance):
    a_mote, enems = instance
    if a_mote == 1:
        return len(enems)
    return iterate(a_mote, enems)


filename = sys.argv[1]
out = open(filename + ".out", "w")
for idx, instance in enumerate(problem_instances(filename), 1):
    out.write("Case #%i: %s\n" % (idx, solve(instance)))