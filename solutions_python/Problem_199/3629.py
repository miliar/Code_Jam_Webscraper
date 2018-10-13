
import logging


def find_first(row, start):
    while start < len(row) and row[start] == '+':
        start += 1
    return start


def flippit(row,size,idx):
    modify = list(row)
    while size > 0:
        if modify[idx] == '+':
            modify[idx] = '-'
        else:
            modify[idx] = '+'
        idx += 1
        size -= 1
    return ''.join(modify)


def check(row):
    ok = False
    idx=0
    while idx < len(row) and row[idx] == '+':
        idx += 1
    if idx == len(row):
        ok = True
    return ok


def solve(row, size):
    logging.info("Solving " + row + " with " + str(size))
    nb_flip = 0
    idx = find_first(row, 0)
    while(idx < len(row)):
        logging.debug("idx=" + str(idx))
        if idx + size <= len(row):
            row = flippit(row, size, idx)
            nb_flip += 1
            logging.debug(row)
            idx = find_first(row, idx + 1)
        else:
            idx += size
    ok=check(row)
    if not ok:
        nb_flip="IMPOSSIBLE"
    logging.info(nb_flip)
    return str(nb_flip)

logging.basicConfig(level=logging.WARNING)

logging.info("Loading problem")
file = open("C:/Users/fabrice/CloudStation/Telechargements/A-large.in",'r')
res = open("C:/Users/fabrice/CloudStation/Telechargements/A-large.out",'w')
nb_case = file.readline()
logging.debug("Number of case : "+nb_case)
nb = 1
for line in file:
    # logging.debug(line)
    info = line.split()
    pancake_row = info[0]
    flipper_size = int(info[1])
    logging.debug("pancake_row=" + pancake_row)
    logging.debug("flipper_size="+str(flipper_size))
    result = solve(pancake_row, flipper_size)
    print ("Case #" + str(nb) + ": " + result)
    res.write("Case #" + str(nb) + ": " + result+'\n')
    nb += 1
    logging.debug("   NEXT    ")


file.close()
res.close()
logging.info("End")

