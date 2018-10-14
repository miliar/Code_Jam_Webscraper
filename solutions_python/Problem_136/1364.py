'''
Created on Apr 11, 2014

@author: Andrew
'''


def solve_case(probe, minerals, gateway):
    new_minerals = 2
    total_time = 0
    while 1:
        probe_time = probe/new_minerals
        gateway_time = gateway/new_minerals
        new_minerals += minerals
        new_gateway_time = probe_time + (gateway/new_minerals)
        if gateway_time <= new_gateway_time:
            return (total_time + gateway_time)
        total_time += probe_time
            

def solve():        
    text = open("google.in", "r")
    test_cases = int(text.readline())
    total_cases = [[] for x in range(0,test_cases)]
    
    for x in range(0, test_cases):
        for i in text.readline().split():
            total_cases[x].append(float(i))
        
    text.close()
    
    solution = open("solution.txt", "w")
    number = 1
    for case in total_cases:
        answer = solve_case(case[0],case[1],case[2])
        solution.write("Case #" + str(number) + ": " + str(answer) + "\n")
        number += 1
    solution.close()
    
solve()