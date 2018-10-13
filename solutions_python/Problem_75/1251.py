#!/usr/bin/env python3 -tt
"""Google Code Jam 2011
Date: May 7, 2011
Round: Qualification
Problem: B-Magicka
Usage python3 magicka.py <infile >outfile
"""

import sys

def read_from_stdin():
    inputs = sys.stdin.readlines()
    T = int(inputs.pop(0))

    return (T, inputs)

def output_result(case, result):
    """Writes out the data in the expeted format.
    """
    out_string = "Case #{0}: {1}"
    print(out_string.format(case, result))

def solve_case(data_combines, data_opposes, data_string):
    combo_dict = {}
    for combination in data_combines:
        combo_dict[combination[0] + combination[1]] = combination[2]
        combo_dict[combination[1] + combination[0]] = combination[2]
    
    opp_dict = {}
    for combo in data_opposes:
        opp_dict[combo[0]] = combo[1]
        opp_dict[combo[1]] = combo[0]

    elements = []
    data_list = list(data_string)
    while data_list:
        element = data_list.pop(0)
        if not data_list:
            next_element = ""
        else:
            next_element = data_list[0];

        if element + next_element in combo_dict:
            elements.append(combo_dict[element + next_element])
            del(data_list[0])
        elif element in opp_dict:
            opposite = opp_dict[element]
            while data_list.count(opposite) > 0:
                pos = data_list.index(opp_dict[element])
                if pos > 0 and data_list[pos-1] + data_list[pos] in combo_dict:
                    data_list[pos-1] = combo_dict[data_list[pos-1] + data_list[pos]]
                    del(data_list[pos])
                else:
                    elements = []
                    del(data_list[:pos + 1])
                    break
            else:
                elements.append(element)
        else:
            elements.append(element)

    return str(elements).replace("'", "")
        

def main():
    T, inputs = read_from_stdin()
    
    for case in range(T):
        data = inputs[case].split()
        C = int(data.pop(0))
        
        data_combines = []
        for idx in range(C):
            data_combines.append(data.pop(0))
        
        D = int(data.pop(0))
        data_opposes = []
        for idx in range(D):
            data_opposes.append(data.pop(0)) 

        data_string = data.pop()

        output_result(case + 1, solve_case(data_combines, data_opposes, data_string))


if __name__ == '__main__':
    main()
    
