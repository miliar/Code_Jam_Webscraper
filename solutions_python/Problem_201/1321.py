import sys
import queue

def odd(n):
    return n % 2 == 0

def add(inst, num, instances, counters):
    if inst > 0 and num > 0:
        if inst not in counters:
            instances.put(inst)
            counters[inst] = num
        else:
            counters[inst] = counters[inst] + num
    
def solve(n, m):
    instances = queue.Queue()
    counters = {}
    add(n, 1, instances, counters)
    while m > 0:
      inst = instances.get()
      available = counters[inst]
      shitters = min(available, m)
      m -= shitters
      if odd(inst - 1):
          l1 = (inst - 1) // 2
          l2 = l1
          add(l1, 2 * shitters, instances, counters)
      else:
          l1 = (inst - 1) // 2
          l2 = l1 + 1
          add(l2, shitters, instances, counters)
          add(l1, shitters, instances, counters)
    return (min(l1, l2), max(l1, l2))

def main():
    fname = sys.argv[1]
    with open(fname) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if i == 0:
            n_cases = int(line)
            assert(len(lines) == n_cases + 1)
        else:
            line = line[:-1]
            split = line.split(" ")
            n = int(split[0])
            m = int(split[1])
            (mi, ma) = solve(n, m)
            print("Case #%i: %i %i" % (i, ma, mi))

if __name__ == "__main__":
    main()
