t = int(input())
i = 0
dict = {}
ncase = 0
while ncase < t + 1:
    if i == 0:
        if ncase == t:
            spd = []
            while any(dict):
                far = max(dict.keys())
                lim = dict[far]
                if spd != []:
                    if (des - far) / lim <= tdes:
                        spd = [far, lim]
                    else:
                        tdes = (des - far) / lim
                        spd = [far, lim]
                else:
                    tdes = (des - far) / lim
                    spd = [far, lim]
                dict.pop(far)
            print("Case #{}: {}".format(ncase, format(des/tdes,'.6f')))
            break
        elif ncase == 0:
            des, num = [int(s) for s in input().split(" ")]
            i = num
            ncase += 1
        else:
            spd = []
            while any(dict):
                far = max(dict.keys())
                lim = dict[far]
                if spd != []:
                    if (des - far) / lim <= tdes:
                        spd = [far, lim]
                    else:
                        tdes = (des - far) / lim
                        spd = [far, lim]
                else:
                    tdes = (des - far) / lim
                    spd = [far, lim]
                dict.pop(far)
            print("Case #{}: {}".format(ncase, format(des/tdes,'.6f')))
            des, num = [int(s) for s in input().split(" ")]
            dict = {}
            i = num
            ncase += 1
    else:
        Ki, Si = [int(s) for s in input().split(" ")]
        dict[Ki] = Si
        i -= 1
