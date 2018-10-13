#!/usr/bin/python 

from __future__ import division

def get_card_number (first_answer, first_arrangement, second_answer, second_arrangement):
    number_found = 0
    for number in first_arrangement [first_answer -1]:
        if number in second_arrangement [second_answer - 1]:
            output = number 
            number_found = number_found + 1
    if number_found == 0:
        output = "Volunteer cheated!"
    elif number_found > 1:
        output = "Bad magician!"
    return output

name='input'
fp_in = open (name, "r")
fp_out = open ('output.txt', "w")
lines = fp_in.readlines ()
no_of_lines = int (lines [0])
print "test cases need to be read ", no_of_lines
lines = lines [1:]

output = 1
input_size = 0
input_count = 0
while input_count < no_of_lines:
    first_answer = int (lines [input_size])
    first_arrangement = map (lambda x: x.split (),lines [input_size+1:input_size+5])
    second_answer = int (lines [input_size + 5])
    second_arrangement =  map (lambda x: x.split (), lines [input_size + 6:input_size+10])
    card = get_card_number (first_answer, first_arrangement, second_answer, second_arrangement)
    fp_out.write ("case #" + str(output) +": " + str (card))
    fp_out.write ("\n")
    output = output + 1
    input_count = input_count + 1
    input_size = input_count * 10

fp_in.close ()
fp_out.close ()
    



