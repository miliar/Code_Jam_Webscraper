# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:31:02 2017

@author: Ameet
"""
import decimal

from math import floor, ceil
import decimal

def get_horse_speed(D, N, horses):
    assert(len(horses)>0)
    assert(N>0)
    assert(D>0)
    assert(len(horses)==N)
    times = [decimal.Decimal(D-horse[0])/decimal.Decimal(horse[1]) for horse in horses]
    max_time = max(times)
    return decimal.Decimal(D)/max_time

def test_get_horse_speed():
    D=2525
    horses = [(2400,5)]
    assert(get_horse_speed(D, len(horses), horses)==101)
    D=300
    horses = [(120,60),(60,90)]
    assert(get_horse_speed(D, len(horses), horses)==100)
    D=100
    horses = [(80,100), (70,10)]
    assert(get_horse_speed(D, len(horses), horses)==100/3)
        

def run_sample(input_filename, output_filename, func):
    input_file = open(input_filename, 'r')
    num_tests_line = input_file.readline()
    num_tests = int(num_tests_line)
    test_number = 1
    output_file = open(output_filename, 'w')
    for test_no in range(num_tests):
        header_row = input_file.readline()
        [D,N] = header_row.split(" ")
        N = int(N)
        D = int(D)
        horses = []
        for horse_num in range(N):
            horse_line = input_file.readline()
            K, S = horse_line.split(" ")
            horses.append((int(K),int(S)))
        output = func(D, N, horses)
        output_file.write("Case #")
        output_file.write(str(test_number))
        output_file.write(": ")
        output_file.write(str(output))
        output_file.write("\n")
        test_number += 1