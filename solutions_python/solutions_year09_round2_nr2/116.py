import copy
def asc_sort(num):
    temp = list(num)
    temp2 = copy.deepcopy(temp)
    temp2.sort(reverse=True)
    if num == ''.join(temp2):
        temp2.append('0')
        tempseg = copy.deepcopy(temp2)
        minitem = None        
        while (len(tempseg) != 0):
            minitem = min(tempseg)
            if minitem != '0':
                break
            else:
                tempseg.remove(minitem)
        if minitem == None:
            return num + '0'
        else:
            temp2.remove(minitem)
            temp3 = copy.deepcopy(temp2)
            temp3.sort()
            result =[minitem]
            result.extend(temp3)
            return ''.join(result)
    item = -1
    while True:
        next = item - 1
        if temp[item] > temp[next]:
            tempseg = copy.deepcopy(temp[item:])
            minitem = None
            while (len(tempseg) != 0):
                minitem = min(tempseg)
                if minitem > temp[next]:
                    break
                else:
                    tempseg.remove(minitem)       
                                        
            index = temp[item:].index(minitem)
            index = len(temp) + index + item
            t = temp[index]
            temp[index] = temp[next]
            temp[next] = t
            seg = temp[item:]
            seg.sort()
            temp[item:] = seg
            return ''.join(temp)
        item = next
        
N = int(raw_input())
for i in range(N):
    T = raw_input()
    print 'Case #%s: %s' % (i + 1, asc_sort(T))
