def solution(case):
    input = f_in.readline()
    english = str(input).strip()
    english_lower = 'abcdefghijklmnopqrstuvwxyz'
    english_higher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    googlenese = 'YHESOCVXDUIGLBKRZTNWJPFMAQ'

    for i in range(0,26):
        english = english.replace(english_lower[i],googlenese[i])
            
    for i in range(0,26):
                english = english.replace(english_higher[i],english_lower[i])     
    #Constant         
    answer = english #change this bit

    if case > 0:
        f_out.write('\n')
    f_out.write('Case #'+str(case)+': '+str(answer))

#Constant
path = 'C:\Code Jam'
f_in = open(path+'\A-small-attempt0.in','r') #make this fit
f_out = open(path+'\out.in','w') #make this fit
no_cases = int(f_in.readline())

for i in range(no_cases):
    solution(i)

f_in.close
f_out.close