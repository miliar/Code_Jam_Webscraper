import sys
import math



def rem(moto_num,index,moto):
                count=0
                if index==len(moto_num)-1:
                                return 1
                while moto_num[index]>moto:
                                moto+=moto-1
                                count+=1
                if count>=len(moto_num)-index:
                                return len(moto_num)-index
                for i in range(index,len(moto_num)):
                                if moto_num[i]<moto:
                                                moto+=moto_num[i]
                                elif moto_num[i]<moto*2-1:
                                                moto+=moto-1+moto_num[i]
                                                count+=1
                                elif moto_num[i]>=moto*2-1:
                                               count+=rem(moto_num,i,moto)
                                               break
                return count
                                




fin=open('A-small-attempt4.in','r')
fout=open('output.out','w')
case_num=fin.readline()


print case_num

for i in range (0,int(case_num)):
                out="Case #"
                c_num=i+1
                print c_num
                out+=str(c_num)+": "
                line=fin.readline()
                num_list=line.split(' ')
                moto=int(num_list[0])
                num=int(num_list[1])
                line=fin.readline()
                moto_list=line.split(' ')
                moto_num=[]
                for i in moto_list:
                                moto_num.append(int(i))
                moto_num.sort()
                count=0
                for m in moto_num:
                                if m<moto:
                                                moto+=m
                                                print "1",moto
                                elif m<moto*2-1:
                                                moto+=moto-1+m
                                                count+=1
                                                print "2",m,moto
                                elif m>=moto*2-1:
                                                if moto==1:
                                                                count+=1
                                                                continue
                                                else:
                                                                count+=rem(moto_num,moto_num.index(m),moto)
                                                                break
                                              
                                               
                out+=str(count)    
                out+="\n"
                fout.write(out)
fin.close()
fout.close()
                
                
