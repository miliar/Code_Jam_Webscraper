num = int(raw_input())
output = [None]*num

for k in range(num):
        digits = [x for x in raw_input().strip()]

        l = len(digits)
        prev = "0"
        last_increase = 0
        first_decrease = l
        for i in range(l):
            if digits[i]>prev:
                last_increase = i
            elif digits[i]<prev:
                first_decrease = i
                break
            prev = digits[i]

        if first_decrease==l:
            output[k] = "".join(digits)
        else:
            digits[last_increase] = chr(ord(digits[last_increase])-1)
            digits[last_increase+1:] = ["9"]*(l-last_increase-1)

        if digits[0]=="0":
            digits = digits[1:]
        output[k] = "".join(digits)

for i, k in enumerate(output):
    print ("Case #%d: %s"%(i+1,k))
