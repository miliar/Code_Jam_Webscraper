'''
Created on Apr 13, 2014

@author: Adam Speakman
'''
in_file = open("B-large.in")
out_file = open("B-large.out", "w")
num_cases = int(in_file.readline())

C = 0.0 # Farm cost
C_ps = 2.0 # Cookies per second
F = 2.0 # Farm benefit in CPS
X = 2000.0 # Winning value

# 31.25
# 125

def time_to_win(cps):
    return X / cps

def next_farm_time():
    return C / C_ps

def buy_farm():
    # If we buy another farm, will that get us to X faster than just going straight there?
    straight_to_X = time_to_win(C_ps)
    # Buying another farm costs us time-to-next-farm, plus the time-to-X at the new CPS
    buy_a_farm = next_farm_time() + time_to_win(C_ps + F)
    return straight_to_X > buy_a_farm

for case in range(0, num_cases):
    vals = in_file.readline().split()
    C = float(vals[0])
    F = float(vals[1])
    X = float(vals[2])
    time_taken = 0.0
    C_ps = 2.0
    while buy_farm():
        time_taken += next_farm_time()
        C_ps += F
    time_taken += time_to_win(C_ps)
    out_str = "Case #" + str((case + 1)) + ": "
    out_str += "{:.7f}".format(time_taken) 
    out_str += "\n"
    out_file.write(out_str)

out_file.close()
        


    