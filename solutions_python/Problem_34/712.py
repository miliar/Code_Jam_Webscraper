     
def TestWord(case,word):
    case_iter=iter(case)
    word_iter=iter(word)
    while 1:
        try:
            word_char=word_iter.next()
            case_char=case_iter.next()
            if(case_char=='('):
                found=False
                while(case_char!=')'):
                    case_char=case_iter.next()
                    if case_char==word_char:
                        found=True;
                if not found:
                    return False
            elif case_char!=word_char:
                #print "false cause of char",case_char,"in",case,"for word",word,word_char
                return False
        except:
            break;
    return True    

def getMatches(case,words):
    word_length=len(words[0])
    total_matches=0
    for word in words:
        if TestWord(case,word):
            #print word,"matches",case
            total_matches+=1
    return total_matches        

file_in=open("A-large.in")
lines=file_in.readlines()
file_in.close()
#get input nos
input_nos=(total_chars,total_words,total_cases)=map(int,lines[0].split(' '))
print input_nos
words=[]
cases=[]
lines=lines[1:]
#get words
i=0
while i<total_words:
    words.append(lines[i][:total_chars])
    i=i+1
#print words
i=0;
while i<total_cases:
    cases.append(lines[total_words+i].strip())
    i=i+1
#print cases
file_out=open("out.txt","w")
i=1
for case in cases:
    output_str="Case #%d: %d"%(i,getMatches(case,words))
    print output_str
    if i!=1:
        file_out.write("\n"+output_str)
    else:
        file_out.write(output_str)
    i=i+1
file_out.close()



