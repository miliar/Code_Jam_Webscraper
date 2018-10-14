in_file=open('A-large.in','r')
t_cases=int(in_file.readline())
need=[]
if ((t_cases<=100)and(t_cases>=1)):
    for reader in range(t_cases):
        aggr_sum=0
        frnd_cnt=0
        data_set=(in_file.readline()).split()
        shy_max=int(data_set[0])
        ppl_cnt=data_set[1]
        aggr_sum=int(ppl_cnt[0])
        for shy_level in range(1,shy_max+1):
            needed=shy_level-aggr_sum
            if needed>0:
                frnd_cnt+=needed
                aggr_sum+=needed
                aggr_sum+=int(ppl_cnt[shy_level])
            else:
                aggr_sum+=int(ppl_cnt[shy_level])
        need+=[frnd_cnt]
out_file=open('OutputBig.txt','w')
for reader2 in range(t_cases):
    out_file.write("Case #")
    out_file.write(str(reader2+1))
    out_file.write(": ")
    out_file.write(str(need[reader2]))
    if reader2<99:
        out_file.write('\n')
out_file.close()
