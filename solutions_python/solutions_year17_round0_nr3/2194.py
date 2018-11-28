import sys  
from heapq import heappush, heappop

#f = open("inputfile", "r")
f = open("C-small-2-attempt0.in", "r")
#f = open("C-large.in", "r")
t = int(f.readline().strip())

sys.stdout = open('C-small-out.txt', 'w')
#sys.stdout = open('C-large-out.txt', 'w')


for case_num in range(1,t+1):
    input_line = f.readline().strip().split(" ")
    num_stalls = int(input_line[0])
    num_people = int(input_line[1])

    #print ("Input #", case_num, ":", num_stalls, num_people)

    queue = []
    heappush(queue, -num_stalls)

    while(num_people > 0):
        #print (queue)
        space = -heappop(queue)
        #print (space)
        if space % 2 == 0:
            append1 = int((space-1)/2)+1
            append2 = int((space-1)/2)
        else:
            append1 = int((space-1)/2)
            append2 = int((space-1)/2)

        heappush(queue,-append1)
        heappush(queue,-append2)
        #last person, select answer
        if num_people == 1:
             print ("Case #{}: {} {}".format(case_num, append1, append2))  
             break        
        #otherwise, set up for next iteration
        num_people = num_people - 1;


'''
for case_num in range(1,t+1):
    input_line = f.readline().strip().split(" ")
    num_stalls = int(input_line[0])
    num_people = int(input_line[1])

    queue = []
    queue.append(num_stalls)

    while(num_people > 0):
        space = queue.pop()
        if space % 2 == 0:
            append1 = int((space-1)/2)+1
            append2 = int((space-1)/2)
        else:
            append1 = int((space-1)/2)
            append2 = int((space-1)/2)
        queue.append(append1)
        queue.append(append2)
        #last person, select answer
        if num_people == 1:
             print ("Case #{}: {} {}".format(case_num, append1, append2))  
             break        
        #otherwise, set up for next iteration
        queue.sort()
        num_people = num_people - 1;
'''
        

