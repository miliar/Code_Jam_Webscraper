def main():
	f = open("B-large.in","r")
	ListOfLetters = f.readlines()
	f.close()
	f = open("Result.txt","w")
	f.close
	i=0
	for text in ListOfLetters:
		if(i==0):
			Casos=int(text)
		else:
			Mat=text.split( )
			C=float(Mat[0])
			F=float(Mat[1])
			X=float(Mat[2])						
			Farms=0
			TiempoTerminar=0.0000000
			TiempoGranja=0.0000000
			TiempoTotal=0.0000000
			Cookies=0
			while (Cookies<X):
				TiempoGranja=(C)/((2+(F*Farms)))
				TiempoTerminar=(X)/((2+(F*Farms)))
				TiempoFuturo=(X)/(2+((F*(Farms+1))))
				Calc=TiempoGranja+TiempoFuturo
				if (TiempoGranja<TiempoTerminar and Calc<TiempoTerminar):
					Farms=Farms+1
					TiempoTotal=TiempoTotal+TiempoGranja
				else:
					TiempoTotal=TiempoTotal+TiempoTerminar
					f = open("Result.txt","a")
					f.write("Case #"+str(i)+": "+str(TiempoTotal)+"\n")
					f.close
					break
		i=i+1





						

			


if __name__=='__main__' :
    main() 			