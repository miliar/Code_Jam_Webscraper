def lastNumTidy(num):
    last_num = 9
    curr_num = num
    if curr_num < last_num:
        last_num = curr_num
    else:
        while curr_num > last_num:
            if IsNonDecreasing(curr_num):
                last_num = curr_num
            curr_num -= 1
    return str(last_num)
    

def IsNonDecreasing(num):
    num_str = str(num)
    nonDecreasing = True
    i = 0
    length_num = len(num_str)
    while (i <length_num-1):
        if int(num_str[i]) > int(num_str[i+1]):
            i = length_num
            nonDecreasing = False
        i += 1
    return nonDecreasing

def readFile(filepath):
    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()
    return lines

def main(filepath, output_path):
    lines = readFile(filepath)
    num_outputs = int(lines[0])
    to_it = lines[1:]
    outputs = []
    for i in range(num_outputs):
        curr_last_num = lastNumTidy(int(to_it[i].strip('\n')))
        curr_out = "Case #"+str(i+1)+": "+curr_last_num+"\n"
        outputs.append(curr_out)
    f = open(output_path, 'w')
    f.writelines(outputs)
    f.close()

if __name__ == '__main__':
    main("B-small-attempt0.in","output_file.txt")
    print('done')
    
