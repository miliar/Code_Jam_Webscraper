import sys
import pdb

def get_char_num(s):
    m_res=[]
    for c in s:
        if len(m_res)>0:
            if c==m_res[-1][0]:
                m_res[-1]=(c,m_res[-1][1]+1)
            else:
                m_res.append((c,1))
        else: m_res.append((c,1))
    return m_res

def opr_num(s1,st):
    num=0;
    s1_group=get_char_num(s1)
    st_group=get_char_num(st)
    if s1_group==st_group: return 0
    elif len(s1_group)!=len(st_group): return -1
    else:
        for m_i in range(len(s1_group)):
            if st_group[m_i][0]!=s1_group[m_i][0]:
                return -1
            elif st_group[m_i][1]>s1_group[m_i][1]:
                num+=st_group[m_i][1]-s1_group[m_i][1]
            elif st_group[m_i][1]<s1_group[m_i][1]:
                num+=s1_group[m_i][1]-st_group[m_i][1]
    return num

with open('test_in.in','r') as f:
	data=f.readlines()

N=int(data[0]);
res="";

t=0;
for i in range(N):
    n=int(data[t+1])
    #pdb.set_trace()
    ss=[data[t+2+idx].split()[0] for idx in range(n)]
    #print t
    t=t+n+1;
    n_mins=[]
    res_t=""
    for t_s in range(n):
        n_tmp=[];
        for cmp_s in ss:
            n_tmp.append(opr_num(ss[t_s],cmp_s))
        if -1 in n_tmp:
            res_t="Fegla Won"
            break
        else: n_mins.append(sum(n_tmp))
    if res_t!="Fegla Won": res_t=str(min(n_mins))
    
    res+="Case #"+str(i+1)+": "+res_t +"\n"

#print res

with open('res.txt', 'w') as f:
	f.write(res)
