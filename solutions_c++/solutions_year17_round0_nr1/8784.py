#include <iostream>
#include <stdio.h>
#include <algorithm> 
#include <vector>
#include <math.h>


using namespace std;

bool toodbien(string combinacion){
	for (int i = 0; i < combinacion.size(); ++i)
	{
		if(combinacion[i]!='+'){return true;}
	}
	return false;
}
string invertir(string punto,int movimientos,int empieza){
	for (int i = empieza; i < movimientos+empieza; ++i)
	{
		if(punto[i]=='+'){punto[i]='-';}else{
			punto[i]='+';
		}
	}
	return punto;
}
int main()
{
	int t,espatula,contador=0;
	string combinacion;
	scanf("%d",&t);
	bool flag=true;
	for (int i = 1; i <= t; ++i)
	{
		cin>>combinacion;
		scanf("%d",&espatula);
		flag=toodbien(combinacion);
		if(!flag){printf("Case #%d: %d\n",i,0);}
		string aux=combinacion;

		while(flag){
			for (int j = 0; j < (combinacion.size()-espatula) +1 ; ++j)
			{
				if(aux[j]=='-'){aux=invertir(aux,espatula,j);
				contador++;
				if(!toodbien(aux)){flag=false;printf("Case #%d: %d\n",i,contador); break;}
				//cout<<aux<<endl;
				}
			}
			break;
		}
		if(flag){printf("Case #%d: IMPOSSIBLE\n",i);}
		contador=0;
	}
	return 0;
}