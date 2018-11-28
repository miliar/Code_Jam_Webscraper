import sys  

#f = open("input.txt", "r")

#f = open("A-small-attempt0.in", "r")
f = open("A-large.in", "r")

#sys.stdout = open('A-small-out.txt', 'w')
sys.stdout = open('A-large-out.txt', 'w')

t = int(f.readline().strip())

for case_num in range(1,t+1):
    input_line = f.readline().strip().split(" ")
    dest = int(input_line[0])
    num_horses = int(input_line[1])
    
    finish_time_list = []
    
    for horse_i in range(0,num_horses):
        input_line_i = f.readline().strip().split(" ")
        start_i = int(input_line_i[0])
        speed_i = int(input_line_i[1])
        finish_time_i = (dest - start_i) / speed_i
        finish_time_list.append(finish_time_i)
    
    #print(finish_time_list)
    #print(max(finish_time_list))
    ans = round(dest / max(finish_time_list),6)
    print ("Case #{}: {}".format(case_num, ans))