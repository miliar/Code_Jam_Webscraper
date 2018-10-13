def split(str):
    return list ( str )

def final_total(total_km, distance, speed):
    return float(total_km/(float((total_km-distance)/speed)))

def remaining_hours(total_km, distance, speed):
    return float((total_km-distance)/speed)

def final_speed(total_km, hours):
    return float(total_km/hours)

def calculate_speed(total_km, number_of_horses):
    if number_of_horses == 1:
        inputs2 = raw_input().split()
        distance = float(inputs2[0])
        speed = float(inputs2[1])
        return final_total(total_km, distance, speed)
    last_list = []
    max_hours_list = []
    for k in range(0, number_of_horses):
        inputs2 = raw_input().split()
        distance = float(inputs2[0])
        speed = float(inputs2[1])
        if k == 0:
            max_hours = remaining_hours(total_km, distance, speed)
            max_hours_list.append(max_hours)
            last_list = [distance, speed, max_hours]
        else:
            max_hours = remaining_hours(total_km, distance, speed)
            if last_list[-1] > max_hours:
                max_hours_list.append(last_list[-1])
            elif last_list[-1] < max_hours:
                last_list = [distance, speed, max_hours]
                max_hours_list.append(max_hours)
    return final_speed(total_km, max(max_hours_list))

test_cases = int(raw_input())
for i in range (0, test_cases):
    inputs = raw_input().split()
    total_km = float(inputs[0])
    number_of_horses = int(inputs[1])
    print("Case #" + str(i+1) + ": %.6f" % calculate_speed(total_km, number_of_horses))
