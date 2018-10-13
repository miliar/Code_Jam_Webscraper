with open('input.in', 'r') as fin:
    with open('output.txt', 'w') as fout:
        numcases = int(fin.readline())
        for i in range(1,numcases+1):
            numcandy = int(fin.readline())
            candies = [int(j) for j in fin.readline().split()]
            answer = ""
            xsum = 0
            for j in candies:
                xsum = xsum ^ j
            if (xsum != 0):
                answer = "NO"
            else:
                answer = str(sum(candies)-min(candies))
                                
            fout.write("Case #"+str(i)+": ")
            fout.write(answer)
            fout.write('\n')
