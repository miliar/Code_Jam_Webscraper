


fread=open('/home/jay/Desktop/A-large.in','r')
fwrite=open('/home/jay/Desktop/A-small-practice.out','w')

LDN=fread.readline().strip()
LDN_list= LDN.split(" ")
D=LDN_list[1]
N=LDN_list[2]

main_wordlist=[]
for i in range(int(D)):
  word =  str( fread.readline().strip() )
  main_wordlist.append( word )

LL=[]
st_list=[]
LL_pos=0

def func1(st):
  global LL
  global st_list
  i=0
  while (i < len(st) ):
    if st[i] =="(":
      st_list.append('LL')
      temp_ll_list=[]
      i=i+1
      while(st[i]!=")"):
        temp_ll_list.append(st[i])
        i=i+1
      LL.append(temp_ll_list)
      i=i+1
    else:
      st_list.append(st[i])
      i=i+1

def func2(elem,wordlist,pos):
        matched_list=[]
        if elem!='LL':
           for word in wordlist:
             if word[pos] == elem:
               matched_list.append(word)
        else:
          global LL_pos
          global LL

          for word in wordlist:
            if word[pos] in LL[LL_pos]:
              matched_list.append(word)
          LL_pos= LL_pos+1
        return matched_list


for caseno in range(int(N)):
    
    input=""
    input= fread.readline()
    input = input.strip()
    func1(input)
    pos=0
    LL_pos=0

    wordlist=[]
    for w in main_wordlist:
      wordlist.append(w)

    for elem in st_list:
        wordlist = func2(elem,wordlist,pos)
        if wordlist == []:
           break
        pos = pos + 1
    count= len(wordlist)
    o_string="Case #"+str(caseno+1)+": "+str(count)+"\n"
    fwrite.write(o_string)


    LL=[]
    st_list=[]
    
fread.close()
fwrite.close()

