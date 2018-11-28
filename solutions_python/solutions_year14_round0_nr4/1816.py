
def deceitful_war(ken, naomi):
    ken_desc = sorted(ken, reverse=True)
    naomi_asc = sorted(naomi)
    deceit = 0
    for i in range(len(ken_desc)):
        tobeat = ken_desc[i]
        for j in range(len(naomi_asc)):
            if naomi_asc[j] > tobeat:
                deceit += 1
                naomi_asc[j] = -1
                break

    ken_asc = sorted(ken)
    war = 0
    for i in range(len(naomi)):
        tobeat = naomi[i]
        for j in range(len(ken_asc)):
            if ken_asc[j] > tobeat:
                war += 1
                ken_asc[j] = -1
                break
    war = len(ken) - war
    return deceit, war

def main():
    t = int(raw_input())
    for i in range(1, t+1):
        blocks = int(raw_input())
        naomi = [float(x) for x in raw_input().split()]
        ken = [float(x) for x in raw_input().split()]
        deceit, war = deceitful_war(ken, naomi)
        print('Case #{}: {} {}'.format(i, deceit, war))
if __name__ == '__main__':
    main()
