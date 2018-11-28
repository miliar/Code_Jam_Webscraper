#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	unsigned short int casos;
	unsigned long long int	kmcaballo, destino;
	unsigned int caballos;
	long double tiempo, velocidad, maximo;


	cin >> casos;
	cout.precision(21);

	for (int i = 1; i <= casos; ++i){
		cin >> destino >> caballos;

		maximo = 0;
		for (; caballos > 0; --caballos){
			cin >> kmcaballo >> velocidad;
			kmcaballo = destino - kmcaballo;
			tiempo = kmcaballo/velocidad;

			if (tiempo > maximo)
				maximo = tiempo;
		}

		cout << "Case #" << i << ": " << destino/maximo << '\n';

	}

	return 0;
}