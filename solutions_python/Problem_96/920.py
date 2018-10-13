if __name__ == '__main__':
    num = int(raw_input())
    
    for i in range(1, num + 1):
        line = raw_input().split(' ')
        _ = int(line[0])
        S = int(line[1])
        p = int(line[2])
        
#        print('S = ' + str(S))
#        print('p = ' + str(p))
        
        scores = [int(n) for n in line[3:]]

        points = []
        
        for s in scores:
            if s % 3 == 0:
                points.append((s/3, s/3, s/3))
            if s % 3 == 1:
                points.append((s/3, s/3, s/3 + 1))
            if s % 3 == 2:
                points.append((s/3, s/3 + 1, s/3 + 1))
        
#        print scores
#        print points
        
        total= 0
        
        surp = 0
        
        for contestant in points:
            if max(contestant) >= p:
                total += 1
#                print contestant
            elif max(contestant) + 1 >= p and surp < S and sum(contestant) != 0 and sum(contestant) % 3 != 1:
                total += 1
                surp += 1
#                print contestant
                    
        print "Case #" + str(i) + ": " + str(total)