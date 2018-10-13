from sys import argv


with open(str(argv[1]), 'r') as file:
    with open(str(argv[2]), 'w') as out:
        t = int(file.readline())
        for i in range(1,t+1):
            s_max,si = file.readline().split()
            s_max = int(s_max)
            count = 0
            extra = 0
            for j in range(s_max+1):
                if count < j:
                    extra += 1
                    count += 1
                count += int(si[j])
            out.write("Case #{0}: {1}\n".format(i,extra))