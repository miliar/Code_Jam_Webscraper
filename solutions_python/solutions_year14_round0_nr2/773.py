import math
init_power = 2.0

def shouldBuyFarm(rest_product, current_power, farm_cost, farm_power):
    time1 = rest_product / current_power
    time2 = (farm_cost + rest_product) / (current_power + farm_power)
    return time1 > time2
   
def getAnswer(input_arr):
    farm_cost = input_arr[0]
    farm_power = input_arr[1]
    rest_product = input_arr[2]
    current_power = init_power
    elapsed = 0.0
    #wait for the moment to buy first farm
    rest_product = rest_product - farm_cost
    elapsed = elapsed + (farm_cost / current_power)
    while shouldBuyFarm(rest_product, current_power, farm_cost, farm_power):       
        current_power = current_power + farm_power
        elapsed = elapsed + (farm_cost / current_power)
    elapsed = elapsed + (rest_product / current_power)
    return elapsed
    
test_cnt = input()
outputs = []
for num in range(0, test_cnt):
    input_arr = [float(v) for v in raw_input().split(" ")]
    outputs.append(getAnswer(input_arr))
    
for i,v in enumerate(outputs):
    print "Case #%d: %f" % ((i + 1), v)

