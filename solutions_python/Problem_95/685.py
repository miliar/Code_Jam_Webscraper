def replace(input_str):
    output_str = ''
    for to_replace in input_str:
        if to_replace == ' ' :replaced = ' '
        elif to_replace == 'c' :replaced = 'e'
        elif to_replace == 'r' :replaced = 't'
        elif to_replace == 'y' :replaced = 'a'
        elif to_replace == 'e' :replaced = 'o'
        elif to_replace == 'k' :replaced = 'i'
        elif to_replace == 'd' :replaced = 's'
        elif to_replace == 'b' :replaced = 'h'
        elif to_replace == 'p' :replaced = 'r'
        elif to_replace == 's' :replaced = 'n'
        elif to_replace == 'i' :replaced = 'd'
        elif to_replace == 'm' :replaced = 'l'
        elif to_replace == 'j' :replaced = 'u'
        elif to_replace == 'x' :replaced = 'm'
        elif to_replace == 'f' :replaced = 'c'
        elif to_replace == 'w' :replaced = 'f'
        elif to_replace == 't' :replaced = 'w'
        elif to_replace == 'a' :replaced = 'y'
        elif to_replace == 'l' :replaced = 'g'
        elif to_replace == 'v' :replaced = 'p'
        elif to_replace == 'g' :replaced = 'v'
        elif to_replace == 'o' :replaced = 'k'
        elif to_replace == 'n' :replaced = 'b'
        elif to_replace == 'u' :replaced = 'j'
        elif to_replace == 'h' :replaced = 'x'
        elif to_replace == 'z' :replaced = 'q'
        elif to_replace == 'q' :replaced = 'z'
        else:
            replaced = chr(10)
        output_str += replaced
    return output_str
f = open('G:/Study/input.in', 'r')
g = open('G:/Study/output.txt', 'w')
no_test_cases = int(f.readline())
for i in range(1,no_test_cases+1):
    g.write("Case #"+str(i)+": "+replace(f.readline()))
f.close()
g.close()
g = open('G:/Study/output.txt', 'r')
print g.read()
g.close()

