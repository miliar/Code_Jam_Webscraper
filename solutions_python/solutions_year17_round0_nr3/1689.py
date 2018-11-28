import math
import heapq

def read_file(file_name):
    f = open(file_name, 'r')
    first_line = f.readline()
    return_str = ""
    for i in range(0, int(first_line)):
        number = f.readline().split(' ')
        answer = get_final_order(int(number[0]), int(number[1]))
        return_str += 'Case #'+str(i+1)+': '+str(answer[0]) + ' '+str(answer[1])
        return_str += '\n'

    return return_str


def get_final_order(n,k):
    list =[n*-1]
    heapq.heapify(list)
    return get_partition(n,k,list)

def get_partition(n,k, partitions):
    maximum = 0
    for i in range(0,k):
        maximum = heapq.heappop(partitions)
        if maximum % 2 == 0:
            heapq.heappush(partitions, maximum/2)
            heapq.heappush(partitions, (maximum/2 + 1))
        else:
            heapq.heappush(partitions, maximum / 2 + 1)
            heapq.heappush(partitions, maximum / 2 + 1)

    if maximum % 2 == 0:
        return [(maximum/2) * -1, (maximum/2 + 1) * -1]
    else:
        return [(maximum/2 + 1) * -1, (maximum/2 + 1) * -1]
    #     if(max(n[0],n[1]) % 2 == 0):
    #         if (n[0] < n[1]):
    #             n[1] = n[1]/2
    #         else:
    #             n[0] = n[0]/2
    #     else:
    #         if (n[0] < n[1]):
    #             n[1] = n[1]/2 + 1
    #         else:
    #             n[0] = n[0]/2 + 1
    # if n[0] > n[1]:
    #     if n[1] % 2 == 0:
    #         return [n[1], n[1]]
    #     else:
    #         return [n[1] - 1, n[1]]
    # else:
    #     if n[0] % 2 == 0:
    #         return [n[0], n[0]]
    #     else:
    #         return [n[0], n[0] - 1]
    # if n[0] > n[1]:
    #     if n[1] % 2 == 0:
    #         return [n[1] / 2, n[1] / 2 - 1]
    #     else:
    #         return [n[1] / 2, n[1] / 2]
    # else:
    #     if n[0] % 2 == 0:
    #         return [n[0] / 2, n[0] / 2 - 1]
    #     else:
    #         return [n[0] / 2, n[0] / 2]

def partition(n,k,i):
    if i == k:
        if n/2 == 0:
            return [0,0]
        else:
            if n%2 != 0:
                return[n/2,n/2]
            else:
                return [n/2, n/2 - 1]
    elif i > k:
        return None
    else:
        if n%2 ==0:
            x = partition(n/2 - 1,k,2*i)
            y = partition(n/2 - 1,k,(2*i)+1)
        else:
            x = partition(n/2,k,2*i)
            y = partition(n/2-1,k,(2*i)+1)
        if x is None:
            return y
        else:
            return x



output = read_file('C-small-2-attempt1.in')
output_file = open('output.txt', 'w')
output_file.write(output)
output_file.close()