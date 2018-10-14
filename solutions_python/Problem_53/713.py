#python3
f = open("./A-large.in")
out = open("./A-large.out","w")
times = int(f.readline().strip())
for i in range(times):
    N,K = [int(x) for x in f.readline().strip().split()]
    on = all([x=="1" for x in bin(K)[:1:-1].ljust(N,"0")[0:N]])
    out.write("Case #%s: %s\n"%(i+1, "ON" if on else "OFF"));
f.close()
out.close()
