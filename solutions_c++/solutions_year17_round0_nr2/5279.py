#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>

using namespace std;

string CalculateLastTidy(string);

int main(){
	ifstream in("input.txt");
  	ofstream out("output.txt");
  
  	int nRighe;
  	in >> nRighe;

  	for(int i = 0; i < nRighe; i++)
  	{
  		string intero;
  		in >> intero;

  		string res = CalculateLastTidy(intero);

  		out << "Case #" << i+1 << ": " << res << endl;
  		
  	}
  
  	return 0;
}

string CalculateLastTidy(string numero)
{
	for(int i = numero.length() - 1; i >= 0; i--)
	{
		if(i > 0)
		{
			//se una cifra è piu PICCOLA di quella prima, allora la metto a 9 e riduco di 1 il numero prima, e metto tutte le cifre dopo a 9
			if(int(numero[i]) < int(numero[i-1]))
			{
				numero[i] = '9';
				numero[i-1] = (char)(int(numero[i-1]) - 1);

				for(int j = i; j < numero.length(); j++)
				{
					numero[j] = '9';
				}
			}
		}
	}

	//tolgo gli zeri davanti
	string tmp;
	for(int i = 0; i < numero.length(); i++)
	{
		if(numero[i] != '0')
			tmp += numero[i];
	}
	numero = tmp;

	return numero;
}