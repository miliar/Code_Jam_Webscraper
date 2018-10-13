import threading
import Queue
import time
import sys
import math
def is_palindrom(number):
        if number < 10:
                return True
        str_num = str(number)
        str_rev = str_num[::-1]
        if str_num == str_rev:
                return True
        else:
                return False

test_cases = {}
task_queue = Queue.Queue()
test_count = 0
task_lock = threading.Lock()

def get_input(file_name):
        fl = open(file_name)
        lines = fl.readlines()
        global test_count
        global test_cases
        test_count = int(lines[0])
        for i in range(1, test_count+1):
                task_queue.put(i)
                lines[i] = lines[i].rstrip('\n')
                str_low, str_high = lines[i].split(" ")
                test_cases[i] = {'low': str_low, 'high': str_high}


class TestThread(threading.Thread):
        def __init__(self):
                threading.Thread.__init__(self)
                
        def run(self):
                while(True):
                        global task_queue
                        global test_cases
                        
                        if task_queue.empty():
                                break

                        test_id = task_queue.get()
                        test_case =  test_cases[test_id]
                        lm_low = int(test_case['low'])
                        lm_high = int(test_case['high'])

                        start = int(math.sqrt(lm_low))
                        if start ** 2 != lm_low:
                                start += 1
                        count = 0
                        while(True):
                                if is_palindrom(start):
                                        square = start ** 2
                                        if square > lm_high:
                                                break
                                        if is_palindrom(square):
                                                count += 1

                                start += 1

                        test_cases[test_id]['result'] = count
                        
thread_list = []
def run_threaded(thread_count):
        global thread_list
        for i in range(1, thread_count+1):
                thrd = TestThread()
                thrd.start()
                thrd.join()
                thread_list.append(thrd)

def main():
        file_name = sys.argv[1]
        get_input(file_name)

        run_threaded(1)
        global test_count
        global test_cases
        for i in range(1, test_count+1):
                test_case = test_cases[i]
                print "Case #%d: %d"%(i, test_case['result'])
        
        

if __name__ == '__main__':
        main()
