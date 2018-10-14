#!/usr/bin/env python
def solve_test(num_plugins, snaps):
    #print "Plugins: %s\t Snaps:%s" % (num_plugins, snaps)
    if (2**num_plugins - 1) & snaps == (2**num_plugins - 1):
        return "ON"
    else:
        return "OFF"
    
if __name__ == "__main__":
    # Parse the file, and send in the details
    import fileinput
    it = fileinput.input()
    tests = int(it.next().strip())
    for x in range(1, tests+1):
        num_plugins, num_snaps = map(int, it.next().split())
        answer = solve_test(num_plugins, num_snaps)
        print "Case #%s: %s" % (x, answer)