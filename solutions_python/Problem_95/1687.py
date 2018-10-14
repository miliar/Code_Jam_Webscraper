'''
Created on Apr 14, 2012

@author: Ankit
'''
code = 'yhesocvxduiglbkrztnwjpfmaq'
with open('A-small-attempt0.in',"r") as file_inp:
    T = int(file_inp.readline())
    inp = file_inp.readlines()

out=''
with open('out.txt', 'w') as file_out:
    for j in range(T):
        x=''
        for i in inp[j]:
            if ord(i) >= ord('a') and ord(i)<= ord('z'):
                x = x + code[ord(i)-97]
            elif ord(i) == ord(' '):
                x = x + ' '
        out = out+"Case #"+str(j+1)+": "+x
        file_out.write(out)
        out = "\n"
