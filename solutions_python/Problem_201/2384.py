import time
import threading


VACANT = '.'
OCCUPIDE = 'O'


def consume_gaps(stalls):
    stalls = [OCCUPIDE] + stalls[:] + [OCCUPIDE]
    prev = OCCUPIDE
    counter = 0
    begin_index = 0
    results = []
    for i in xrange(len(stalls)):
        if prev == stalls[i]:
            counter += 1
        else:
            if prev == VACANT:
                results.append((begin_index, prev, counter))
            counter = 1
            begin_index = i
            prev = stalls[i]
    
    if prev == VACANT:
        results.append((begin_index, prev, counter))

    return results


def add_man(gaps):
    max_gaps = max(gaps, key=lambda x: x[1])
    filtered = [x for x in gaps if x[1] == max_gaps[1]]
    selected = filtered[0]
    begin_index, length = selected

    middle_index = begin_index + ((length - 1) / 2)
    gaps.remove(selected)

    left_group_length = middle_index - begin_index
    if left_group_length:
        gaps.append((begin_index, left_group_length))

    right_group_length = (begin_index + length - 1) - middle_index
    if right_group_length:
        gaps.append((middle_index + 1, right_group_length))
    
    #print middle_index
    return middle_index


def solve(stalls, ppl):
    gaps = [(1, stalls)]
    for i in xrange(ppl):
        idx = add_man(gaps)
    
    gaps.sort(key=lambda x: x[0])
      
    smaller = larger = None
    for first_larger_idx, val in enumerate(gaps):
        if val[0] > idx:
            smaller = first_larger_idx - 1
            larger = first_larger_idx
            break

    if smaller is None or larger is None:
        return "0 0"

    distance_to_left = 0
    if smaller >= 0:
        last_available_smaller = gaps[smaller][0] + gaps[smaller][1] - 1
        if last_available_smaller + 1 < idx:
            distance_to_left = 0
        else:
            distance_to_left = gaps[smaller][1]

    distance_to_right = 0
    if larger < len(gaps):
        first_available_larger = gaps[larger][0]
        if first_available_larger - 1 > idx:
            distance_to_right = 0
        else:
            distance_to_right = gaps[larger][1]

    #print distance_to_left, distance_to_right

    return "{} {}".format(max(distance_to_left, distance_to_right),
                          min(distance_to_left, distance_to_right))


lock = threading.Lock()
running_threads = 0


def solve_thread(i, stalls, ppl, ret_dict, callback):
    global lock
    global running_threads
    lock.acquire()
    running_threads += 1
    lock.release()
    
    ret_dict[i] = solve(stalls, ppl)
    callback(i)


TNUM = 4


def main_threads():
    #print solve('-----', 5)
    #return
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    threads = []
    results = {}

    def run_next_thread(problem):
        global lock
        global running_threads

        lock.acquire()
        running_threads -= 1
        lock.release()

        if threads:
            thread = threads.pop(0)
            thread.start()
        else:
            lock.acquire()
            local_running = running_threads
            lock.release()

            if local_running == 0 and len(results) == t:
                for i in xrange(1, t + 1):
                    print "Case #{}: {} ".format(i, results[i])

    for i in xrange(1, t + 1):
        stalls, ppl = [int(f) for f in raw_input().split(" ")]
        threads.append(threading.Thread(target=solve_thread, args=(i, stalls, ppl, results, run_next_thread)))

    runthreads = []
    for _ in xrange(TNUM):
        if threads:
            runthreads.append(threads.pop(0))
    
    for thread in runthreads:
        thread.start()

if __name__ == '__main__':
    main_threads()
