#!/usr/bin/python
casenumber = int(raw_input())

for case in range(0, casenumber):
    input = raw_input()
    result = ""
    if len(input) == 1:
        print "Case #{}: {}".format(case+1,input)
    else:
        count = len(input)
        for i in range(0,count):
            letter = input[i]
            if result == "":
                result += letter
            elif result[-1] <= letter:
                result += letter
            elif int(result[-1]) > 1:
                resLen = len(result)
                index = resLen - 1
                while index > 0:
                    if int(result[index]) == int(result[index-1]):
                        index-=1
                    else:
                        break
                result = result[:index] + str(int(result[index])-1)
                x = index + 1
                while x < count:
                    result += '9'
                    x+=1
                break
            else:
                x = 1
                result = ""
                while x < count:
                    result += '9'
                    x+=1
                break
        print "Case #{}: {}".format(case+1,result)
