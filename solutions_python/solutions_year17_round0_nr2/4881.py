import unittest
from collections import deque

def find_tidy(num):
    num = str(num)
    idx = 1
    tidy = True
    while idx < len(num):
        if num[idx] < num[idx-1]:
            tidy = False
            break
        idx += 1
    
    if tidy:
        return int(num)

    queue = deque([9 for _ in xrange(len(num) - idx)])    

    idx -= 1
    while idx >= 0:
        digit = int(num[idx])
        if digit == 1:
            if idx > 0:
                queue.appendleft(9)
        else:
            if idx > 0:
                if num[idx] == num[idx-1]:
                    queue.appendleft(9)
                else:
                    queue.appendleft(digit-1) 
                    for digit in num[:idx][::-1]:
                        queue.appendleft(int(digit))
                    break
            else:
                queue.appendleft(digit-1) 
        idx -= 1      
    
    return int(''.join([str(digit) for digit in list(queue)]))


class FindTidyTestCase(unittest.TestCase):
    
    def test(self):
        self.assertEquals(find_tidy(23300), 22999)
        self.assertEquals(find_tidy(132), 129) 
        self.assertEquals(find_tidy(1000), 999)
        self.assertEquals(find_tidy(7), 7)
        

def solve():
    with open('B-small-attempt0.in', 'r') as in_file, open('B-small-attempt0.out', 'w') as out_file:
        _ = in_file.readline()
        for case_num, case in enumerate(in_file.readlines()):
            result = find_tidy(int(case))
            out_file.write('Case #{0}: {1}\n'.format(int(case_num)+1, result))

if __name__ == '__main__':
    #unittest.main()
    solve()
    

 
    
    
