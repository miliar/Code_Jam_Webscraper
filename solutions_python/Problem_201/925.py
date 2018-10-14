import Queue

import datetime


class Solution:
    def find_min_max(self, n, k):
        number_appear = {n: 1}

        q = Queue.PriorityQueue()
        q.put(-n)
        min_value, max_value = 0, 0
        sum = 0
        while not q.empty():
            t = abs(q.get())
            number = number_appear.pop(t)
            sum += number


            if t <= 1:
                return 0, 0

            min_value = (t - 1) >> 1
            max_value = t - 1 - min_value

            if sum >= k: break

            if min_value > 0:
                self.put_element(q, number_appear, min_value, number)
            if max_value > 0:
                self.put_element(q, number_appear, max_value, number)

        return min_value, max_value

    def put_element(self, q, number_appear, value, number):
        temp_number = number_appear.get(value, 0)
        if number_appear.get(value) == None:
            q.put(-value)
        number_appear.update({value: number + temp_number})


# t1 = datetime.datetime.now()
# s = Solution()
# print s.find_min_max(1000000, 520000)
# #
# t2 = datetime.datetime.now()
# print  t2 - t1

t = int(raw_input())
for i in xrange(1, t + 1):
    ss = raw_input()
    n, k = [int(s) for s in ss.split(" ")]
    solution = Solution()
    min_value, max_value = solution.find_min_max(n, k)
    print "Case #{}: {} {}".format(i, max_value, min_value)
