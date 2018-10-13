"""
Input
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

Output
Case #1: 6
Case #2: 100
Case #3: 4
"""

import sys, datetime

def main(input):
    results = []
    with open(input, "r") as f:
        T = int(f.readline())
        while T:
            result = ""
            steps = f.readline().split()
            move = iter(steps)
            N = int(move.next())
            button = {"O": 1, "B": 1}
            total_time = {"O": 0, "B": 0}
            for i in range(N):
                R = move.next()
                P = int(move.next())
                previous_button = button[R]
                button[R] = P
                time = abs(P - previous_button) + 1
                total_time[R] += time
                if R == "O":
                    compare_time = total_time["B"]
                else:
                    compare_time = total_time["O"]
                if total_time[R] <= compare_time:
                    total_time[R] = compare_time + 1
                result = total_time[R]
            results.append(result)
            T -= 1
    return results

if __name__ == "__main__":
    try:
        start = datetime.datetime.now()
        file_name = sys.argv[1]
        input = file_name + ".in"
        results = main(input)
        output = open(file_name + ".out", "w")
        for case, result in enumerate(results):
            output.write("Case #{0}: {1}\n".format(case + 1, result))
            output.flush()
        output.close()
        print "Time: {0}".format(datetime.datetime.now() - start)
    except Exception, e:
        print e
