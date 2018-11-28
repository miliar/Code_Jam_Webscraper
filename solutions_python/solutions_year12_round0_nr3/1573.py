def recnum(a,b):
   count=0
   values={}
   for i in range(a,b+1):
       values[i]=[]
   for i in range(a,b+1):
      for v in range(1,len(str(i))):
         strnum=str(i)
         if int(strnum[v:]+strnum[:v]) in range(a,b+1):
            if int(strnum[v:]+strnum[:v]) - int(strnum) > 0:
                if not int(strnum) in values[int(strnum[v:]+strnum[:v])]:
                    count+=1
                    values[int(strnum[v:]+strnum[:v])].append(int(strnum))


   return count
                  

tests =[
[266, 266],
[106, 918],
[70, 71],
[100, 101],
[170, 953],
[178, 953],
[190, 959],
[112, 919],
[171, 980],
[176, 930],
[121, 997],
[154, 950],
[149, 968],
[362, 918],
[166, 946],
[100, 999],
[118, 991],
[126, 760],
[147, 978],
[189, 929],
[49, 53],
[188, 918],
[163, 954],
[146, 991],
[648, 648],
[115, 945],
[109, 953],
[185, 940],
[137, 937],
[190, 980],
[166, 928],
[135, 929],
[173, 959],
[126, 911],
[102, 305],
[144, 920],
[169, 928],
[170, 942],
[2, 2],
[1, 1],
[100, 909],
[125, 970],
[152, 978],
[172, 948],
[165, 937],
[10, 99],
[154, 982],
[137, 976],
[128, 992],
[145, 967]
    ]


def run():
    cnt=1
    for a in tests:
        print "Case #"+str(cnt)+": "+str(recnum(a[0],a[1]))
        cnt+=1


run()
