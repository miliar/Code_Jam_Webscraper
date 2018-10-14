__author__ = 'kurtis'





def calculate_case(case_number, finput):
    case_info = map(float, finput.readline().split(" "))
    C = case_info[0]
    F = case_info[1]
    X = case_info[2]
    cookies = 0.0
    farms = 0
    current_time = 0.0

    while(cookies != X):
        if (C <= cookies):
            # we can invest!
            # but do we want to invest?
            time_remaining_to_win_without_more_investment = (X-cookies)/(2+farms*F)
            time_remaining_to_win_with_immediate_investment = (X-cookies+C)/(2+(farms+1)*F)
            if time_remaining_to_win_with_immediate_investment < time_remaining_to_win_without_more_investment:
                # Okay, it's better to invest!
                cookies -= C
                farms += 1.0
                # Now we have to calculate cookies to add over the next period of time
                time_remaining_to_invest = (C-cookies)/(2+farms*F)
                cookies += time_remaining_to_invest*(2+farms*F)
                current_time += time_remaining_to_invest
                print "We just invested!" + " Time: " + str(current_time) + " Cookies: " + str(cookies) + " Farms: " + str(farms)
            else:
                # It's better not to invest
                # This means that we should just play the game until the end
                cookies = X
                current_time += time_remaining_to_win_without_more_investment
        else:
            time_remaining_to_win_without_investment = (X-cookies)/(2+farms*F)
            time_remaining_to_invest = (C-cookies)/(2+farms*F)
            if time_remaining_to_invest < time_remaining_to_win_without_investment:
                # The opportunity to invest will arrive sooner than we will win
                current_time += time_remaining_to_invest
                cookies += time_remaining_to_invest*(2+farms*F)
                print "Waiting to invest!" + " Time: " + str(current_time) + " Cookies: " + str(cookies) + " Farms: " + str(farms)
            else:
                # We will win before we can invest
                current_time += time_remaining_to_win_without_investment
                cookies = X


    message = "Case #" + str(case_number) + ": " + str(round(current_time,7))
    return message

def print_message(message, foutput):
    print message
    foutput.write(message + "\n")

if __name__ == "__main__":
    fin = open('B-large.in', 'r')
    fout = open('problemb.out','w')
    number_of_cases = int(fin.readline())
    for i in xrange(number_of_cases):
        message = calculate_case(i+1, fin)
        print_message(message, fout)
    fin.close()
    fout.close()




