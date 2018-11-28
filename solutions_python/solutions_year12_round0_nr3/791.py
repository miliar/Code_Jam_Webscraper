import sys
j="".join
def candidate(first,rest):
    cand_inde=[]
    for inde,num in enumerate(rest):
        if num>=first:
            cand_inde.append(inde)
    return cand_inde
            
def pre_candi():
    cand_list=[[]]
    for i in range(1,2000000):
        num=map(int,list(str(i)))
        cand_list.append(candidate(num[0],num[1:]))
    return cand_list


def pre_pair(cand_list):
    pair_list_set=[]
    for all_inde,cand in enumerate(cand_list):
        num=str(all_inde)
        first=num[0]
        rest_str=num[1:]
        dup_set=[]
        check_dup=[]
        for inde in cand:
            candi_comb=int(j([rest_str[inde:],str(first),rest_str[:inde]]))
            if candi_comb<=2000000 and candi_comb>=1 and candi_comb>all_inde:
                if candi_comb not in check_dup:
                    pair_list_set.append([all_inde,candi_comb])
                    check_dup.append(candi_comb)
    return pair_list_set
    

        
# a=pre_candi()
# b=pre_pair(a)
with open("3.output","w") as op:
    with open("3.input") as ip:
        case_cnt=int(ip.readline().strip())
        for case_line in range(case_cnt):
            line=ip.readline().strip().split()
            line_min=int(line[0])
            line_max=int(line[1])
            count=len(filter(lambda x:x[0]>=line_min and x[1]<=line_max,b))
            print count

    


