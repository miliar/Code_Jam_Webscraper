#GLOBALS
case_num = 1

def get_input(input):
        global case_num
        inp_arr = input.split('\n')
        for i, v in enumerate(inp_arr):  
                if i == 0:
                        continue
                audience = dict()  # for the current test case
                went_in = False
                v = v.split(" ")
                for j, c in enumerate(v[1]):
                        went_in = True
                        # if j == 0 and c == ' ':
                        #       continue
                        #if j == 0:
                        #        S_max = int(c)
                        #        continue 
                        audience[j] = int(c) # count from 0
                if went_in:
                        print so(audience)
                        # print audience
                        case_num += 1

def so(audience):
        global case_num
        extra_clap = 0
        if not audience:
                pass
        else:
                prev_clap = 0
                for i in range(len(audience)):
                        if prev_clap >= i:
                                prev_clap += audience[i] 
                        else:
                                extra_clap += i - prev_clap
                                prev_clap += i-prev_clap + audience[i]
        return "Case #{}: {}".format(str(case_num), str(extra_clap)) 

def do():
        global case_num
        case_num = 1
        a = raw_input("Enter: ")
        get_input(a)

if __name__ == "__main__":
        pass
        #a = raw_input("Enter: ")
        #print a
        #get_input("100\n 6 0000001\n 5 300041\n 6 5811014\n 3 4474\n 6 9999999\n 6 0900005\n 6 0910731\n 6 2299028\n 6 7401936\n 6 0000001\n 5 000607\n 6 4060001\n 6 2300801\n 6 2002003\n 0 1\n 5 000051\n 6 6723636\n 2 202\n 6 1111111\n 4 00007\n 6 0000001\n 6 0020074\n 3 5852\n 1 51\n 3 0401\n 3 6542\n 6 6000001\n 6 4000301\n 6 8000004\n 6 2211112\n 0 1\n 6 2835819\n 6 3700003\n 6 0009001\n 1 01\n 6 3080001\n 6 4000401\n 0 8\n 6 0006601\n 2 141\n 0 1\n 6 7540567\n 1 09\n 4 11111\n 4 20704\n 6 0221022\n 6 2200121\n 6 1221211\n 5 110011\n 0 3\n 6 2121111\n 0 1\n 2 201\n 6 0000001\n 6 0000001\n 6 1120111\n 6 6097392\n 2 701\n 5 990001\n 6 0824016\n 6 1220021\n 6 3007011\n 6 3080081\n 6 2021002\n 6 0000606\n 6 0222001\n 6 1200121\n 3 3136\n 3 0001\n 6 5812806\n 6 1111111\n 1 81\n 2 291\n 6 9000021\n 3 0201\n 1 01\n 6 1111202\n 6 1120221\n 6 0000001\n 6 4973653\n 6 0006801\n 5 000601\n 2 617\n 4 11211\n 6 0020001\n 6 6000001\n 2 651\n 6 2222002\n 1 91\n 6 1210122\n 4 60092\n 6 0000001\n 5 576188\n 6 4000001\n 6 1190001\n 0 2\n 0 1\n 0 1\n 2 081\n 6 9000009\n")
