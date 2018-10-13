'''
Created on Apr 14, 2012

@author: lucamaf
'''

def total_point(alist):
    result=0
    for i in range(len(alist)):
        result+=alist[i]
    return result

def best_res(alist):
    return max(alist)

def is_surprise(alist):
    if max(alist)-min(alist)==2:
        return True
    return False

def expand_list(total,surprise):
    avg=total/3
    com=total/3.0
    diff=com-avg
    if surprise and diff<0.5:
        temp=0
        for i in range(3):
            temp=3*avg-1+i
            if temp==total:
                return [avg-1,avg-1+i,avg+1]
        return[-1,-1,-1]
    elif surprise and diff>=0.5:
        temp=0
        for i in range(3):
            temp=3*avg+2+i
            if temp==total:
                return [avg,avg+i,avg+2]
        return[-1,-1,-1]
    else:
        for i in range(3):
            temp=3*avg+i
            if temp==total and i==0:
                return [avg,avg,avg]
            elif temp==total and i==1:
                return [avg,avg,avg+1]
            elif temp==total and i==2:
                return [avg,avg+1,avg+1]
        return[-1,-1,-1]

def comp_list(alist,surprises,score):
    lists=[]
    result=0
    for i in range(len(alist)):
        lists.append(expand_list(alist[i], False))    
    
    #print lists
    
    for i in range(len(lists)):
        if -1 in lists[i]:
            lists[i]=expand_list(alist[i], True)
            surprises-=1
    #print lists
    i=0
    while surprises>0 and i<len(lists):
        avg=alist[i]/3
        m=max(lists[i])
        if m<score and avg+1>=score:
            temp=expand_list(alist[i], True)
            if -1 not in temp:
                lists[i]=temp
                surprises-=1
        i+=1
    i=0
    while surprises>0 and i<len(lists):
        avg=alist[i]/3
        m=max(lists[i])
        if m<score:
            temp=expand_list(alist[i], True)
            if -1 not in temp:
                lists[i]=temp
                surprises-=1
        i+=1            
    for i in range(len(lists)):
        if max(lists[i])>=score:
            result+=1
    #print lists
    return result

def results(afile):
    f=open(afile)
    T=int(f.next())
    for i in range(T):
        line=f.next()
        nums=line.split()
        N=int(nums[0])
        s=int(nums[1])
        p=int(nums[2])
        li=[]
        for j in range(N):
            li.append(int(nums[j+3]))
        res=comp_list(li, s, p)
        print 'Case #{case}: {s}'.format(case=i+1,s=res)

results('B-small-attempt0.in.txt')