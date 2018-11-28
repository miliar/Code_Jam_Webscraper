# Script text here


def build_dict(s,t):
   
    dict={}
    for i in range(0,len(s)):
        if s[i] not in dict:
            dict[s[i]]=t[i]
    return dict       
            

googlerese = "y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
english = "a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
dict = build_dict(googlerese.replace(" ",""),english.replace(" ",""))
dict["z"]="q"
        
def googlerese_to_english(i,dict):
    o = ''
    for n in i:
        if n not in dict:
            o=o+n
        else:
            o=o+dict[n]
    return o         
        

file_in=open("c:/users/rhv/Downloads/A-Small-attempt3.in","r")
 
out = ''
i = 0
for e in file_in:
   
    if i!=0:
       
        out = out +"Case #" + str(i) +": "+ googlerese_to_english(e,dict)
    i=i+1
print out   
          