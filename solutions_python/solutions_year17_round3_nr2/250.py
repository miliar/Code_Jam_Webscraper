import sys


class Solution:
    def process(self, m, n, time1, time2):
        time1.sort()
        time2.sort()

        while True:
            min_time1, time1_temp = self.find_min_time(time1)
            if min_time1 == None:
                min_time1, time1_temp = self.find_min_time2(time1)

            min_time2, time2_temp = self.find_min_time(time2)
            if min_time2 == None:
                min_time2, time2_temp = self.find_min_time2(time2)

            if min_time1 != None and min_time2 != None:
                if min_time1 > min_time2:
                    time2 = time2_temp
                else:
                    time1 = time1_temp
            elif min_time1 != None:
                time1 = time1_temp
            elif min_time2 != None:
                time2 = time2_temp
            else:
                break

        time1.extend(time2)
        time1.sort()

        result = 0
        length = len(time1)
        for i in range(length):
            next = (i + 1) % length
            if time1[i][2] != time1[next][2]:
                result += 1
            else:
                result += 2

        return result

    def calculate_time(self, start, end):
        if end > start:
            return end - start
        else:
            return end + 1440 - start


    def find_min_time(self, time):
        length = len(time)
        if length <= 1:
            return None, time

        min_time = sys.maxint
        min_index = None
        for i in range(length):
            next = (i + 1) % length
            if min_time > self.calculate_time(time[i][1], time[next][0]):
                min_time = self.calculate_time(time[i][1], time[next][0])
                min_index = i

        time_temp = []
        if min_index == length - 1:
            start_index = 1
        else:
            start_index = 0

        for i in range(start_index, min_index):
            time_temp.append(time[i])

        next = (min_index + 1) % length
        time_temp.append((time[min_index][0], time[next][1], time[min_index][2]))

        if min_index == length - 1:
            end = length - 1
        else:
            end = length

        for i in range(next + 1, end):
            time_temp.append(time[i])

        total = 0
        for start, end, type in time_temp:
            total += self.calculate_time(start, end)

        if total > 720:
            return None, 0

        return min_time, time_temp

    def find_min_time2(self, time):
        length = len(time)
        if length <= 1:
            return None, time

        min_time = sys.maxint
        min_index = None
        for i in range(length):
            next = (i + 1) % length
            if min_time > self.calculate_time(time[i][0], time[next][1]):
                min_time = self.calculate_time(time[i][0], time[next][1])
                min_index = i

        time_temp = []
        if min_index == length - 1:
            start_index = 1
        else:
            start_index = 0

        for i in range(start_index, min_index):
            time_temp.append(time[i])

        next = (min_index + 1) % length
        time_temp.append((time[min_index][0], time[next][1], time[min_index][2]))

        if min_index == length - 1:
            end = length - 1
        else:
            end = length

        for i in range(next + 1, end):
            time_temp.append(time[i])

        total = 0
        for start, end, type in time_temp:
            total += self.calculate_time(start, end)

        if total > 720:
            return None, 0

        return min_time, time_temp


# INPUT_FILE_NAME = 'input.in'
INPUT_FILE_NAME = 'B-small-attempt1.in'
OUTOUT_FILE_NAME = 'b-small.out'

fi = open(INPUT_FILE_NAME, 'r')
fo = open(OUTOUT_FILE_NAME, 'w')

number_test = int(fi.readline())
for t in xrange(1, number_test + 1):
    print t
    m, n = [int(s) for s in fi.readline().split(" ")]
    time1 = []
    time2 = []

    for i in range(m):
        start, end = [int(s) for s in fi.readline().split(" ")]
        time1.append((start, end, 0))

    for i in range(n):
        start, end = [int(s) for s in fi.readline().split(" ")]
        time2.append((start, end, 1))

    result = Solution().process(m, n, time1, time2)
    print t, " ", result

    fo.write("Case #%s: %s\n" % (t, result))

fi.close()
fo.close()
