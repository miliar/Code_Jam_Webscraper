f = open('B-large.in', 'r')
o = open('cookieclicker.out', 'w')

N = int(f.readline())
ccs = []
for x in f.readlines():
    C,F,X = map(float, x.split(' '))
    ccs.append([C,F,X,2.0])

def time_to_x(cc):
    return cc[2]/cc[3]

def time_to_farm_x(cc):
    return cc[0]/cc[3] + cc[2]/(cc[3] + cc[1])

def buy_farms(cc):
    count = 0
    while time_to_x(cc) > time_to_farm_x(cc):
        count += 1
        cc[3] += cc[1]
    return count

def total_time(cc):
    buy_count = buy_farms(cc)
    cc[3] = 2.0
    total_time = 0
    for x in range(buy_count):
        rate = x * cc[1] + cc[3]
        total_time += cc[0]/rate
    total_time += cc[2]/(buy_count*cc[1] + cc[3])
    return total_time

answers = []
for x in ccs:
    answers.append(total_time(x))

for x in range(N):
    o.write('Case #' + str(x+1) + ': ' + str(answers[x]) + '\n')