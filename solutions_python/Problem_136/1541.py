from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='Code Jam File Input handler')
parser.add_argument('file_name', metavar='file_name', type=str, help='File name to use as input')

def cfx( c, f, x ):
    rate      = 2.0
    time_cost_of_farm = c/rate
    print('Time cost of farm: %f'%time_cost_of_farm)
    time      = 0.0
    cookies   = 0.0
    while( (cookies < (x -c)) and ((x-c)>0)):
        time += c/rate
        print('Elapsed time: %f'%time)
        cookies += c
        print('Cookies: %f'%cookies)
        new_rate = rate + f
        print('New rate: %f'%new_rate)
        new_expected_time = time + x / new_rate
        current_expected_time =  time + (x - cookies) / rate
        print('New expected time: %f'%new_expected_time)
        print('Current expected time: %f'%current_expected_time)
        if new_expected_time < current_expected_time:
            cookies = 0
            rate    = new_rate
    if (x-c) > 0:
        time += (x-cookies)/rate
    else:
        time+= x/rate
    return time 

def solve( file_name ):
    with open(file_name,'r') as fh, open(file_name + '_solution.out', 'w') as fo:
        num_cases = int( fh.readline() )
        for case in xrange(num_cases):
            C,F,X = map(float, fh.readline().split() )
            print( 'Case #%d: %f'%(case+1, cfx(C,F,X) ), file=fo )


solve( parser.parse_args().file_name )
