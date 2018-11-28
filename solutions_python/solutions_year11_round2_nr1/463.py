
entrada = file('A-large.in')
salida = file('output-large.ou', 'w')
casos = int(entrada.readline())

def calculateWPS(equipo):
	ganados = 0
	totales = 0
	for i in equipo:
		if i != '.':
			totales += 1
			ganados += int(i)
			
	return ganados / float(totales)

	
	

for w in range(casos):
	equipos = int(entrada.readline())
	
	schedule = []
	
	for i in range(equipos):
		schedule.append(list(entrada.readline().rstrip('\n')))
	
	WPs = []
	
	#Calculamos los wps
	for i in schedule:
		WPs.append(calculateWPS(i))
	
	#print WPs
	
	OWPs = []
	
	for i in range(len(schedule)):
		totalOponents = 0
		wpsOponents = 0
		for j in range(len(schedule[i])):
			if schedule[i][j] != '.': #Significa que juge contra j 
				temp = schedule[j][:]
				del temp[i]
				wpsOponents += calculateWPS(temp)
				totalOponents += 1
			
		OWPs.append(wpsOponents / float(totalOponents))
		
	OOWPs = []
	for i in range(len(schedule)):
		totalOponents = 0
		owpsOponents = 0
		for j in range(len(schedule[i])):
			if schedule[i][j] != '.':
				totalOponents += 1
				owpsOponents += OWPs[j]
			
		OOWPs.append(owpsOponents / float(totalOponents))
	
	salida.write('Case #%d:\n' % (w+1))
	
	for i in range(len(WPs)):
		try:
			RPI = 0.25 * WPs[i] + 0.50 * OWPs[i] + 0.25 * OOWPs[i]
		except IndexError:
			#print WPs
			#print OWPs
			#print OOWPs
			pass
		salida.write('%.10f\n' % RPI)
	
	
				
				
				
				
				
				
				
				
				
				
				
				
				
				
	
