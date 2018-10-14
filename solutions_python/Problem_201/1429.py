for x in range(int(input())):
    N, K = map(int, (input().strip().split()))
    i = 0
    while True:
        if int(K/(2**(i+1))) == 0:
            break
        i = i + 1
    y = 2**i
    minimum_in_partition = (N-y+1)//y
    maximum_in_partition = minimum_in_partition + 1
    number_max = (N - y + 1)% y
    number_min = y - number_max
    if(K - y) < number_max:
        print("Case #{0}: {1} {2}".format(str(x+1), maximum_in_partition//2, (maximum_in_partition - 1)//2))
    else:
        print("Case #{0}: {1} {2}".format(str(x+1), minimum_in_partition//2, ((minimum_in_partition-1)//2)))