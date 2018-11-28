#-*- coding:utf-8 -*-

input_file = open('entrada.in')
output_file = open('output.out', 'w')

phrase = 'welcome to code jam'

# N casos
N = input_file.readline()
N = int(N)

def count(p, line):
    if p == line:
        return 1

    if len(p) > len(line):
        return 0

    if not p:
        return 1

    try:
        head, rest = line.split(p[0], 1)
    except ValueError:
        return 0


    return count(p[1:], rest) + count(p, rest)
    

def complete(string):
    if len(string) >= 4:
        return string

    return '0'*(4-len(string)) + string
        
        

for case in range(1, N+1):
    result = count(phrase, input_file.readline())
    
    # Se deben sacar solo los últimos 4 del result.
    result = str(result)

    result = complete(result)
    
    output_file.write("Case #%s: %s\n"%(case, result))
