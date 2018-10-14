import math

loop = input()
res = 0
no = 1
while loop>0:
	num = raw_input()
	row_before = int(num)
	line1 = raw_input()
	line1_s = line1.split(" ")
	p11 = line1_s[0]
	p12 = line1_s[1]
	p13 = line1_s[2]
	p14 = line1_s[3]
	line2 = raw_input()
	line2_s = line2.split(" ")
	p21 = line2_s[0]
	p22 = line2_s[1]
	p23 = line2_s[2]
	p24 = line2_s[3]
	line3 = raw_input()
	line3_s = line3.split(" ")
	p31 = line3_s[0]
	p32 = line3_s[1]
	p33 = line3_s[2]
	p34 = line3_s[3]
	line4 = raw_input()
	line4_s = line4.split(" ")
	p41 = line4_s[0]
	p42 = line4_s[1]
	p43 = line4_s[2]
	p44 = line4_s[3]
	
	num = raw_input()
	row_after = int(num)
	line1 = raw_input()
	line1_s = line1.split(" ")
	pa11 = line1_s[0]
	pa12 = line1_s[1]
	pa13 = line1_s[2]
	pa14 = line1_s[3]
	line2 = raw_input()
	line2_s = line2.split(" ")
	pa21 = line2_s[0]
	pa22 = line2_s[1]
	pa23 = line2_s[2]
	pa24 = line2_s[3]
	line3 = raw_input()
	line3_s = line3.split(" ")
	pa31 = line3_s[0]
	pa32 = line3_s[1]
	pa33 = line3_s[2]
	pa34 = line3_s[3]
	line4 = raw_input()
	line4_s = line4.split(" ")
	pa41 = line4_s[0]
	pa42 = line4_s[1]
	pa43 = line4_s[2]
	pa44 = line4_s[3]

	check = 0

	if row_before==1:
		if row_after==1:
			if p11==pa11 or p11==pa12 or p11==pa13 or p11==pa14:
				output = p11 
				check = check+1
			if p12==pa11 or p12==pa12 or p12==pa13 or p12==pa14:
				output = p12
				check = check+1
			if p13==pa11 or p13==pa12 or p13==pa13 or p13==pa14:
				output = p13 
				check = check+1
			if p14==pa11 or p14==pa12 or p14==pa13 or p14==pa14:
				output = p14 
				check = check+1
		if row_after==2:
			if p11==pa21 or p11==pa22 or p11==pa23 or p11==pa24:
				output = p11 
				check = check+1
			if p12==pa21 or p12==pa22 or p12==pa23 or p12==pa24:
				output = p12
				check = check+1
			if p13==pa21 or p13==pa22 or p13==pa23 or p13==pa24:
				output = p13 
				check = check+1
			if p14==pa21 or p14==pa22 or p14==pa23 or p14==pa24:
				output = p14 
				check = check+1
		if row_after==3:
			if p11==pa31 or p11==pa32 or p11==pa33 or p11==pa34:
				output = p11 
				check = check+1
			if p12==pa31 or p12==pa32 or p12==pa33 or p12==pa34:
				output = p12
				check = check+1
			if p13==pa31 or p13==pa32 or p13==pa33 or p13==pa34:
				output = p13 
				check = check+1
			if p14==pa31 or p14==pa32 or p14==pa33 or p14==pa34:
				output = p14 
				check = check+1
		if row_after==4:
			if p11==pa41 or p11==pa42 or p11==pa43 or p11==pa44:
				output = p11 
				check = check+1
			if p12==pa41 or p12==pa42 or p12==pa43 or p12==pa44:
				output = p12
				check = check+1
			if p13==pa41 or p13==pa42 or p13==pa43 or p13==pa44:
				output = p13 
				check = check+1
			if p14==pa41 or p14==pa42 or p14==pa43 or p14==pa44:
				output = p14 
				check = check+1

	if row_before==2:
		if row_after==1:
			if p21==pa11 or p21==pa12 or p21==pa13 or p21==pa14:
				output = p21 
				check = check+1
			if p22==pa11 or p22==pa12 or p22==pa13 or p22==pa14:
				output = p22
				check = check+1
			if p23==pa11 or p23==pa12 or p23==pa13 or p23==pa14:
				output = p23 
				check = check+1
			if p24==pa11 or p24==pa12 or p24==pa13 or p24==pa14:
				output = p24 
				check = check+1
		if row_after==2:
			if p21==pa21 or p21==pa22 or p21==pa23 or p21==pa24:
				output = p21 
				check = check+1
			if p22==pa21 or p22==pa22 or p22==pa23 or p22==pa24:
				output = p22
				check = check+1
			if p23==pa21 or p23==pa22 or p23==pa23 or p23==pa24:
				output = p23 
				check = check+1
			if p24==pa21 or p24==pa22 or p24==pa23 or p24==pa24:
				output = p24 
				check = check+1
		if row_after==3:
			if p21==pa31 or p21==pa32 or p21==pa33 or p21==pa34:
				output = p21 
				check = check+1
			if p22==pa31 or p22==pa32 or p22==pa33 or p22==pa34:
				output = p22
				check = check+1
			if p23==pa31 or p23==pa32 or p23==pa33 or p23==pa34:
				output = p23 
				check = check+1
			if p24==pa31 or p24==pa32 or p24==pa33 or p24==pa34:
				output = p24 
				check = check+1
		if row_after==4:
			if p21==pa41 or p21==pa42 or p21==pa43 or p21==pa44:
				output = p21 
				check = check+1
			if p22==pa41 or p22==pa42 or p22==pa43 or p22==pa44:
				output = p22
				check = check+1
			if p23==pa41 or p23==pa42 or p23==pa43 or p23==pa44:
				output = p23 
				check = check+1
			if p24==pa41 or p24==pa42 or p24==pa43 or p24==pa44:
				output = p24 
				check = check+1

	if row_before==3:
		if row_after==1:
			if p31==pa11 or p31==pa12 or p31==pa13 or p31==pa14:
				output = p31 
				check = check+1
			if p32==pa11 or p32==pa12 or p32==pa13 or p32==pa14:
				output = p32
				check = check+1
			if p33==pa11 or p33==pa12 or p33==pa13 or p33==pa14:
				output = p33 
				check = check+1
			if p34==pa11 or p34==pa12 or p34==pa13 or p34==pa14:
				output = p34 
				check = check+1
		if row_after==2:
			if p31==pa21 or p31==pa22 or p31==pa23 or p31==pa24:
				output = p31 
				check = check+1
			if p32==pa21 or p32==pa22 or p32==pa23 or p32==pa24:
				output = p32
				check = check+1
			if p33==pa21 or p33==pa22 or p33==pa23 or p33==pa24:
				output = p33 
				check = check+1
			if p34==pa21 or p34==pa22 or p34==pa23 or p34==pa24:
				output = p34 
				check = check+1
		if row_after==3:
			if p31==pa31 or p31==pa32 or p31==pa33 or p31==pa34:
				output = p31 
				check = check+1
			if p32==pa31 or p32==pa32 or p32==pa33 or p32==pa34:
				output = p32
				check = check+1
			if p33==pa31 or p33==pa32 or p33==pa33 or p33==pa34:
				output = p33 
				check = check+1
			if p34==pa31 or p34==pa32 or p34==pa33 or p34==pa34:
				output = p34 
				check = check+1
		if row_after==4:
			if p31==pa41 or p31==pa42 or p31==pa43 or p31==pa44:
				output = p31 
				check = check+1
			if p32==pa41 or p32==pa42 or p32==pa43 or p32==pa44:
				output = p32
				check = check+1
			if p33==pa41 or p33==pa42 or p33==pa43 or p33==pa44:
				output = p33 
				check = check+1
			if p34==pa41 or p34==pa42 or p34==pa43 or p34==pa44:
				output = p34 
				check = check+1

	if row_before==4:
		if row_after==1:
			if p41==pa11 or p41==pa12 or p41==pa13 or p41==pa14:
				output = p41 
				check = check+1
			if p42==pa11 or p42==pa12 or p42==pa13 or p42==pa14:
				output = p42
				check = check+1
			if p43==pa11 or p43==pa12 or p43==pa13 or p43==pa14:
				output = p43 
				check = check+1
			if p44==pa11 or p44==pa12 or p44==pa13 or p44==pa14:
				output = p44 
				check = check+1
		if row_after==2:
			if p41==pa21 or p41==pa22 or p41==pa23 or p41==pa24:
				output = p41 
				check = check+1
			if p42==pa21 or p42==pa22 or p42==pa23 or p42==pa24:
				output = p42
				check = check+1
			if p43==pa21 or p43==pa22 or p43==pa23 or p43==pa24:
				output = p43 
				check = check+1
			if p44==pa21 or p44==pa22 or p44==pa23 or p44==pa24:
				output = p44 
				check = check+1
		if row_after==3:
			if p41==pa31 or p41==pa32 or p41==pa33 or p41==pa34:
				output = p41 
				check = check+1
			if p42==pa31 or p42==pa32 or p42==pa33 or p42==pa34:
				output = p42
				check = check+1
			if p43==pa31 or p43==pa32 or p43==pa33 or p43==pa34:
				output = p43 
				check = check+1
			if p44==pa31 or p44==pa32 or p44==pa33 or p44==pa34:
				output = p44 
				check = check+1
		if row_after==4:
			if p41==pa41 or p41==pa42 or p41==pa43 or p41==pa44:
				output = p41 
				check = check+1
			if p42==pa41 or p42==pa42 or p42==pa43 or p42==pa44:
				output = p42
				check = check+1
			if p43==pa41 or p43==pa42 or p43==pa43 or p43==pa44:
				output = p43 
				check = check+1
			if p44==pa41 or p44==pa42 or p44==pa43 or p44==pa44:
				output = p44 
				check = check+1

	if check==0:
		output = 'Volunteer cheated!'
	if check>1:
		output = 'Bad magician!'

	nos = str(no)
	outputs = str(output)
	print 'Case #'+nos+': '+outputs
	output = 0
	no = no+1
	loop = loop-1