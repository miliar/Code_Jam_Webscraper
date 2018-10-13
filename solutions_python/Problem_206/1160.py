for tests in range(int(input())):

    D,N = (int(i) for i in input().split())


    besttime = 0

    for horses in range(N):

        start, speed = (int(i) for i in input().split())

        time = (D-start)/speed

        if besttime < time:

            besttime = time

    output = 'Case #'+str(tests+1)+': '

    output += str(D/besttime)

    print(output)

        
