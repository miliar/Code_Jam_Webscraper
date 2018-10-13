#!/usr/bin/python


#-----------------------------------------------------

#-----------------------------------------------------
    
fin = open("horses_sample.txt", "r+")
number_of_test_cases = int(fin.readline()) ;
print("Number of test cases: ", number_of_test_cases)

fout = open('horses_output.txt', 'w')

for x in range(0, number_of_test_cases):
    string = fin.readline().rstrip('\n')
    
    parts   = string.split()
    distance= int(parts[0])
    horses  = int(parts[1])
    maxtime = -1

    print("Distance: ", distance, " Horse: ", horses)
    
    for h in range(0, horses):
        hstring  = fin.readline().rstrip('\n')
        hparts   = hstring.split()
        hlocation= int(hparts[0])
        hspeed   = int(hparts[1])
        htime    = (distance - hlocation)/hspeed

        print(h,"th horse, location: ", hlocation, " speed: ", hspeed,
              " time: ", htime)
        if (htime > maxtime):
            maxtime = htime

    alicespeed = distance/maxtime
    output_string = 'Case #' + str(x+1) + ": " + str(alicespeed) + "\n" 
    print(output_string)
    fout.write(output_string)
    
fout.close()
fin.close()

