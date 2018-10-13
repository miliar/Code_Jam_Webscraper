#!/usr/bin/env python3

import argparse
import logging
import math
import sys


DESC = '''Google Code Jam
Qualification Round 2017
Problem C. Bathroom Stalls
'''

USAGE = '''python {} < input_file.txt > output_file.txt 
   (see https://code.google.com/codejam/resources/quickstart-guide#io-tutorial)'''.format(__file__)

logger = logging.getLogger()

def parse_arguments():
    parser = argparse.ArgumentParser(description=DESC, usage=USAGE, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-v', '--verbose', action='store_true', help='Display debugging information')
    return parser.parse_args()

def problem_cases():
    num_cases_total = -1
    num_cases_passed = 0
    
    for count, line in enumerate(sys.stdin):
        line = line.rstrip()
        
        if count == 0:
            num_cases_total = int(line)
            logger.debug('{} cases in total.'.format(num_cases_total))
            continue
        
        logging.debug('Case #{} {}'.format(count, line))
        num_stalls, num_people = list(map(int, line.split(' ')))
        num_cases_passed += 1

        yield (count, num_stalls, num_people)
    
    assert num_cases_passed == num_cases_total
    


def solve(num_stalls, num_people):
    
    turns_needed = math.floor(math.log(num_people, 2))
    logger.debug('Will sit after turn {}'.format(turns_needed))
    num_people_present = 0
    num_people_left = num_people
    counts = {num_stalls: 1}

    for turn in range(1, turns_needed+1):
        current_sizes = list(counts.keys())
        
        if len(current_sizes) == 1:
            only_size = current_sizes[0]

            new_counts = { math.floor((only_size - 1) / 2): 0, math.ceil((only_size - 1) / 2): 0 }

            new_counts[ math.floor((only_size - 1) / 2) ] += counts[only_size]
            new_counts[ math.ceil((only_size - 1) / 2) ] += counts[only_size]
        else:
            small, big = sorted(current_sizes)
                
            new_counts = { math.floor((small - 1) / 2): 0, math.ceil((big - 1) / 2): 0 }

            new_counts[ math.floor((small - 1) / 2) ] += counts[small]
            new_counts[ math.ceil((small - 1) / 2) ] += counts[small]
            new_counts[ math.floor((big - 1) / 2) ] += counts[big]
            new_counts[ math.ceil((big - 1) / 2) ] += counts[big]

        counts = new_counts
        num_people_present = int(math.pow(2, turn) - 1)
        num_people_left = num_people - num_people_present
        msg = ', '.join(['{} areas of size {}'.format(n, s) for (s, n) in counts.items()])
        logger.debug('After turn {}: {} ({} people present, {} left)'.format(turn, msg, num_people_present, num_people_left))

    num_people_left = num_people - num_people_present
    current_sizes = list(counts.keys())
    
    if len(current_sizes) == 1:
        final_area_size = current_sizes[0]
    else:
        small, big = sorted(current_sizes)
        if num_people_left <= counts[big]:
            final_area_size = big
        else:
            final_area_size = small

    
    logger.debug('Will sit in an area of size {}'.format(final_area_size))
    
    if final_area_size == 1:
        return 0, 0

    solution = math.ceil((final_area_size - 1)/2), math.floor((final_area_size - 1) / 2)
    return solution
            
if __name__ == '__main__':
    args = parse_arguments()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format='CJ17.QR.C %(levelname)s %(message)s')

    for case_id, num_stalls, num_people in problem_cases():
        # print('case {} - N={} K={}'.format(case_id, num_stalls, num_people))
        solution = solve(num_stalls, num_people)
        solution_output = ' '.join(map(str, solution))
        print('Case #{}: {}'.format(case_id, solution_output))
        

