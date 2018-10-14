{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf190
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural

\f0\fs24 \cf0 def main():\
	inp = open('input.txt')\
	output = open('output.txt', 'w')\
	cases = inp.readline().replace("\\n", "")\
\
	for n in range(0, int(cases)):\
		line = inp.readline().replace("\\n", "")\
		list2 = line.split()\
		C, F, X = float(list2[0]), float(list2[1]), float(list2[2])\
		cookies = 0\
		time = 0.0\
		R = 2.0\
		while(True):\
			temp1 = time + X/R\
			temp2 = time + (min(X, C))/R + X/(R+F)\
			if temp1<temp2:\
				output.write("Case #"+str(n+1)+": "+str(temp1)+"\\n")\
				break\
			else:\
				time = time+(C/R)\
				R = R+F\
\
\
\
\
\
\
	inp.close()\
	output.close()\
\
main()\
}