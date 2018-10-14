t = input("")

def cookie(c, f, x):
    production = 2
    time_total = 0
    
    time_to_farm = float(c)/float(production)
    time_to_complete = float(x)/float(production)
    time_to_complete_with_new_farm = (float (x) / (float (production) + float(f)))

    a = float (time_total) + float(time_to_complete)
    b = float (time_total) + float(time_to_complete_with_new_farm) + float(time_to_farm)

    while b < a:
        time_total = float (time_total) + float (time_to_farm)
        production = float (production) + float(f)
 
        time_to_complete = (float(x) / float(production))
        time_to_farm = (float(c) / float(production))
        time_to_complete_with_new_farm = (float(x) / (float(production) + float(f)))
 
        a = float(time_total) + float(time_to_complete)
        b = float(time_total) + float(time_to_farm) + float(time_to_complete_with_new_farm)

    
    return a

for cases in range(t):
    i = raw_input("")
    inArray = i.split(" ")
    C = float(inArray[0])
    F = float (inArray[1])
    X = float (inArray[2])
    result = cookie(C, F, X)
    result_str = str (result)
    print "Case #" + str(cases + 1) + ": " + result_str
    
