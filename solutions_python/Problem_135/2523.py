
def solve(cipher):    
    first_choice=int(cipher)
    for i in range(1,5):
        row=map(int, raw_input().split())
        if (i==first_choice):
            selected_row_1=row
    second_choice=int(raw_input())
    for i in range(1,5):
        row=map(int, raw_input().split())
        if (i==second_choice):
            selected_row_2=row
    m=[val for val in selected_row_1 if val in selected_row_2]
    if len(m)==1:
        return m[0]
    if len(m)>1:
        return "Bad magician!"
    if len(m)==0:
        return "Volunteer cheated!"
        
    
if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))