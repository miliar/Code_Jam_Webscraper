file = 'A-large.in.txt'

def parameters(textfile):
    file = open(textfile, 'r')
    curr_line = file.readline()
    curr_line = file.readline()
    wanted_list = []
    
    while curr_line != '':
        most_shy, dist = curr_line.split(' ')
        
        wanted_list = wanted_list + [[most_shy, str(dist)[:-1]]]

        curr_line = file.readline()
        

    return wanted_list

##print(parameters(file))

def get_most_shy(lst):
    return lst[0]

def get_dist(lst):
    return lst[1]

def number(lst):
    output = open('GCJ Ovation Answer.txt', 'w')

    for index, element in enumerate(lst):
        extra = 0
        total_stand = 0
        dist = get_dist(element)
        
        for s in range(len(dist)):
            if total_stand >= s:
                total_stand += int(dist[s])
                
            else:
                extra += (s - total_stand)
                total_stand += int(dist[s]) + (s - total_stand)

        

        output.write(("Case #%d: %d" % (index + 1,extra) +'\n'))

       
number(parameters(file))


    




        
