import sys


class Solution:
    def genera(self, n, rr, o, yy, g, bb, v):
        t1 = [rr, 'R']
        t2 = [yy, 'Y']
        t3 = [bb, 'B']
        number = [[rr, 'R'], [yy, 'Y'], [bb, 'B']]

        for i in range(3):
            for j in range(i,3):
                if number[i][0] < number[j][0]:
                    temp = number[i]
                    number[i] = number[j]
                    number[j] = temp

        total = rr + yy + bb
        for i in range(3):
            if 2 * number[i][0] > total:
                return "IMPOSSIBLE"

        result = "T"
        for i in range(total):
            max_value = 0
            temp = 0
            for i in range(3):
                if max_value < number[i][0] and number[i][1] != result[-1]:
                    max_value = number[i][0]
                    temp = i

            result += number[temp][1]
            number[temp][0] -= 1

        words = list(result[1:])
        length = len(words)
        for i in range(o):
            for j in range(length):
                if words[j] == 'B':
                    words[j] = 'BOB'
                    break

        for i in range(g):
            for j in range(length):
                if words[j] == 'R':
                    words[j] = 'RGR'
                    break

        for i in range(v):
            for j in range(length):
                if words[j] == 'V':
                    words[j] = 'YVY'
                    break

        return "".join(words)

    def process(self, n, r, o, y, g, b, v):
        bb = b - o
        yy = y - v
        rr = r - g

        return self.genera(n, rr, o, yy, g, bb, v)


# INPUT_FILE_NAME = 'input.in'
INPUT_FILE_NAME = 'B-small-attempt1.in'
OUTOUT_FILE_NAME = 'b-small.out'

fi = open(INPUT_FILE_NAME, 'r')
fo = open(OUTOUT_FILE_NAME, 'w')

number_test = int(fi.readline())
for i in xrange(1, number_test + 1):
    n, r, o, y, g, b, v = [int(s) for s in fi.readline().split(" ")]

    solution = Solution()
    result = solution.process(n, r, o, y, g, b, v)

    print i
    fo.write("Case #%s: %s\n" % (i, result))

fi.close()
fo.close()
