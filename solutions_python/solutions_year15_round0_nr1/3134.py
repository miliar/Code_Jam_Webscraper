#!/bin/python
#gcj standing-ovation


def main():
    testcases = int(raw_input())
    for case in xrange(1, testcases+1):
        standing_audience_count = 0
        invited_friends = 0
        individual_case = raw_input()
        splitted_shy = individual_case.split(' ')
        audience_shy = [int(x) for x in splitted_shy[1]]
        #core logic
        for index, value in enumerate(audience_shy):
            if(standing_audience_count >= index):
                standing_audience_count += value
            else:
                invited_friends += (index - standing_audience_count)
                standing_audience_count += (index - standing_audience_count)+value

        print "Case #%d:" % (case), invited_friends


if __name__ == "__main__":
    main()
