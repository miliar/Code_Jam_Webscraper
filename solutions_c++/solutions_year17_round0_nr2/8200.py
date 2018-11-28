#include<iostream>
#include<cstdio>
#include<string>
using namespace std;


string resolucion ( string numero)
{
	int posicion = numero.size()-1;
	while(posicion!=0)
	{
		if( numero.at(posicion) < numero.at(posicion-1))
		{
			for(int i = posicion;i<numero.size();i++)
			{
				numero.at(i) = '9';
			}
			
			numero.at(posicion-1) -=1;
			
		}
		posicion-=1;
	}
	if(numero.at(0)=='0')
	{
		numero.at(0) = ' ';
	}
	
	return numero;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;

	cin >> t;

	string numeroFinal;

	for(int i = 1;i<=t;i++)
	{
		cin >> numeroFinal;
		string respuesta = resolucion(numeroFinal);
		cout << "Case #" << i << ": " << respuesta << endl;
	}

	
	return 0;
}



