import sys


class Solution:
    def calculate_min(self, s, k):
        if self.check(s):
            return 0

        length = len(s)
        set_string = set()
        queue = [(0, s)]
        front_index = 0

        while front_index < len(queue):
            weight, s = queue[front_index]
            front_index += 1
            for generated_string in self.generate(s, k, length):
                if self.check(generated_string):
                    return weight + 1
                if generated_string not in set_string:
                    set_string.add(generated_string)
                    queue.append((weight + 1, generated_string))

        return "IMPOSSIBLE"

    def generate(self, s, k, length):
        result = []
        for i in range(length - k + 1):
            temp = ""
            for j in range(0, i):
                temp += s[j]

            for j in range(i, i + k):
                if s[j] == "-":
                    temp += "+"
                else:
                    temp += "-"

            for j in range(i + k, length):
                temp += s[j]

            result.append(temp)

        return result

    def check(self, generated_string):
        for c in generated_string:
            if c == '-':
                return False
        return True


# s = Solution()
# print s.calculate_min("---+-++-", 3)

t = int(raw_input())
for i in xrange(1, t + 1):
    s, k = [s for s in raw_input().split(" ")]
    solution = Solution()
    result = solution.calculate_min(s, int(k))
    print "Case #{}: {}".format(i, result)
