noOfTestCase = int(raw_input())
result =[]
def compare_two_list (first_list, second_list):
    first_list = first_list.split(' ')
    second_list = second_list.split(' ')
    if sorted(first_list)==sorted(second_list):
        return 'Bad magician!'
    if len(list(set(first_list) & set(second_list))) ==0:
        return 'Volunteer cheated!'
    else:
        
        return list(set(first_list) & set(second_list))
for each in range(0,noOfTestCase):
    first_input = []
    second_input =[]
    first_ans = int(raw_input())
    for i in range(0,4):
        first_input.append(raw_input())
    second_ans = int(raw_input())
    for i in range(0,4):
        second_input.append(raw_input())
    result_compare_result=''
    compare_result = compare_two_list(first_input[first_ans-1], second_input[second_ans-1])
    if type(compare_result) is list:
        if len(compare_result) > 1:
            result_compare_result = 'Case #'+str(each+1)+': Bad magician!'
        
        else:
            another= ''
            for each1 in compare_result:
                another += each1 +'^'
            result_compare_result = 'Case #'+str(each+1)+': '+ another[:-1]
    
    else:
        result_compare_result ='Case #'+str(each+1)+': '+compare_result
    result.append(result_compare_result)
for re in result:
    print str(re).replace(',','').replace("'",'').replace('(','').replace(')','').replace('^',',')