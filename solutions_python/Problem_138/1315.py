def main():
    a = open('D-large.in', 'r')
    test = a.read()
    #test = raw_input()
    test2 = test.replace('\n', ',')
    allinfo = test2.split(',')
    testcase = int(allinfo[0])
    b = open('result4','w')
    for i in range (1, testcase + 1):
        block_num = allinfo[3 * i - 2]
        testnaomi = allinfo[3 * i - 1]
        testken = allinfo[3 * i]
        naomi = testnaomi.split(' ')
        ken = testken.split(' ')
        ken2 = testken.split(' ')
        
        counter = 0
        counter2 = 0
        naomi.sort()
        ken.sort()
        ken2.sort()
        len_ken2 = len(ken2)
        
        for n in naomi:
            if float(n) < float(ken[0]):
                del ken[-1]
            elif float(n) > float(ken[0]):
                del ken[0]
                counter += 1
        
        for m in naomi:
            counter3 = []
            

            for k in range (0, len_ken2):
                if float(ken2[k]) > float(m):
                    counter3.append(k)
                else: pass
                
            if counter3:
                del ken2[counter3[0]]
                len_ken2 = len_ken2 - 1
                counter2 +=1
            
            
        print ("Case #%d: %d %d" % (i, counter, int(block_num) - counter2))
        b.write("Case #%d: %d %d\n" % (i, counter, int(block_num) - counter2))
                        
main()
