for linur in range(int(input(""))):
	inntok = [float(x) for x in input("").split(" ")]
	c = inntok[0]
	f = inntok[1]
	x = inntok[2]
	clickGildi = 2.0 # 2 kökur á sek fyrir að ýta á köku
	fjoldiFarm = 0.0
	timi = 0.0
	while(c / (clickGildi + f*fjoldiFarm) + x / (clickGildi + f*(fjoldiFarm+1)) < x / (clickGildi + f*fjoldiFarm)): # meðan það er gáfulegt að kaupa
		timi += c / (clickGildi + f*fjoldiFarm)
		fjoldiFarm += 1

	timi += x / (clickGildi + f*fjoldiFarm)

	print("Case #" + str(linur+1) + ": " + str(timi))
