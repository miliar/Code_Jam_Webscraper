#!env python

class Testcase:
    def __init__(self, s_max, audience):
        self.audience = audience
        self.s_max = s_max

    def solve(self):
        """ Returns the minimum number of friends to guarantee the standing ovation """
        invite_count = 0
        standing_count = 0
        for shyness, count in enumerate(self.audience):
            if shyness > (standing_count + invite_count):
                invite_count += shyness - standing_count - invite_count
            standing_count += int(count)
            # print("Shyness: {0}, Count: {1}, Standing: {2}, Inviting: {3}".format(shyness, int(count), standing_count, invite_count))
        return invite_count

def process_input():
    """Read, process input and returns a list of Testcases for them"""
    # Read number of test cases
    testcase_count = int(input())

    # Read testcase_count testcases
    testcases_list = []
    for i in range(0, testcase_count):
        s_max, audience = str(input()).split(' ', 2)
        testcases_list.append(Testcase(s_max, audience))
    return testcases_list

def main():
    testcases_list = process_input()
    for i, l in enumerate(testcases_list):
        print("Case #{0}: {1}".format(i+1, l.solve()))
        
main()
