import math

def prep_file():
    #f = open('Daten/C-large-practice.in', 'r');
    f = open('Daten/C-small-attempt0.in', 'r');
    #f = open('Daten/testcase.txt', 'r');
    singleLines = f.readlines();
    return singleLines;

def extract_case(line):
    line = line.replace('\n', '');
    return line.split(' ');

def is_palindrome(w):
    string = str(int(w));
    print string, ' palindrome: ', string == string[::-1] 
    return string == string[::-1]

def is_square(number):
    a = math.sqrt(number);
    b = int(a)
    print 'a-b ', str(a-b), ' a: ', a, ' b: ', b
    print (a - b) == 0
    return (a - b) == 0 and is_palindrome(a)

def main():
    f = prep_file();
    cases = f.pop(0);
    output = '';
    for i in range(int(cases)):
	c = extract_case(f[i]);
        offset = int(c[0])
        counter = 0;
        for e in range(int(c[1]) - int(c[0]) + 1):
            curr = e + offset;
            print 'curr: ', curr
            if is_palindrome(curr) and is_square(curr):
                counter = counter + 1;

        output = output + 'Case #' + str(i + 1) + ': ' + str(counter) + '\n';

    f = open('myfile.txt', 'w+');
    f.write(output[:-1]);

main()
