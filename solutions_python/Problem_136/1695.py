def get_time_to_objective(base_cookie_gain_rate, base_farm_gain_rate, price_farm, objective):
    # On va simuler chaque situation, d'abord en achetant 0 fermes, puis en achetant 1 ferme, puis 2, jusque objective/price_farm
    number_of_simulation = int(objective/price_farm) + 1
    calculated_times = []
    for number_of_farm_to_buy in range(0, number_of_simulation):
        time = 0
        cookie_gain_rate = base_cookie_gain_rate
        # On doit acheter number_of_farm_to_buy le plus rapidement possible
        for number_of_bought_farm in range(0, number_of_farm_to_buy):
            # On regarde le temps qu'il nous faut pour acheter cette ferme
            time_to_buy_this_farm = price_farm/cookie_gain_rate
            # On rajoute ce temps au pool final de temps
            time += time_to_buy_this_farm
            # On rajoute le gain en cookie/sec
            cookie_gain_rate += base_farm_gain_rate
        # On arrive à la fin avec le nombre de ferme qu'il nous faut
        # Il nous reste plus qu'à rajouter le temps qu'il faudra pour arriver à objective cookies.
        time += objective/cookie_gain_rate
        calculated_times.append(time)

    # A la fin, on retourne le temps le plus court
    return min(calculated_times)




fInput = open("input2.txt", "r")
fOutput = open("output2.txt", "w")
# On lit la première ligne
number_of_case = int(fInput.readline())
line = fInput.readline()
i = 0
while i < number_of_case:
    # On récupère les données
    data_line = line.split(" ")
    # On définit les variables du problèmes
    base_cookie_gain_rate = 2
    price_farm = float(data_line[0])
    base_farm_gain_rate = float(data_line[1])
    objective = float(data_line[2])
    fOutput.write("Case #" + str(i + 1) + ": " + str(round(get_time_to_objective(base_cookie_gain_rate, base_farm_gain_rate, price_farm, objective), 7)) + "\n")
    line = fInput.readline()
    i += 1
    print(str(round((i/number_of_case)*100)) + "%")
fInput.close()
fOutput.close()