
with open('A-large.in') as input, open('out.txt', 'w') as output:
    cases = int(input.readline().strip());
    for i in range(1,cases+1):
        N,M = map(int,input.readline().strip().split(" "))
        directories = {}
        for p in range(N):
            directory = input.readline().strip().split("/")
            array = directories
            for j in range(1,len(directory)):
                dir = directory[j]
                if array.get(dir)==None:
                    array[dir] = {}
                array = array[dir]
                    
        count = 0
        for p in range(M):
            directory = input.readline().strip().split("/")
            array = directories
            for j in range(1,len(directory)):
                dir = directory[j]
                if array.get(dir)==None:
                    array[dir] = {}
                    count+=1
                array = array[dir]
        print('Case #{}: {}\n'.format(i,count))
        output.write('Case #{}: {}\n'.format(i,count))
    output.close()