"""
Jonathan Simowitz

Google Code Jam 2014
Qualification Round
"""

import os


def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "B-large.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    num_test_cases = int(rf.readline().strip())
    for test_num in range(1, num_test_cases + 1):
        row = rf.readline().strip().split(' ')
        cookie_rate = 2.0  # 2 cookies per second
        seconds = 0.0      # begin at 0 seconds
        C = float(row[0])  # cost to buy a cookie farm
        F = float(row[1])  # cookies/second the farms produce
        X = float(row[2])  # number of cookies needed to win

        # 2 options, wait to win or wait to buy a farm
        while True:
            time_to_win = X / cookie_rate
            time_to_win_with_farm = C / cookie_rate + X / (cookie_rate + F)
            if time_to_win <= time_to_win_with_farm:
                # end condition
                seconds += time_to_win
                break
            else:
                # buy a farm and repeat
                seconds += C / cookie_rate
                cookie_rate += F
        wf.write('Case #%s: %.7f\n' % (test_num, seconds))
    rf.close()
    wf.close()

main()
