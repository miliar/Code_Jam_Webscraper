import logging

def check(number):
    ret=True
    strnb = str(number)
    idx=0
    while ret and idx < len(strnb)-1:
        if int(strnb[idx]) > int(strnb[idx+1]):
            ret=False
        else:
            idx += 1
    return(ret)

def solve(number):
    ret = check(number)
    while(not ret):
        number -= 1;
        ret = check(number)
    return(number)


logging.basicConfig(level=logging.WARNING)

logging.info("Loading problem")
file = open("C:/Users/fabrice/CloudStation/Telechargements/B-small-attempt0.in",'r')
res = open("C:/Users/fabrice/CloudStation/Telechargements/B-small-attempt0.out",'w')
nb_case = file.readline()
logging.debug("Number of case : "+nb_case)
nb = 1
for line in file:
    last_number=int(line)
    logging.info("Case "+str(nb) + " ===> " + str(last_number))

    ret=solve(last_number)
    print("Case #"+str(nb)+": "+str(ret))
    res.write("Case #"+str(nb)+": "+str(ret)+'\n')
    nb += 1

file.close()
res.close()
logging.info("End")

