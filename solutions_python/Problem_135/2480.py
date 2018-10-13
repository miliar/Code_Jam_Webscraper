
testcase = int(raw_input())
result =[]
def compare (set1, set2):
    set1 = set1.split(' ')
    set2 = set2.split(' ')
    if sorted(set1)==sorted(set2):
        return 'Bad magician!'
    elif len(list(set(set1) & set(set2))) ==0:
        return 'Volunteer cheated!'
    else:
        
        return list(set(set1) & set(set2))
for each in range(1,testcase+1):
    first_input = []
    second_input =[]
    first_ans = int(raw_input())
    for i in range(0,4):
        first_input.append(raw_input())
    second_ans = int(raw_input())
    for i in range(0,4):
        second_input.append(raw_input())
    result_temp=''
    temp = compare(first_input[first_ans-1], second_input[second_ans-1])
    if type(temp) is list:
        if len(temp) > 1:
            result_temp = 'Case #'+str(each)+': Bad magician!'
        
        else:
            another= ''
            for each1 in temp:
                another += each1 +'&'
            result_temp = 'Case #'+str(each)+': '+ another[:-1]
    
    else:
        result_temp ='Case #'+str(each)+': '+temp
    result.append(result_temp)
for re in result:
    print str(re).replace(',','').replace("'",'').replace('(','').replace(')','').replace('&',',')