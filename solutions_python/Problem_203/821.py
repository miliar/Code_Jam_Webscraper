# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:13:24 2017

@author: Trevor
"""

def solve(input_cells,rows,cols):
    answer_cells = input_cells
    r = 0
    c = 0
    set_chars = set()
    set_chars.update('?')
    current_char = ""
    while True:
        while input_cells[r][c] in set_chars:
            c = (c + 1) % cols
            if c == 0:
                r = r + 1
            if r == rows:
                answer_string = ""
                for row in answer_cells:
                    answer_string = answer_string + "\n"
                    for item in row:
                        answer_string = answer_string + item
                return answer_string
        current_char = input_cells[r][c]
        temp_r = r
        temp_c = c
        while True:
            if temp_r == -1:
                temp_r = 0
                break
            if answer_cells[temp_r][temp_c] not in ['?',current_char]:
                temp_r = temp_r + 1
                break
            temp_r = temp_r - 1 
        lower = temp_r
        breaking = False
        while True:
            if temp_c == -1:
                temp_c = 0
                break
            for i in xrange(lower,r+1):
                if answer_cells[i][temp_c] not in ['?',current_char]:
                    breaking = True
                    temp_c = temp_c + 1
                    break
            if breaking:
                break
            temp_c = temp_c -1
        left = temp_c
        temp_r = r
        temp_c = c
        breaking = False
        while True:
            if temp_r == rows:
                break
            for i in xrange(left,c+1):
                if answer_cells[temp_r][i] not in ['?',current_char]:
                    breaking = True
                    break
            if breaking:
                break
            temp_r = temp_r + 1
        upper = temp_r
        breaking = False
        while True:
            if temp_c == cols:
                break
            for i in xrange(lower,upper):
                if answer_cells[i][temp_c] not in ['?',current_char]:
                    breaking = True
                    break
            if breaking:
                break
            temp_c = temp_c + 1
        right = temp_c
        for row in xrange(lower,upper):
            for col in xrange(left,right):
                answer_cells[row][col] = current_char
        set_chars.add(current_char)
        r = 0
        c = 0

def run(filename):
    f = open(filename,"r")
    data = f.read()
    f.close()
    
    lines = data.splitlines()
    num_cases = int(lines[0])
    i = 1
    cases_run = 0
    answer_string = ""
    while cases_run < num_cases:
        line = lines[i]
        rows = int(line.split(' ')[0])
        cols = int(line.split(' ')[1])
        cells = [[] for j in xrange(0,rows)]
        for j in xrange(0,rows):
            i = i + 1
            cells[j] = [char for char in lines[i]]
        answer = solve(cells,rows,cols)
        cases_run = cases_run + 1
        answer_string = '{}Case #{}:{}\n'.format(answer_string,cases_run,answer)
        i = i + 1
    out_file = filename.split('.')[0] + "_out.txt"
    f = open(out_file,"w")
    f.write(answer_string)
    f.close()