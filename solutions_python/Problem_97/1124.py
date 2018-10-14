##text_obj = open("D:/desktop/recycled_test.txt", "wb+")
def count_number_of_digits(number):
    count = 0
    while(number != 0):
        number = number /10
        count = count + 1
    ##print count
    return (count)

test = raw_input()
test = int(test)
for i in range(1, test+1):
    big_list = []
    data = raw_input()
    data = data.rsplit(' ')
    low = int(data[0])
    count = count_number_of_digits(low)
    high = int(data[1])
    loop_counter = high - low
    answer = 0
    
    for k in range(0, loop_counter):
        ##print "*******TEST case %s" %(low + k)
        number = low + k
        new_number_list = []
        ##print "**** Number is %s" %number
        for j in range(1, count):
            ##print " &&& iterating for count %s" %j
            div_factor = 1
            for m in range(0, j):
                div_factor = div_factor*10
            part = number%(div_factor)
            ##print "**** Part of the Number is %s" %part
            mul_factor = 1
            

            for jh in range(j, count):
                mul_factor = mul_factor*10
            ##print "**** Mul factor is %s" %mul_factor
            ##print "**** Div factor is %s" %div_factor
            new_number = ((number - part)/div_factor) + part*mul_factor
            if new_number in new_number_list:
                pass
            else:
                new_number_list.append(new_number)
            
                ##print "New Number is %s" %new_number
                if new_number > number and (new_number <= high):
                    ##print "This case added"
##                    if new_number in new_number_list:
  ##                      pass
    ##                else:
                        answer = answer + 1
                        small_list = [number, new_number]
                        big_list.append(small_list)
                        ##text = "%s,%s\n" %(number, new_number)
                        ##text_obj.write(text)
                    
    print "Case #%s: %s" %(i, answer)
    
    
    ##text_obj.close()
                
            
            
            



        
