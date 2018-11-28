__author__ = 'iToR'
import sys

file_name = "B-small-attempt0.in"

def computeUseTime(init_cookie_per_sec, parameter, farm_buy):
    cookie_farm_cost    = float(parameter[0])
    cookie_farm_income  = float(parameter[1])
    target_cookie       = float(parameter[2])
    cookie_per_sec = init_cookie_per_sec
    req_time = 0
    for i in range(farm_buy):
        req_time += cookie_farm_cost/cookie_per_sec
        cookie_per_sec += cookie_farm_income
    req_time += target_cookie/cookie_per_sec
    req_time = round(req_time, 7)
    return req_time

def generateOutput(ans, case):
    ans_file = open("answer.txt", "a")
    ans_file.write("Case #" + str(case) + ": ")
    ans_file.write(str(ans) + "\n")

f = open(file_name)

input_num = int(f.readline())

for i in range(1,input_num+1):
    input_parameter = f.readline()
    parameter       = input_parameter.split()

    cookie_farm_cost    = float(parameter[0])
    cookie_farm_income  = float(parameter[1])
    target_cookie       = float(parameter[2])

    req_time = target_cookie/2.0
    req_time = round(req_time, 7)
    farm_buy = 1
    while True:
        test_req_time = computeUseTime(2.0, parameter, farm_buy)
        if req_time < test_req_time:
            break
        else:
            req_time = test_req_time
            farm_buy += 1
    generateOutput(req_time, i)
