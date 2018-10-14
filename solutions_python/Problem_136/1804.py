import sys
def compute_test_case(t):
    c, f, x = map(float,sys.stdin.readline().split(' '))
    #print "\bc = ", c, "\nf = ", f, "\nx = ", x

    time_till = 0 #seconds
    time_to_500 = 0
    time_to_2000 = 0
    time_to_new_2000 = 0
    curr_rate = 2

    while True:
        time_to_500 = float(c)/curr_rate
        time_to_2000 = float(x)/curr_rate

        time_to_new_2000 = float(x)/(curr_rate+f) + time_to_500


        #print "result\n"
        #print time_to_500
        #print time_to_2000
        #print time_to_new_2000

        if time_to_new_2000 < time_to_2000:
            time_till += time_to_500
            curr_rate += f
        else:
            fh = open('output.txt','a')
            #print float(time_till+time_to_2000)
            fh.write("Case #"+str(t)+": "+str(float(time_till+time_to_2000)))
            fh.write("\n")
            fh.close()
            break
        #print time_till

    return

def main():
    for t in range(int(raw_input())):
        compute_test_case(t+1)

main()