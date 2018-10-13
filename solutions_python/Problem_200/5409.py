with open('B-small-attempt0.in') as f:
        n = int(f.readline())
        for i in range(n):
                num = int(f.readline())
                num_copy = num
                while num_copy > 0:
                        num = str(num_copy)
                        prev = num[0]
                        success = True
                        for m in num[1:]:
                                if int(prev) > int(m):
                                        success = False
                                        break
                                else:
                                        prev = m
                        if success == True:
                                print('Case #' + str(i+1) + ': ' + str(num_copy))
                                break
                        else:
                                num_copy -= 1
