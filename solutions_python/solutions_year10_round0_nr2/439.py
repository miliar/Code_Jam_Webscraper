# coding: utf-8

"""
Problem

"""
foutput  = open('B-large.out', 'w')

def gcm(num1, num2):
        if num1 > num2:
                i = num1
                num1 = num2
                num2 = i
        if (num2 % num1) == 0 :
                return num1
        else:
                return gcm((num2 % num1),num1)
        
i = 0
for line in open('B-large.in', 'r'):
        items = map(int, line[:-1].split())
        if len(items) == 1:continue
        i += 1
        n = items.pop(0)
        items.sort()
        prev = 0
        diff = []
        gcm_o = 0
        for item in items:
                if prev == 0 or prev == item:
                        if gcm_o == 0:
                                gcm_o = item
                        prev = item
                        continue
                diff.append(item - prev)
                gcm_o = gcm(gcm_o, item)
                prev = item
        diff.sort()
        prev = 0
        for item in diff:
                if prev == 0 or prev == item:
                        prev = item
                        continue
                prev = gcm(prev, item)
#        print str(n) + ":" + str(prev) + ":" + str(gcm_o),
#        print str(n) + ":" + str(prev) + ":" + str(items) + ":" +str(diff)
#        print prev - (items[0] % prev)
        if prev == 1 or gcm_o == prev:
                day = 0
        else:
                day = prev - (items[len(items) - 1] % prev)
        result = "Case #" + str(i) + ": " + str(day) + '\n'
#        print result,
        foutput.write(result)
foutput.close()

