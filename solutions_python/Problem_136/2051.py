def time(farm_price, farm_speed, victory, base_speed):
   building_time = 0
   n_of_farms = 0
   past_time = victory / base_speed
   while True:
      winning_time = victory / (base_speed + n_of_farms * farm_speed)
      total_time = winning_time + building_time
      if (total_time > past_time) :
         return past_time
      past_time = total_time
      building_time += farm_price / (base_speed + n_of_farms * farm_speed)
      n_of_farms += 1

def output(ans, i):
   out.write("Case #" + str(i + 1) + ": ")
   out.write(str(ans))
   out.write("\n")
      
global_base_speed = 2

f = open('input.txt', 'r')
out = open('output.txt', 'w')

T = int(f.readline())

for i in xrange(T):
    line = f.readline().split(" ")
    output(time(float(line[0]), float(line[1]), float(line[2]), global_base_speed), i)

f.close()
out.close()
