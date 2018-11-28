inp_file=file("A-large.in")
out_file=file("A-large.out","w")

def solve(names,queries):
    switch=0
    free=[True for c1 in names]
    for query in queries:
        if query in names:
            free[names.index(query)]=False
            if not True in free:
                free=[c1!=query for c1 in names]
                switch+=1
    return str(switch)

num=int(inp_file.readline())
for case in range(num):
    l1=int(inp_file.readline())
    p1=[]
    for line in range(l1):
        p1.append(inp_file.readline())
    l2=int(inp_file.readline())
    p2=[]
    for line in range(l2):
        p2.append(inp_file.readline())
    out_file.write("Case #%s: "%(case+1)+solve(p1,p2)+"\n")
inp_file.close()
out_file.close()
