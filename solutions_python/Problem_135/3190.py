'''
Created on Apr 12, 2014

@author: rakesh
'''

def generate_answer_and_arrangement(f):
    answer = int(f.readline().split()[0])
    arrangement = []
    
    
    #Generate lines as sets, this uses the property that lines contain unique numbers
    for i in range(4):        
        arrangement.append(set(f.readline().split()))
    
    return answer, arrangement

def process_test_case(i, ans1, arr1, ans2, arr2):
    #print 'ans1:', ans1, "arr1:",arr1
    #print 'ans2:', ans2, "arr2:",arr2
    
    #Take the relevant lines from the input
    set1 = arr1[ans1-1]
    set2 = arr2[ans2-1]

    #Intersect the line sets    
    intersection =  set1 & set2
    case_num = "Case #"+str(i+1)+":"
             
    #If the intersection has 1 element, it is the output
    if len(intersection) == 1:
        print case_num, list(intersection)[0]
    #If the intersection has more than 1 elements, Bad Magician!
    elif len(intersection) > 1:
        print case_num, "Bad magician!"
    #If the intersection is a null set, 
    elif len(intersection) == 0:
        print case_num, "Volunteer cheated!"
    
    
if __name__ == '__main__':
    f = open("A-small-attempt0.in", "r")
    
    num_test_cases = int(f.readline().split()[0])
    #print "Number of test cases", num_test_cases
    
    #Go through each test-case and prcocess them
    for i in range(num_test_cases):
        ans1, arr1 = generate_answer_and_arrangement(f)
        ans2, arr2 = generate_answer_and_arrangement(f)
        process_test_case(i, ans1, arr1, ans2, arr2)
        
        
    
            