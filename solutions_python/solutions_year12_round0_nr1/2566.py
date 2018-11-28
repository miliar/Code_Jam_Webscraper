import sys

filename_in = sys.argv[1]
filename_out = sys.argv[2]

ex_input = " qejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
ex_output = " zourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"

trans_dic = {}
for i in range(len(ex_input)) :
    trans_dic[ex_input[i]] = ex_output[i]
string = "abcdefghijklmnopqrstuvwxyz"
not_founds = [c for c in string]
rest = None
for c in string :
    if c in trans_dic.keys() :
        not_founds.remove(trans_dic[c])
    else :
        rest = c
if bool(rest) :
    trans_dic[rest] = not_founds[0]

f_in = open(filename_in, "r")
f_out = open(filename_out, "w")

cases = f_in.read().split("\n")[1:-1]
trans_cases = []
for case in cases :
    trans_case = ''.join([trans_dic[c] for c in case])
    trans_cases.append(trans_case)

for i in range(len(trans_cases)) :
    trans_cases[i] = 'Case #' + str(i+1) + ': ' + trans_cases[i]

f_out.write('\n'.join(trans_cases))
