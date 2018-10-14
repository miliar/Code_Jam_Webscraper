#use python3
def main():
    file = open('2.txt','r')
    file_out = open('2_output.txt','w')

    test_cases = int(file.readline())

    for test in range(1,test_cases+1):
        case = [float(x) for x in file.readline().split()]
        c = case[0] #cost of farm
        f = case[1] #farm cookies per second
        x = case[2] #win amount (cookies you haven't spent on farms)

        cps = 2 #cookies per second
        farms = 0
        cookies = 0
        time = 0

        while True:
            time_to_buy_farm = c/cps #time to regain cookies lost by buying farm

            time_to_win = x/cps #time needed to win in current cookies per second

            #time needed to win if you buy another farm
            farm_worth = time_to_buy_farm + x/(cps+f)

            if time_to_win>farm_worth:
                time+=time_to_buy_farm
                cps+=f
            else:
                time+=time_to_win
                break

        file_out.write("Case #"+str(test)+": "+str(time)+"\n")

    file.close()
    file_out.close()
main()