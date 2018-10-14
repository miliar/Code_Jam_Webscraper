import math

input = open('C:\\Users\\Adam\\Downloads\\CodeJam\\B-large.in', 'r')
output = open('C:\\Users\\Adam\\Downloads\\CodeJam\\outputs.out', 'w')
cases = int(input.readline())
thiscase = 1

#def get_all_trips(total, w):
 #   trips = []
  #  if w:
   #     x = math.ceil(total / 3.0)
   # else:
   #     x = math.ceil(total / 3.0) #largest possible value
   #     y = math.floor(total / 3.0) #smallest possible value
   #     if x == y:
    #        trips.append[x, x, x]
     #   else:
      #      if sum(x, x, y) == total:
       #         trips.append(x, x, y)
        #    else:
         #       trips.append(x, y, y)

def possible_with_surprise(total, high):
    max_possible = min(math.floor((total + 4) / 3.0), 10)
    if total <= 1:
        max_possible = total
    if max_possible >= high:
        return 2
    else:
        return 0

def possible_without_surprise(total, high):
    max_possible = math.ceil(total / 3.0)
    if max_possible >= high:
        return 1
    else:
        return 0
    
while thiscase <= cases:
    stats = input.readline().split(' ')
    number_of_googlers = int(stats[0])
    s = int(stats[1])
    n = number_of_googlers - s
    scoregoal = int(stats[2])
    actlscores = []
    for i in stats[3:]:
        actlscores.append(int(i))
    possibilities = []
    for i in actlscores:
        possibilities.append(possible_with_surprise(i, scoregoal) + \
                             possible_without_surprise(i, scoregoal))
    s_only = 0
    n_only = 0
    both = 0
    for i in possibilities:
        if i == 1:
            n_only += 1
        elif i == 2:
            s_only += 1
        elif i == 3:
            both += 1
    result = min(s_only, s) + min(n_only, n) + both
    output.write('Case #' + str(thiscase) + ': ' + str(result) + '\n')
    thiscase += 1
    
input.close()
output.close()
