import re
import sys

def make_run(capacity, queue, front_of_queue):
    old_front_of_queue = front_of_queue
    taken = 0
    while taken + queue[front_of_queue] <= capacity:
        taken += queue[front_of_queue]
        front_of_queue += 1
        if front_of_queue == len(queue):
            front_of_queue = 0
        if front_of_queue == old_front_of_queue:
            break # a group can't board the coaster twice in one run

    return (taken, front_of_queue)

def solve(num_runs, capacity, queue):
    euros = 0
    front_of_queue = 0
    for i in xrange(num_runs):
        euros_i, front_of_queue = make_run(capacity, queue, front_of_queue)
        euros += euros_i

    return euros

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])

    for i in xrange(T):
        R, k, N = lines[2*i+1].split(' ')
        str_gs = lines[2*i+2].split(' ')
        group_sizes = [int(s) for s in str_gs]
        assert int(N)==len(group_sizes)
        euros = solve(int(R), int(k), group_sizes)
        print 'Case #%d: %d' % (i+1, euros)

if __name__ == '__main__': main()
