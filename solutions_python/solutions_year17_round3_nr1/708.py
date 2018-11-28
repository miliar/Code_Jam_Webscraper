# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:31:02 2017

@author: Ameet
"""
import decimal


import decimal
import math
import itertools

def get_surface_area(pancakes):
    side_area = sum([2*decimal.Decimal(math.pi)*p[0]*p[1] for p in pancakes])
    max_r = max([p[0] for p in pancakes])
    top_areas = decimal.Decimal(math.pi)*decimal.Decimal(max_r)**2
    #print(pancakes,side_area + top_areas)
    
    return side_area + top_areas

def get_best_stack_exhaustive(N, K, pancakes):
    best_area = 0
    for comb in itertools.combinations(pancakes, r=K):
        sa = get_surface_area(comb)
        if sa>best_area:
            best_area = sa
    
    return best_area


def get_best_stack(N, K, pancakes):
    assert(len(pancakes)>0)
    assert(N>0)
    assert(K>0)
    assert(len(pancakes)==N)
    
    
    max_surface_area = decimal.Decimal(0)

    counter = 0    
    for pancake in pancakes:
        top_area = decimal.Decimal(math.pi)*pancake[0]**2
        side_area = 2*decimal.Decimal(math.pi)*pancake[0]*pancake[1]
        side_surface_areas = [2*decimal.Decimal(math.pi)*pancakes[i][0]*pancakes[i][1] for i in range(N) if pancakes[i][0]<=pancake[0] and i!=counter]
        side_areas_used = sum(sorted(side_surface_areas,reverse=True)[:K-1])
        total_area = decimal.Decimal(top_area) + decimal.Decimal(side_area) + decimal.Decimal(side_areas_used)
        if total_area>max_surface_area:
            max_surface_area = total_area
        
    
    return max_surface_area

def test_get_best_stack():
    N=2
    K=1
    pancakes = [(100,20),(200,10)]
    assert(abs(get_best_stack(N,K,pancakes)-decimal.Decimal(138230.076757951))<decimal.Decimal(0.000001))
    N=2
    K=2
    pancakes = [(100,20),(200,10)]
    assert(abs(get_best_stack(N,K,pancakes)-decimal.Decimal(150796.447372310))<decimal.Decimal(0.000001))
    N=3
    K=2
    pancakes = [(100,10),(100,10),(100,10)]
    assert(abs(get_best_stack(N,K,pancakes)-decimal.Decimal(43982.297150257))<decimal.Decimal(0.000001))
    N=4
    K=2
    pancakes = [(9,3),(7,1),(10,1),(8,4)]
    assert(abs(get_best_stack(N,K,pancakes)-decimal.Decimal(625.176938064))<decimal.Decimal(0.000001))

def run_sample(input_filename, output_filename, func):
    input_file = open(input_filename, 'r')
    num_tests_line = input_file.readline()
    num_tests = int(num_tests_line)
    test_number = 1
    output_file = open(output_filename, 'w')
    for test_no in range(num_tests):
        header_row = input_file.readline()
        [N,K] = header_row.split(" ")
        N = int(N)
        K = int(K)
        pancakes = []
        for pancake in range(N):
            horse_line = input_file.readline()
            R, H = horse_line.split(" ")
            pancakes.append((int(R),int(H)))
        output = func(N, K, pancakes)
        output_file.write("Case #")
        output_file.write(str(test_number))
        output_file.write(": ")
        output_file.write(str(output))
        output_file.write("\n")
        test_number += 1