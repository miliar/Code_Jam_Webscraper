
def is_tidy(x):
    largo = len(x)
    midlargo =  int(largo/2)
    if(largo==0 or largo==1):
        return True
    if(x[midlargo]>=x[midlargo-1]):
        return is_tidy(x[:midlargo]) and is_tidy(x[midlargo:])
    else:
        return False

def last_tidy(n):
    for x in range(n, 0, -1):
        if(is_tidy(str(x))):
            return x


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  entrada = input()# read a list of integers, 2 in this case
  print("Case #{}: {} ".format(i, last_tidy(int(entrada))))
