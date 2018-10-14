__author__ = 'Stephane'


#f = open('sample.in', 'r')
f = open('B-large.in', 'r')
o = open('out.in', 'w+')

basic_prod = 2


def resolve(cookies, farm, goal):
    f = 0
    production = basic_prod
    time_to_buy_farm = []
    time_to_buy_farm.append(0)
    time_to_goal = 0
    best_time_to_goal = goal/basic_prod
    while True:
        if f == 0:
            time_to_goal = goal/basic_prod
            #print time_to_goal

        else:

            time_to_buy_farm.append(time_to_buy_farm[f-1] + (cookies ) / production)
            production+=farm
            #print 'time_to_buy_farms %s ' % time_to_buy_farm[f]
            time_to_goal = time_to_buy_farm[f] + goal / production


        #print 'f %s production %s time to goal %s best time %s ' % (f,production,time_to_goal,best_time_to_goal)
        if  time_to_goal > best_time_to_goal :
            break
        else :
            best_time_to_goal = time_to_goal
        f+=1
    return best_time_to_goal


first_line = 0
first_read = False
second_read = False
first_n = -1
second_n = -1

count = 0
case = 1
tests = 0
number = -1
for line in f.readlines():
    if first_line == 0:
        tests = line.rstrip('\r\n')
        first_line += 1
    elif line.rstrip('\r\n') == '':
        continue
    else:
        cookies = float(line.rstrip('\r\n').split()[0])
        farm = float(line.rstrip('\r\n').split()[1])
        goal = float(line.rstrip('\r\n').split()[2])
        #print '%s %s %s ' % (cookies, farm, goal)
        msg = 'Case #%s: ' % case
        case +=1
        time = resolve(cookies, farm, goal)
        #print 'time %s' % time

        o.write('%s%.7f\n' %(msg,time))


f.close()
o.close()
