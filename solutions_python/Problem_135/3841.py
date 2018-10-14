def solve(path):
    
    answer = []
    
    with open(path) as f:
        alist = [line.rstrip() for line in f]
    data = []  
    cases = int(alist.pop(0))
    for w in range(cases):
        b = []
        for k in range(2):
            ans = int(alist.pop(0))
            print(ans)
            for j in range(4):
                if (j==ans-1):
                    u = alist.pop(0)
                else:
                    alist.pop(0)
            b.append([int(x) for x in u.split()])
        c = set(b[0]) & set(b[1])
        if (len(c) == 1):
            answer.append("Case #{0}: {1}".format(w+1, c.pop()))
        else: 
            if (len(c) == 0):
                answer.append(str("Case #{0}: Volunteer cheated!".format((w+1))))
            else:
                answer.append("Case #{0}: Bad magician!".format((w+1)))
        print(c)
        

    return answer

ans =  solve("input_test.in")
print(ans)
with open("output_file2.out", 'w') as f:
        for item in ans:
            f.write("%s\n" % item)
                
        
    
