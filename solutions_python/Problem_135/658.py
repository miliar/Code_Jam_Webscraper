from sys import argv
import math

f = open("A-small-attempt0.in")
cases = int(f.readline())

def get_row(answer):
    j = 1
    row = []
    while j <= 4 : 
        a = f.readline().split()
        if j == answer[0]:
            row = a;
        j += 1
    return row

def check_card(index, row1, row2):
    result = set(row1) & set(row2)
    num =  len(result)
    if num == 1:
        print "Case #%d:"%index, result.pop()  
    elif num > 1:
        print "Case #%d:"%index, "Bad magician!"
    else:
        print "Case #%d:"%index, "Volunteer cheated!"

for i in range(cases):
    answer = map(int, f.readline().split())
    row1 = get_row(answer)
    answer = map(int, f.readline().split())
    row2 = get_row(answer)
    result = check_card(i+1, row1, row2)
    
