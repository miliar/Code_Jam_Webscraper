'''
Created on 14 Apr 2012

@author: manofest
'''
import os

folder = 'A1'
input_file_name = 'A-small-attempt0.in' 
output_file_name = 'A-small-attempt0.out'



code = {
'q':'z'        
,'a':'y'        
,'h':'x'        
,'t':'w'        
,'g':'v'        
,'j':'u'        
,'r':'t'        
,'d':'s'        
,'p':'r'        
,'z':'q'        
,'v':'p'        
,'e':'o'        
,'s':'n'        
,'x':'m'        
,'m':'l'        
,'o':'k'   
,'u':'j'        
,'i':'d'   
,'b':'h'               
,'w':'f'        
,'c':'e'        
,'l':'g'        
,'f':'c'        
,'n':'b'        
,'y':'a',
'k':'i'}



def Process(input_file):
    output = open(folder + os.sep + output_file_name,'wb')
    
    total = input_file.readline().strip()
    
    #results = []
    case = 1
    print "Processing and writing out file"
    for line in input_file:
        line_altered = ""
        for let in line:
            if code.has_key(str(let).lower()):
                print "code lookup " + str(code[str(let).lower()])
                line_altered += str(str(code[let]).lower())
            else:
                line_altered = line_altered + str(let)
            print "line alt " + line_altered
        output.write("Case #" + str(case) + ": " + str(line_altered))
        case = case + 1
    
    
    output.close()


if __name__ == '__main__':
    
    print "Starting"
    input_file = open(folder + os.sep + input_file_name)
    Process(input_file)
    
    input_file.close()
    print "Finished Processing"