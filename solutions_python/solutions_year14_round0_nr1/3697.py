def rows():
    lista_de_rows = []
    for i in range(4):
        row = [int(x) for x in str(raw_input()).split()]
        lista_de_rows.append(row) 
    return lista_de_rows

def parse_answer(answer):
    
    if len(answer) == 0:
        return "Volunteer cheated!"
    elif len(answer) == 1:
        return answer[0]
    return "Bad magician!"

testcases = int(raw_input())
for t in range(1, testcases + 1):
    first_answer = int(raw_input())
    first_array = rows()
    second_answer = int(raw_input())
    second_array = rows()

    answer = []
    for i in first_array[first_answer-1]:
        if i in second_array[second_answer-1]:
            answer.append(i)
    
    print "Case #"+str(t)+":",parse_answer(answer)
    
