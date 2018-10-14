#! /usr/bin/env python

import pprint
import sys





if __name__ == "__main__":

    data = open(sys.argv[1])

    test_count = int(data.readline().strip())

    for count in range(0, test_count):
        number = data.readline().strip()
        #print number

        numbers_used = {}
        for char in number:
            if char == "0": continue
            if char in numbers_used:
                numbers_used[char]["count"] += 1
            else:
                numbers_used[char] = {"count": 1,
                                      "order": 0}

        ordered_numbers = ['0']
        ordered_numbers.extend(sorted(numbers_used.keys()))

        for counter, num in enumerate(ordered_numbers):
            if num == '0': continue
            numbers_used[num]["order"] = counter
        
        #pprint.pprint(numbers_used)

        valid = False
        while not valid:
            #add one


            carry = True
            number_count = {}
            next_number = ""
            for char in number[::-1]:
                #print "Running char: %s - %s" % (number, char)
                if carry:
                    order_index = 0
                    if char == '0':
                        order_index = 1
                    else:
                        order_index = numbers_used[char]["order"] + 1

                    if order_index >= len(ordered_numbers):
                        order_index = order_index % len(ordered_numbers)
                        carry = True
                    else:
                        carry = False


                    next_number = ordered_numbers[order_index] + next_number
                    if ordered_numbers[order_index] in number_count:
                        number_count[ordered_numbers[order_index]] += 1
                    else: 
                        number_count[ordered_numbers[order_index]] = 1

                else:
                    next_number = char + next_number
                    if char in number_count:
                        number_count[char] += 1
                    else: 
                        number_count[char] = 1

                #print "%s - %s, carry - %s" % (number, next_number, carry)
                #pprint.pprint(number_count)


            #print "Appending final carry"
            if carry:
                next_number = ordered_numbers[1] + next_number
                if ordered_numbers[1] in number_count:
                    number_count[ordered_numbers[1]] += 1
                else: 
                    number_count[ordered_numbers[1]] = 1
                
            number = next_number

            valid = True
            for char in ordered_numbers:
                if char == '0': continue
                if char in number_count:
                    #print "number test- %s : %s" % (number_count[char], numbers_used[char]["count"])
                    if number_count[char] != numbers_used[char]["count"]:
                        valid = False
                        break
                else:
                    valid = False
            
        
        print( "Case #%s: %s" % (count + 1, number ))
