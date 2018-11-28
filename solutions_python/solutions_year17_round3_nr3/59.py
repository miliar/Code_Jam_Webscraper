import sys

EPS = .0000001

def best_prob(cores, trains, num_des):
    cores.sort()
    while trains > EPS:
        print(cores)
        print(trains)
        min_size = cores[0]
        if min_size > 1 - EPS:
            break
        num_updates = len(cores)
        next_size = 1
        for index in range(len(cores)):
            if cores[index] > min_size + EPS:
                num_updates = index
                next_size = cores[index]
                break
        cost = num_updates * (next_size - min_size)        
        
        if cost < trains:
            trains -= cost
        else:
            next_size = min_size + trains / num_updates
            trains = 0
        
        for index in range(num_updates):
            cores[index] = next_size
            
    ret = 1
    print(cores)
    for core in cores:
        ret *= core
    return ret
        
    
def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        num_cores, num_des = (int(val) for val in in_file.readline().strip().split())
        
        trains = float(in_file.readline().strip())
        
        cores = [float(val) for val in in_file.readline().strip().split()]
        
       
        sol = best_prob(cores, trains, num_des)
        out_file.write("Case #{}: {}\n".format(case, sol))        
       
if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'C-sample'
        name = 'C-small-1-attempt0'
        #name = 'C-large-practice'
        file_input = open(path + name + '.in', 'r')
        out_full_name = path + name +'.out'
        if alt_out:
            out_full_name = path + name + "naive" +'.out'            
        file_output = open(out_full_name,'w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        
        
def test():
    q = PriorityQueue()
    q.push('n', 5)
    q.push('i', 4)
    q._swap(0, 1)
    q._swap(0, 1)
    q.push('R', 1)
    q.push('o', 2)
    q.push('b', 3)
    print(q.items)
    print(q.indices)
    q.change_priority('R', 10)
    print(q.items)
    print(q.indices)
    q.decrease_priority('n', 3)
    q.decrease_priority('n', 10)
    print(q.items)
    print(q.indices)
    for _ in range(5):
        print(q.pop())

    print(q.items)
    print(q.indices)    

#test()