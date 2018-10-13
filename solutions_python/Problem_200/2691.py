
def is_tidy(x):
    largo = len(x)
    midlargo =  int(largo/2)
    if(largo==0 or largo==1):
        return True
    try:
        if(x[midlargo]>=x[midlargo-1] and x[midlargo]<=x[midlargo+1] ):
            return is_tidy(x[:midlargo]) and is_tidy(x[midlargo:])
    except IndexError:
        if(x[midlargo]>=x[midlargo-1]):
            return is_tidy(x[:midlargo]) and is_tidy(x[midlargo:])
    else:
        return False

def make_tidy(n):
    flag = False
    for x in range(len(n)):
        #print(x)
        try:
            if(n[x]>n[x+1]):
                #print("no exploto")
                #print("antes "+n)
                ncar = int(n[x])
                n = n[:x+1]+n[x+1].replace(n[x+1],"9")+n[x+2:]
                if(not flag):
                    flag = True
                    n = n[:x]+n[x].replace(n[x],str(ncar-1))+n[x+1:]
                #print("despues "+n)
        except IndexError:
            #print("exploto")
            return n
    return n

def last_tidy(n):
    while(not is_tidy(n)):
        n = make_tidy(n)
    return int(n)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  entrada = input()# read a list of integers, 2 in this case
  print("Case #{}: {} ".format(i, last_tidy(entrada)))
