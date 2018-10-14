kacdefa = input()
index = 1
while(index <= kacdefa):
	
	ilkMatris = []
	ikiMatris = []	
	ilk = input()
	ilkMatris.append(raw_input().split(" "))
	ilkMatris.append(raw_input().split(" "))
	ilkMatris.append(raw_input().split(" "))
	ilkMatris.append(raw_input().split(" "))
	iki = input()
	ikiMatris.append(raw_input().split(" "))
	ikiMatris.append(raw_input().split(" "))
	ikiMatris.append(raw_input().split(" "))
	ikiMatris.append(raw_input().split(" "))


	cevapKume = [] 
	for i in ilkMatris[ilk-1]:
		if( i in ikiMatris[iki-1]):
			cevapKume.append(i)
	#print "Case #%s:"%index

	if( len(cevapKume) == 1):
		print "Case #%s:"%index,cevapKume[0]
	elif(cevapKume == []):
		print "Case #%s:"%index,"Volunteer cheated!"
	else:
		print "Case #%s:"%index,"Bad magician!"
	index = index +1
