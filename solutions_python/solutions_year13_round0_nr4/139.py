#!/usr/bin/env python

import sys
import logging


def go(remaining, keys, chests,  cache):
    """
    """
    # logging.info("remaining: %s, keys: %s", remaining, keys)


    cache_key = frozenset(remaining)
    
    if cache_key in cache:
        return cache[cache_key]
        
    for c in sorted(remaining):
        if chests[c][0] in keys:
            # logging.info("keys: %s", keys)
            new_keys = list(keys)
            new_keys.remove(chests[c][0])
            # logging.info("keys (after removing %d): %s", chests[c][0], new_keys)
            if chests[c][1] != 0:
                new_keys.extend(chests[c][2:])
            # logging.info("keys after chest %s => %s", chests[c], new_keys)
            new_remain = remaining.difference([c])
            r = []
            if new_remain:
                r = go(new_remain, new_keys, chests, cache)

            if r is not None:
                result = [c] + r
                cache[cache_key] = result
                return result
    cache[cache_key] = None
    return None
    
        
            
            
        

def solve(keys, chests):
    result = go(set(range(len(chests))),
                list(keys),
                chests,
                {})
    if result:
        return " ".join([str(x + 1) for x in result])
    else:
        return "IMPOSSIBLE"


def main(lines, output):
    T = int(lines.next())
    for case in xrange(1,T+1):
        K, N = map(int, lines.next().split())
        keys = map(int, lines.next().split())
        chests = []
        for kk in xrange(N):
            chests.append(map(int, lines.next().split()))
        r = solve(keys, chests)
        s = "Case #%d: %s" % (case, r)
        output.write(s + "\n")
        logging.info(s)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "expects filename"
        sys.exit(1)
    logging.basicConfig(level=logging.DEBUG)
    outfile = sys.argv[1] + ".out"
    main(open(sys.argv[1]), open(outfile, "w"))

