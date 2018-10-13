#@author RaunS
#written to just get me over the round

inputf = r"K:\Codes\code jam solutions\2014 Round 1\Problem C Deceitful War\D-large.in"
output = r"K:\Codes\code jam solutions\2014 Round 1\Problem C Deceitful War\SampleOutputlarge.txt"

ifp = open(inputf, 'r')
t = int(ifp.readline().strip())

answer = ''
for i in range(t):
    n = int(ifp.readline().strip())
    naomi = map(float, ifp.readline().strip().split(' '))
    ken = map(float, ifp.readline().strip().split(' '))
    naomi.sort()
    ken.sort(reverse=True)
    naomi2 = list(naomi)
    ken2 = list(ken)
    war, dec_war = 0, 0

    n_dash = n
    for u in range(n):
        chosen_naomi = naomi[u]
        loc_ken_bigger = sum(u>chosen_naomi for u in ken)
        if loc_ken_bigger:
            loc = loc_ken_bigger-1
        else:
            war+=1
            loc = n_dash-1
        chosen_ken = ken.pop(loc)
        n_dash-=1
    naomi2.sort(reverse=True)
    n_dash = n
    for u in range(n):
        chosen_ken = ken2[u]
        loc_naomi_bigger = sum(u>chosen_ken for u in naomi2)
        if loc_naomi_bigger:
            dec_war+=1
            loc = loc_naomi_bigger-1
            
        else:
            loc = n_dash-1
            
        chosen_naomi = naomi2.pop(loc)
        
        n_dash-=1
    answer+='Case #%d: %d %d\n' %(i+1, dec_war, war)
    if dec_war<war:
        break    
ofp = open(output, 'w')
ofp.write(answer)
ofp.close()
ifp.close()


