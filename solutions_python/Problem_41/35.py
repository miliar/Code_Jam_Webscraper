#Templates:
# [int(x) for x in infile.readline().split()]

with open("B.in") as infile:
    with open("B.out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            # Perform all nessesary calculation
            number = [int(x) for x in infile.readline().strip()]
            digs = []
            for i in range(len(number)-1, -1, -1):
                dig = number[i]
                digs.append(dig)
                if dig < max(digs):
                    dig = min([x for x in digs if x > dig])
                    digs.remove(dig)
                    digs.sort()
                    print("Case #{nc}: digs = {digs}\n".format(nc=ncase+1,digs=digs))
                    number = number[0:i] + [dig] + digs
                    print("Case #{nc}: Change #{nd}\n".format(nc=ncase+1,nd=i))
                    break
            else:
                number.sort()
                nz = number.count(0)
                number = [number[nz]] + number[0:nz] + number[nz+1:]
                number.insert(1, '0')
                print("Case #{nc}: Enlarge\n".format(nc=ncase+1))
            answer = "".join([str(x) for x in number])
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=answer))
print("Ready")
