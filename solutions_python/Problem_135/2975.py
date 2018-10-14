#!/usr/bin/env python

def get_chosen_card():
    first_choice = int(raw_input())
    first_row = set()
    for i in range(4):
        inp = raw_input()
        if i + 1 == first_choice: 
            first_row = set((map(int, inp.split())))
   
    second_choice = int(raw_input()) 
    second_row = set()
    for i in range(4):
        inp = raw_input()
        if i + 1 == second_choice:
            second_row = set((map(int, inp.split())))

    common_elem = first_row & second_row
    if len(common_elem) == 1:
        result = list(common_elem)[0]
    elif len(common_elem) > 1:
        result = 'Bad magician!'
    else:
        result = 'Volunteer cheated!'

    return result 

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        print 'Case #%d: %s' % (i + 1, get_chosen_card())
