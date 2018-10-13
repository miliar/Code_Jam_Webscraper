with open("output.txt","wt") as output:
    with open("input.txt","r") as f:
        trial = int(f.readline())
        for t in range(trial):
            dest,num = (int(n) for n in f.readline().split(" "))
            answer = float("inf")
            for n in range(num):
                pos,speed = (int(n) for n in f.readline().split(" "))
                answer = min(answer,dest / ((dest-pos) / speed))
            print("Case #%d: %.6f" % (t+1,answer),file = output)
