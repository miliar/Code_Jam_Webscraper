#!/usr/bin/env python2.7
#

#def is_solved(our, others):
#    for other in others:
#        if our <= other:
#            return False
#        our += other
#    return True

import Queue
q = Queue.Queue() # put, get

def solve():
    while True:
        our, others, n = q.get(block=False)
        #print '===\nbefore\n----\nour:{}\nothers:{}\nn:{}'.format(our, others, n)

        for i, other in enumerate(others):
            if our > other:
                our += other
                continue
            #print '===\nafter\n----\nour:{}\nothers:{}\nn:{}'.format(our, others[i:], n)
            q.put([our*2-1, others[i:], n+1]) # try addind
            q.put([our, others[i:len(others)-1], n+1]) # try removing
            break
        if not others or our > others[len(others)-1]:
            return n

def main():
    T = int(raw_input())
    for i in range(0, T):
        our_mote, nb_motes = map(int, raw_input().split(' '))
        other_motes = map(int, raw_input().split(' '))
        other_motes = sorted(other_motes)
        q.queue.clear()
        q.put([our_mote, other_motes, 0])
        #print 'our: {}\nothers: {}'.format(our_mote, other_motes)

        res = solve()
        print 'Case #{}: {}'.format(i+1, res)

if __name__ == '__main__':
    main()
