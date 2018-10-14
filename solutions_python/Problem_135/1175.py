_file = ""
with open("A-small-attempt1.in", "r") as inputfile:
    _file = inputfile.read()


file_row = _file.split("\n")
batch_size = int(file_row[0])
file_row = file_row[1:]

all_data = []

for batch in range(int(batch_size)):
    curr_batch = file_row[batch*10:batch*10+10]
    all_data.append(curr_batch)


output = []

for data in all_data:
    nums = {} 
    row_idx1 = int(data[0])
    row_idx2 = int(data[5])

    row1 = data[row_idx1].split()
    row2 = data[row_idx2+5].split()
        
    for i in range(len(row1)):
        if row1[i] in nums:
            nums[row1[i]] += 1;
        else:
            nums[row1[i]] =1 

        if row2[i] in nums:
            nums[row2[i]] += 1;
        else:
            nums[row2[i]] =1 
    
    most_freq_num = None 
    curr_output = "Volunteer cheated!"
    for num, freq in nums.items():
        if freq > 1 and not most_freq_num:
            most_freq_num = num
            curr_output = str(num)
        elif freq > 1 and most_freq_num:
            curr_output = "Bad magician!"
            break

    output.append(curr_output)


with open("output.txt", "w+") as output_file:
    for i in range(len(output)):
        output_file.write("Case #{0:}: {1:}\n".format(i+1, output[i])) 





