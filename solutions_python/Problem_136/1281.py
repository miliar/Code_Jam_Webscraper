import decimal

def getTime(current_production, factory_cost, factory_production, goal):
    if(factory_cost >= goal):
        return (goal / current_production)
    time = 0
    while((current_production * factory_cost) < (factory_production * goal - factory_production * factory_cost)):
        time += factory_cost / current_production
        current_production += factory_production
    print goal
    print current_production
    time += goal / current_production
    return time

def main():
    input = open('input.txt', 'r')
    output = open('output.txt', 'w')

    T = int(input.readline())
    for casenum in xrange(1, T + 1):
        print casenum
        line = input.readline().strip().split(' ')
        line = [decimal.Decimal(x) for x in line]
        factory_cost = line[0]
        factory_production = line[1]
        goal = line[2]

        output.write('Case #' + str(casenum) + ': ')
        output.write(str(getTime(2, factory_cost, factory_production, goal)))
        output.write('\n')

    input.close()
    output.close()

main()