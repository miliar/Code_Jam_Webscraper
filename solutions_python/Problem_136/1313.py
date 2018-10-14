inputFile = open('B-large.in', 'rb')

outputFile = open('B-large.out', 'w')

inputText = inputFile.read().splitlines()

T = int(inputText[0])

for i in range(1, T+1):

    row = inputText[i].split(" ")

    #farm cost
    C = float(row[0])

    #cookie increase
    F = float(row[1])

    #winning number
    X = float(row[2])

    cookie_rate = 2.0
    time_elapsed = 0.0

    time_to_win_1 = X / cookie_rate
    time_for_farm = C / cookie_rate
    time_to_win_2 = X / (cookie_rate + F) # initialising the value

    while time_to_win_1 > time_for_farm + time_to_win_2:

        time_elapsed += time_for_farm

        # update time to win for this iteration
        time_to_win_1 = time_to_win_2

        cookie_rate += F
        time_for_farm = C / cookie_rate
        time_to_win_2 = X / (cookie_rate + F)

    time_elapsed += time_to_win_1

    outputFile.write("Case #%d: %.7f\n" % (i, time_elapsed))

inputFile.close()
outputFile.close()