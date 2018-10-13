class GooglerTest:
    def Test(self,st):
        lines = st.splitlines()
        maxtest = int(lines[0])

        for i in range(1,maxtest+1):
            words = lines[i].split()
            c = GCJ03(int(words[0]),int(words[1]))
            print("Case #" + str(i) + ": " + str(c.result))

class GCJ03:
    result=0
    def __init__(self,n,m):
        res=0
        for i in range(n,m+1):
            res += self.getcount(i,m)
        self.result = res
    def getcount(self,num,maxn):
        res=[]
        ns=str(num)
        length = len(ns)
        for i in range(1,length):
            t=['A' for n in range(length)]
            for j in range(length):
                t[j] = ns[(j+i)% length]
            it = int(''.join(t))
            if (it > num and it <= maxn):
                res.append(it)

        return len(set(res))
            
gt = GooglerTest()
gt.Test("""50
106 983
97 98
157 918
130 966
172 971
11 96
169 914
173 911
115 997
4 7
153 937
176 981
1 1
158 968
158 212
126 925
170 910
10 99
150 998
168 952
127 969
150 531
100 989
143 945
102 999
128 993
172 969
169 938
170 915
868 868
153 973
146 980
120 951
125 957
153 920
162 861
182 941
122 986
179 916
158 945
140 976
1 2
175 911
162 918
461 461
165 938
144 925
123 912
114 971
100 999
""")
