count = 0
t = 0

read_file = open('test.in.large', 'r')
write_file = open('result.txt.large', 'w')

def get_tidy_number(num_str):
    if len(num_str) <= 1:
        return num_str
    else:
        while(True):
            is_tidy, num_str = function(num_str)
            if is_tidy:
                return num_str
            else:
                num_str = int(num_str) - 1
                num_str = str(num_str)

def function(num_str):
    #print num_str
    num_list = []
    maximum = 0
    for num in num_str:
        num_list.append(int(num))
    for idx in range(0, len(num_list)):
        #print idx
        if maximum <= num_list[idx]:
            maximum = num_list[idx]
        else:
            first_half_num = num_str[:idx]
            second_half_num = ''
            for num in num_str[idx:]:
                second_half_num += '0'
            num_str = first_half_num + second_half_num
            return False, num_str
    #print 'reached'
    return True, num_str

for line in read_file:
    if count == 0:
        t = int(line.strip())
    else:
        num = line.strip()
        tidy_number = get_tidy_number(num)
        if count != t:
            write_file.write("Case #" + str(count) + ': ' + str(tidy_number) + '\n')
        else:
            write_file.write("Case #" + str(count) + ': ' + str(tidy_number))
    count += 1