def check(pan):
    return all(item == True for item in pan)
if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        l = raw_input().strip().split()
        pan = list(l[0])
        flips = int(l[1])

        pan = [ True if item == '+' else False for item in pan ]
        count = 0
        done = False
        for j in range(len(pan) - flips + 1):
            
            if not pan[j]:
                for k in range(j, j+flips):
                    pan[k] = not pan[k]
                count += 1

            if check(pan):
                print "Case #%d: %d" %(i+1, count)
                done = True
                break

        if not done:
            print "Case #%d: IMPOSSIBLE" %(i+1)

                


        
        
