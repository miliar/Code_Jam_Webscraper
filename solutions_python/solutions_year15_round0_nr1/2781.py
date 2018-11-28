def number_of_friends(intest):
    index = -1
    arr = []
    for one in intest:
        index += 1
        count = one
        weight = index
        arr.append((weight, count))
    
    #print str(arr)
    
    appended = []
    
    
    first = True
    index = -1
    total_count = 0
    #print str(arr)
    for one in arr:
        index += 1
        if first:
            if one[1] == 0:
                appended.append((0, 1))
                total_count += 1
            else:
                total_count += one[1]
            first = False
        else:
            prev_count = arr[index-1][1]
            if index !=1:
                total_count += prev_count
    
            
            diff = total_count - one[0]
            #print 'index '+str(index)+' | diff: '+str(diff)+' | one: '+str(one)+' | total_count: '+str(total_count)+' | prev_count: '+str(prev_count)           
    
            if diff < 0:
                #print 'xaxa'
                app = diff * -1
                appended.append((index-1,app))
                total_count += app
            
    
    return len(appended)

f = open('ovation.in', 'r')
cases = []
output = []
first = True
for one in f:
    if first:
        first = False
        continue
    one = one.rstrip('\n')
    parts = one.split(' ')
    cases.append(parts[1])
f.close()   


index_1 = 0

fin_res = False
for one in cases:
    index_1 +=1
    tmp = map(int, one)
    rs = number_of_friends(tmp)
    trs = 'Case #'+str(index_1)+': '+str(rs)
    
    if fin_res == False:
        fin_res = ''
        fin_res += trs
    else:
        fin_res +='\n'+trs
        

f = open('ovation.out', 'w')
f.write(fin_res)
f.close()







        