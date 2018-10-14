"""
Jonathan Simowitz

Google Code Jam 2014
Qualification Round
"""

from collections import defaultdict
import os


def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "A-small-attempt0.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    num_test_cases = int(rf.readline().strip())
    for test_num in range(1, num_test_cases + 1):
        counts = defaultdict(int)
        for i in range(2):
            chosen_row = int(rf.readline().strip())
            for j in range(4):
                row = rf.readline().strip()
                if j + 1 == chosen_row:
                    for value in row.split(' '):
                        counts[int(value)] += 1
        results = [key_ for key_, count in counts.items() if count == 2]
        if len(results) == 1:
            wf.write('Case #%s: %s\n' % (test_num, results[0]))
        elif len(results) > 1:
            wf.write('Case #%s: Bad magician!\n' % test_num)
        else:
            wf.write('Case #%s: Volunteer cheated!\n' % test_num)
    rf.close()
    wf.close()


main()
