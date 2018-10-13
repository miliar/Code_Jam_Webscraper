'''
Created on Apr 10, 2014

@author: Andrew
'''

def solve_case(first_guess,first_rows,second_guess,second_rows):
    matches = 0
    matched_value = 0
    first_row = first_rows[first_guess-1]
    second_row = second_rows[second_guess-1]
    for first_value in first_row:
        for second_value in second_row:
            if first_value == second_value:
                matched_value = first_value
                matches += 1
    if matches == 0:
        return "Volunteer cheated!"
    elif matches == 1:
        return str(matched_value)
    else:
        return "Bad magician!"
        

def solve():        
    text = open("google.in", "r")
    test_cases = int(text.readline())
    total_cases = [[] for x in range(0,test_cases)]
    
    for x in range(0, test_cases):
        
        total_cases[x].append(int(text.readline()))
        total_cases[x].append([])
        
        for row in range(0, 4):
            total_cases[x][1].append([int(i) for i in text.readline().split()])
            
        total_cases[x].append(int(text.readline()))
        total_cases[x].append([])
        
        for row in range(0, 4):
            total_cases[x][3].append([int(i) for i in text.readline().split()])
        
    text.close()
 
 
    solution = open("solution.txt", "w")
    number = 1
    for case in total_cases:
        answer = solve_case(case[0],case[1],case[2],case[3])
        solution.write("Case #" + str(number) + ": " + answer + "\n")
        number += 1
    solution.close()
    
solve()