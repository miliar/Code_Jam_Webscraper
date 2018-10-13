with open("A.in") as infile:
    with open("A.out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            # Perform all nessesary calculation
            size = int(infile.readline())
            row = [0] * size
            for i in range(size):
                nums = [j*int(x) for j, x in enumerate(infile.readline().strip())]
                row[i] = max(nums)
            # Reorder
            num = 0
            for i in range(size):
                if row[i] <= i: continue
                for j in range(i+1,size):
                    if row[j] <= i:
                        #print("{n}: {j} => {i}".format(n=ncase,i=i,j=j))
                        num += j - i
                        row[i:i] = [row[j]]
                        del row[j+1]
                        break
                        
            
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=num))
print("Ready")
