def is_recycled(n, m):
    n = str(n)
    m = str(m)
    if len(n) != len(m):
        return False
    
    check = m
    while check != n:
        check = check[-1] + check[0:len(check)-1]
        if check == m:
            return False
    return True

lines = """69 95
108 951
169 924
100 999
679 679
189 969
172 936
137 928
171 942
188 939
103 966
119 964
132 910
1 1
115 925
100 999
149 959
176 984
100 960
119 921
130 963
187 989
2 5
156 954
111 111
166 962
163 910
155 920
116 970
178 979
156 927
122 974
10 20
107 920
289 417
166 999
181 957
147 944
514 544
1 2
144 923
122 933
190 979
119 946
797 937
183 976
108 954
163 964
184 941
169 948""".split("\n")
case = 1
for line in lines:
    arr = line.split()
    A = int(arr[0])
    B = int(arr[1])
    count = 0
    for i in range(A, B):
        for j in range(i + 1, B + 1):
            if is_recycled(i, j):
                count += 1
    print 'Case #' + str(case) + ': ' + str(count)
    case += 1
