
import fileinput

def num_people(length, data):
    add_people = 0
    sum = 0;
    for x in range(0, length+1):
        while( (sum + add_people )< x):
            add_people +=1
        sum = sum + data[x]
    return add_people


def parse(line):
    case_x = {}
    length , data = line.split(' ')
    length = int(length)
    data2 = map(int, list(data.strip()))
    case_x['length'] = length
    case_x['data'] = data2
    return case_x

def main():
   f =  fileinput.FileInput();
   num_tt = int(f.readline());
   for x in range(0,num_tt):
       case_i = parse(f.readline())
       #print(case_i['length'], case_i['data'])
       ans = num_people(case_i['length'], case_i['data'])
       print ('Case #' + str(x+1) + ': ' + str(ans))


main()

