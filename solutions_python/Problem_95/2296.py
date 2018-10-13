input_file = open("C:\\A-small-attempt0.in", 'r')
output_file = open("C:\\A-small-attempt0_salida.in", 'w')
t = int(input_file.readline())
code_output = 'yhesocvxduiglbkrztnwjpfmaq'
code_input = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0,int(t)):
    sale = ''
    entra = input_file.readline()
    for j in range(0, len(entra) - 1):
        indx = code_input.find(entra[j])
        if(indx == -1):
            sale = sale + ' '
        else:
            sale = sale + code_output[indx]
    output_file.write ("Case #" + str((i + 1)) + ": "+ sale + "\n")
input_file.close()
output_file.close()
        
