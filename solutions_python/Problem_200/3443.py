import time
import threading

def is_ascending(num):
    digits = [int(i) for i in str(num)]
    prev = digits[0]
    for i in xrange(len(digits) - 1):
        if digits[i + 1] < prev:
            return False
        prev = digits[i + 1]
    
    return True


def fix(num):
    digits = [i for i in str(num)]
    curr_start = len(digits) - 1
    while curr_start > 0:
        digit = digits[curr_start]
        if digit < digits[curr_start - 1]:
            bad_digit_idx = curr_start

            for j in xrange(bad_digit_idx - 1, -1, -1):
                if digit < digits[j]:
                    digits[j] = str(int(digits[j]) - 1)
                    for k in xrange(j + 1, len(digits)):
                        digits[k] = '9'
                    break

        curr_start -= 1
    return ''.join(digits)


def solve(n):
    start = time.time()
    #print n
    n = fix(n)
    #while not is_ascending(n):
    #    n -= 1
    #print n
    assert is_ascending(n)

    end = time.time()
    return n


lock = threading.Lock()
running_threads = 0


def solve_thread(i, n, ret_dict, callback):
    global lock
    global running_threads
    lock.acquire()
    running_threads += 1
    lock.release()
    
    ret_dict[i] = int(solve(n))
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
        n = int(raw_input())
        threads.append(threading.Thread(target=solve_thread, args=(i, n, results, run_next_thread)))

    runthreads = []
    for _ in xrange(TNUM):
        if threads:
            runthreads.append(threads.pop(0))
    
    for thread in runthreads:
        thread.start()

if __name__ == '__main__':
    main_threads()
