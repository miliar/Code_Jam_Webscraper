import io

with open("A-large.in") as fin:
    with open("A.out", "w") as fout:
        T = int(fin.readline())
        for i in range(T):
            (N, K) = tuple(int(x) for x in fin.readline().split(" "))
            fout.write("Case #" + str(i+1) + ": ")
            if K % 2**N == 2**N - 1:
                fout.write("ON\n")
            else:
                fout.write("OFF\n")

            
            
