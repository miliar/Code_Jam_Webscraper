# Speaking in Tongue Problem : Google Code Jam 2012 Problem A
# Author : Santhosh Unnikrishnan
# email  : santa001@gmail.com
# date   : 14th April 2012

# Problem: In a file lots of encrypted words are given and this program will
#          print the decrypted words


IN_File_Name  = 'A-small-attempt.in' 
Out_File_Name = 'ProblemA.out'
 
character_mapping = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c',
                     'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g',
                     'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t',
                     's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m',
                     'y':'a', 'z':'q', 'A':'Y', 'B':'H', 'C':'E', 'D':'S',
                     'E':'O', 'F':'C', 'G':'V', 'H':'X', 'I':'D', 'J':'U',
                     'K':'I', 'L':'G', 'M':'L', 'N':'B', 'O':'K', 'P':'R',
                     'Q':'Z', 'R':'T', 'S':'N', 'T':'W', 'U':'J', 'V':'P',
                     'W':'F', 'X':'M', 'Y':'A', 'Z':'Q', ' ':' '} 



def decrypt_string(input_string):
    ''' This function will decrypt the given input string based on the character_mapping
    '''
    out_put_string = ""
    length = len(input_string)
    i = 0
    
    while i < length:
        try:
            out_put_string+= character_mapping[input_string[i]]
        except:
            out_put_string+= input_string[i]
        i = i + 1

    return out_put_string

if __name__ == '__main__':
    no_of_lines       = 0
    list_of_sentances = []
    Max_Entries       =  30
    count             = 0
    string            = ""
    
    fd = open(IN_File_Name,'r')
    lines = fd.readlines()
    fd.close()	

    fd = open(Out_File_Name, 'w')	

    no_of_lines = int (lines[0])
    
    while ((count < Max_Entries) and (count < no_of_lines)) :
        list_of_sentances.append(lines[count + 1])
        count = count + 1

    # Decrypt the input string
    i = 0
    
    while (i < count):
        string = decrypt_string(list_of_sentances[i])
        out_string = 'Case #%d: %s\n' %((i+1), string)
	fd.write(out_string)
	i = i + 1

    fd.close()
