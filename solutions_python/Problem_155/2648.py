with open('A-large.in') as f:
    count = f.readline()
    count = int(count)

    for i in range(count):
        problem = f.readline()
        max_level, distribution = problem.split(' ')

        original = distribution.strip()

        # solution
        # for each index k, if the sum of the numbers located in the indices lower than k is gte the number at k, suffice

        friends = 0

        for k in range(int(max_level) + 1):
            value = int(distribution[k])
             
            others = sum(int(distribution[i]) for i in range(k))

            if others + friends < k:
                more = k - others - friends

                friends += more

        print 'Case #{id}: {friends}'.format(id=str(i+1), friends=friends) 
