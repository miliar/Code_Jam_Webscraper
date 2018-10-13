text_file = open("B_input.txt", "r")
out_file = open("out.txt", "w")
out_file.write('')
out_file.close()
out_file = open("out.txt", "a")
input_text = text_file.readlines()
run_amount = int(input_text[0])
for x in range(1, run_amount+1):
    data = input_text[x].split(" ")
    number_of_googlers = data[0]
    surprising_triplets = int(data[1])
    critera = int(data[2])
    total_scores = data[3:]
    amount = 0
    for number in total_scores:
        number = int(number)
        divider = number/3
        remainder = number-critera
        method1 = remainder-(2*abs(critera-1))
        if critera == 0 and number >= 0:
            amount += 1
        else:
            if method1 >= 0:
                #out_file.write("Method 1")
                amount += 1
            else:
                method2 = remainder-abs(critera-2)-abs(critera-2)
                if surprising_triplets > 0:
                    if method2 >= 0:
                        #out_file.write("Method 2\t" + str(remainder) + "\t" + str(method2))
                        amount += 1
                        surprising_triplets -= 1
    out_file.write("Case #" + str(x)+ ": " + str(amount) + "\n")
text_file.close()
out_file.close()
