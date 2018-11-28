import sys  
import math

#f = open("input.txt", "r")

#f = open("A-small-attempt2.in", "r")
f = open("A-large.in", "r")

#sys.stdout = open('A-small-out.txt', 'w')
sys.stdout = open('A-large-out.txt', 'w')

t = int(f.readline().strip())

#print ("Case #{}: {}".format(case_num, result)

for case_num in range(1,t+1):    
    input_line = f.readline().strip().split(" ")
    num_avail = int(input_line[0])
    max_size = int(input_line[1])
    
    pancake_list = []
    
    for i in range(0, num_avail):
        line = f.readline().strip().split(" ")
        pancake_list.append((int(line[0]),int(line[1])))
    
    to_sort = []
    for elem in pancake_list:
        to_sort.append([elem[0],elem[1],elem[0]**2,2*elem[0]*elem[1]])
    
    answer_stack = []
    answer = 0
    #sort by side
    #to_sort.sort(key=lambda x: x[3], reverse=True)
    max_top_area = 0
    for i in range(0, max_size):
        max_next = 0
        #key = 0
        #find the best pancake to put on top
        for j in range(0, num_avail):
            if to_sort[j][2] > max_top_area:
                top_diff = to_sort[j][2] - max_top_area
            else:
                top_diff = 0
            if top_diff + to_sort[j][3] > max_next:
                max_next = top_diff + to_sort[j][3]
                key = j
        max_top_area = max(max_top_area,to_sort[key][2])
        answer += max_next
        answer_stack.append(to_sort[key])
        to_sort.pop(key)
        num_avail -= 1
    
    #print("Case #", case_num, max_top_area)    
    
    #print (answer)    
    #print (answer_stack)
    print ("Case #{}: {}".format(case_num, round(answer*math.pi,7)))
    
        