import sys
from collections import defaultdict
import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def do_magicka(line):
    inputs = line.split()

    non_bases = {}
    for i in range(int(inputs.pop(0))):
        elem_a, elem_b, elem_c = inputs.pop(0)
        non_bases[(elem_a,elem_b)] = non_bases[(elem_b,elem_a)] = elem_c

    clashes = defaultdict(set)
    for i in range(int(inputs.pop(0))):
        elem_a, elem_b = inputs.pop(0)
        clashes[elem_a].add(elem_b)
        clashes[elem_b].add(elem_a)

    _ = inputs.pop(0)
    invoked = list(inputs.pop(0))
    elem_list = []
    counts = defaultdict(int)
    while invoked:
        next_e = invoked.pop(0)
        if elem_list:
            replaced = non_bases.get((next_e, elem_list[-1]))
            if replaced:
                logger.debug("Converted {0} and {1} to {2}".format(next_e, elem_list[-1], replaced))
                counts[elem_list[-1]] -= 1
                elem_list[-1] = replaced
                counts[replaced] += 1
                continue
        def clashing(elem):
            for clash in clashes[next_e]:
                if counts[clash] > 0:
                    logger.debug("{0} clashed with {1}".format(next_e, clash))
                    return True
            return False
        if clashing(next_e):
            elem_list = []
            counts = defaultdict(int)
            continue

        logger.debug("Appended {0}".format(next_e))
        elem_list.append(next_e)
        counts[next_e] += 1
    return elem_list

if __name__ == "__main__":
    count = sys.stdin.next()
    for i, line in enumerate(sys.stdin):
        print "Case #{0}: ".format(i + 1) + str(do_magicka(line)).replace("'", "")
