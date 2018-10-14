import re

def process(line):
    res = re.match(r"(?P<s_max>\d+)\s+(?P<cases>\d*)", line)
    s_max, cases = res.groupdict()["s_max"], res.groupdict()["cases"]
    cases = [i for i in cases]
    cs = [int(i) for i in cases]
    
    invitados = 0
    res = calcular(cs, invitados)

    pars = (str(res), "".join(cases), )
    return "{0}".format(*pars)

def calcular(cs, invitados):
    ## invitados = 0
    s_p = 0
    n_p = 0
    ## res = "gotcha!"
    ## longitud = len(cs)
    for idx, c in enumerate(cs):
        n_p += c
        if idx <= s_p:
            s_p += c
        if n_p != s_p:
            ## res =  "NO"
            cs[idx-1] += 1
            invitados += 1
            return calcular(cs, invitados)
    return invitados

with open('A-small-attempt1.in') as f:
    content = f.readlines()

i = 0
for line in content:
    if i == 0:
        if not(int(line)>=1 & int(line)<=100):
            break;
    else:
        res = "Case #" + str(i) + ": " + process(line)
        with open("res.out", "a") as the_file:
            the_file.write(res + "\n")
    i += 1

##m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
##print m.groupdict()["first_name"]
##s_max + "->" + "".join(casesr)
