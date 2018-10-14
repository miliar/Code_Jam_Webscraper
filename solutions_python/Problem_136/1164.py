__author__ = 'fabrizio'

with open("input.txt") as fin:
    with open("output.txt","w") as fout:
        T=int(fin.readline().strip())
        for t in range(1,T+1):
            C,F,X=map(float,fin.readline().strip().split())
            time=0.
            cookies_sec=2.
            min_time=X
            while True:
                time_result=time+X/cookies_sec
                if time_result>min_time:
                    break
                min_time=time_result

                time_for_farm=C/cookies_sec
                time+=time_for_farm
                cookies_sec+=F
            fout.write("Case #"+str(t)+": "+str(min_time)+"\n")

