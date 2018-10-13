with open ("b-small-attempt0.in.txt") as f, open ("Bout.txt",'a+') as p:
    f.readline()
    for i, line in enumerate(f, start=1):
        p.write(f"Case #{i}: ")
        i=int(line)
        while str(i)!="".join(sorted(str(i))):
            i-=1
        p.write(str(i)+"\n")
            
