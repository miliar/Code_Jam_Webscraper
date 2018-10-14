def get_row(in_fl):
    row_number = int(in_fl.readline().strip())
    for i in range(1, 5):
        if i==row_number: first_row = map(int, in_fl.readline().strip().split())
        else: in_fl.readline()
    return first_row
OUT_STR = 'Case #%d: %s'    
def read_case(number, in_fl, out_fl):
    row_1 = get_row(in_fl)
    row_2 = get_row(in_fl)
    result = []
    for card in row_1:
        if card in row_2: result.append(card)
    if len(result)==0: out_fl.write(OUT_STR%(number, 'Volunteer cheated!'))
    elif len(result)==1: out_fl.write(OUT_STR%(number, str(result[0])))
    else: out_fl.write(OUT_STR%(number, 'Bad magician!'))
            
    
input_fl = open('A-small-attempt0.in','r')
output_fl = open('A-small-attempt0.out', 'w')
cases = int(input_fl.readline().strip())
for n in range(1, cases+1):
    read_case(n, input_fl, output_fl)
    if n!=cases: output_fl.write('\n')
input_fl.close()
output_fl.close()
