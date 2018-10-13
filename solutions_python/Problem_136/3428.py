'''
Created on 12 avr. 2014

Problem B

@author: belhassine
'''

def readFile(path):
    fh = open(path, "r")
    return fh.readlines()

def writeLinesToFile(lines,path):
    fh = open(path, "w")
    fh.writelines(lines)
    fh.close()


input_path = "D:/jam/2014/task2/test.in"
output_path = "D:/jam/2014/task2/test.out"
   
lines = readFile(input_path)
test_cases = int(lines[0])
results = [0 for l in range(test_cases)]



for index,current_line in enumerate(lines):
    if (index == 0): continue
    current_line_array = current_line.split(" ")
    C = float(current_line_array[0])
    F = float(current_line_array[1])
    X = float(current_line_array[2])
    Y = 0
    cookies_per_second = 2
    resolved = 0
    win_needed = 0
    next_win_needed = 0

    
    while(resolved != 1):
        win_needed = (X / cookies_per_second)
        next_rate = cookies_per_second + F
        next_win_needed =  X / next_rate
        buy_farm = (C / cookies_per_second)
        buy_farm_and_wait = buy_farm + next_win_needed
        if (buy_farm_and_wait < win_needed):
            cookies_per_second = next_rate
            Y += buy_farm
        else:
            resolved = 1
            Y += win_needed
    results[index-1] = str(round(Y,7))
    if (index-1 != test_cases -1):
        results[index-1] = results[index-1]+"\n"


writeLinesToFile(results, output_path)
    