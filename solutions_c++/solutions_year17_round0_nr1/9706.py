#include <iostream>
using namespace std;

int main()
{

int T; // Cantidad de preguntas

cin >> T; //User pone cantidad

int K[T]; //Declaro largo de coso para cada T
int error[T]; // Va a valer 1 si hay un error (O sea que no es posible)
int Contador[T]; //Va a tener la cantidad de intentos para cada T
string S[T]; // String de los +-

for(int i = 0; i<T; i++)
{
	cin >> S[i];  //Completa cada S
	cin >> K[i]; // Completa cada K
	
	Contador[i] = 0;
	error[i] = 0;
}

for(int j = 0; j<T; j++) // J va a tener todos los casos de T
{
	for(int h = 0; h < S[j].length(); h++)  // H va a tner cada caracter del string
	{
		if(S[j][h] == '-') // Si el caracter H es -, o sea que es plano, si es un mas va a pasar al siguiente h
		{
			if(S[j].length() - h >= K[j])  // Si el largo de S para ese T, menos el numero de h para saber los caracteres restantes, menos k para saber si se pueedn girar panques, es mayor a 0
			{
	
				for(int w = 0; w < K[j]; w++)  // Esto es para invertir los siguientes k panqueuqes
				{
					if(S[j][h + w] == '+')
					{
					 S[j][h + w] = '-';
					}
					else if(S[j][h + w] == '-')
					{
					 S[j][h + w] = '+';
					}
				
				}
				
				Contador[j]++;
			}
			else
			{
				error[j] = 1;
			}
		}
		else if(Contador[j] < 1)
		{
			Contador[j] = 0;
		}
	
	
	}
}

	for(int g = 0; g < T; g++) //Esto ya es para los outputs
	{
		if (error[g] == 1)
		{
			cout << "Case #" << g+1 << ": IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << g+1 << ": " << Contador[g] << endl;
		}
	}

}
