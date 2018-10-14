def number_hunter(lower,upper,event):
    total_found = 0
    for item in range(lower,upper+1):
        if len(str(item)) == 1:
            pass
        elif len(str(item)) == 2: #Two digit number TWO DIGITS WORKS
            new_item = str(item)[1] + str(item)[0] #Reversing the number
            new_item = int(new_item) #Turning back to number
            if new_item > item and new_item < upper and str(new_item)[0] != '0':
                total_found += 1
        elif len(str(item)) == 3: #Three digit number
            first_item = str(item)[1] + str(item)[2] + str(item)[0]
            if first_item[0] == '0':
                first_item = None
            first_item = int(first_item) if first_item != None else None #Back to int
            second_item = str(item)[2] + str(item)[0] + str(item)[1]
            if second_item[0] == '0':
                second_item = None
            second_item = int(second_item) if second_item != None else None #Back to int
            if first_item > item and first_item <= upper and first_item != 0:
                total_found += 1
            if second_item > item and second_item <= upper and first_item != 0:
                total_found += 1
                
    return 'Case #' + str(event) + ': ' + str(total_found)

data = open('input.in', 'r')
data = data.readlines()

new_data = []
for item in data[1:-1]: #Reference from 1 to lose the first line
    new_data.append(item[:-1].split()) #Reference to lose the \n and split the inputs
new_data.append(data[-1].split()) #Add the last one as it will cut off the last character otherwise

out = open('output.out', 'w')
event = 1
for item in new_data:
    x =number_hunter(int(item[0]),int(item[1]),event) + '\n'
    out.write(x)
    event += 1

out.close()