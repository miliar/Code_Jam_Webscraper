#!/usr/bin/env python
from __future__ import print_function
from exceptions import Exception
from collections import deque

def get_input():
    from sys import stdin
    input = stdin.readlines()
    return input[0], deque(input[1:])

def prepare_case(data):
    data = deque(data.split())
    recipes = {}
    recipes_size = int(data.popleft())
    for i in range(recipes_size):
        r = data.popleft()
        recipes[r[0:2]] = r[2]

    opposed = set()
    opposed_size = int(data.popleft())
    for i in range(opposed_size):
        opposed.add(data.popleft())
    data.popleft()

    elements_list = list(data.popleft())
    elements_list.reverse()
    return recipes, opposed, elements_list


def append(elements, element, recipes, opposed):
    if len(elements) == 0:
        elements.append(element)
    else:
        pair = element+elements[-1]
        final_elem = None
        try:
            final_elem = recipes[pair]
        except KeyError:
            try:
                final_elem = recipes[pair[::-1]]
            except KeyError:
                pass
        if final_elem:
            elements.pop()
            append(elements, final_elem, recipes, opposed)
            return
        else:
            for i in elements:
                if i+element in opposed or element+i in opposed:
                    del(elements[:])
                    return
        elements.append(element)
            

def invoke(recipes, opposed, elements_list):
    elements = []#[elements_list.pop()]
    while(len(elements_list) > 0):
        new_elem = elements_list.pop()
        append(elements, new_elem, recipes, opposed)
    return elements
                
            
if __name__ == "__main__":
    cases, data = get_input()

    for case in xrange(int(cases)):
        case += 1
        recipes, opposed, elements_list = prepare_case(data.popleft())
        elements = invoke(recipes, opposed, elements_list)
        print("Case #%d: [" % case, end=''),
        for i in range(len(elements)):
            print(elements[i].lstrip(), end='')
            if i < len(elements)-1:
                print(', ', end='')
        print(']')
