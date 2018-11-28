#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import math


def process(plates):
    
    plates= sorted(plates, reverse=True)
    max_pancakes = plates[0]
    res = max_pancakes  # best effort: no special minutes
    
    for nb_pancakes in range(2, max_pancakes):
        split_cost = 0
        for plate in plates:
            if plate < nb_pancakes:
                break  # plates are sorted
            # cost to split a plate of $plate pancakes into n plates of $nb_pancakes pancakes
            # $plate/n = $nb_pancakes => n = $plate/$nb_pancakes
            split_cost += math.ceil(plate/nb_pancakes) - 1
        if nb_pancakes + split_cost < res:  # nb_pancakes is the maximum number of pancakes in a plate
            res = nb_pancakes + split_cost

    return res
                


def infinite_house_of_pancakes(path):

    with open(path) as f:
        content = f.readlines()
    t = int(content[0].replace("\n", ""))
    for i in range(1, t+1):
        plates = [int(k) for k in content[2*i].replace("\n", "").split(" ")]
        number_of_minutes = process(plates)
        print("Case #{}: {}".format(i, number_of_minutes))
            
                
        




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <path_to_input_file>")
    else:
        infinite_house_of_pancakes(sys.argv[1])
