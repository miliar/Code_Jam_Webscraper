def calculate(A, B):
    result = 0
    for i in xrange(A, B-1):
        I = str(i)
        for j in xrange(i+1, B+1):
            J = str(j)
            for a in xrange(len(I)):
#                print I[a:]+I[:a], J
                if (I[a:]+I[:a] == J):
                    result += 1
                    break
                
    return result
            
    


input = """175 920
100 922
119 972
174 972
149 981
1 2
1 5
122 988
135 989
10 99
112 962
131 980
321 855
106 942
131 976
54 76
124 961
165 998
117 993
100 999
168 949
816 823
169 968
129 970
118 997
134 966
144 953
156 966
100 100
123 919
161 914
125 941
148 979
23 77
160 917
135 995
149 964
171 983
132 986
151 941
133 970
173 948
788 846
817 817
278 278
108 920
137 973
155 960
140 934
154 930""".split("\n")

output = ""
for i in xrange(len(input)):
    A, B = input[i].split(" ")
    output += "Case #" + str(i+1) + ": " + str(calculate(int(A), int(B))) + "\n"

print output
