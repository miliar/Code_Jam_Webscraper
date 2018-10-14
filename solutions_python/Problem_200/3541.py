
def find_next_tidy_reverse(number):
    while number > 0:
        if is_tidy(toArray(str(number))):
            return number
        number = number - 1
        

def toArray(str_number):
    output = []
    for char in str_number:
        output.append(char)
    return output

def is_tidy(array):
    #print sorted(array),array
    if sorted(array) == array:
        return True
    return False
    
f = open("B-small-attempt0.in")
w = open("output.txt",'w')
num_tests = int(f.readline())

count = 1
for line in f:
    output_prefix = "Case #" + str(count) + ": "
    number = long(line.strip())
    output = str(find_next_tidy_reverse(number))
    print output
    w.write(output_prefix + output + '\n')
    count += 1

w.close()
f.close()
