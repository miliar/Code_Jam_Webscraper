#include <iostream>
#include <cstdio>
using namespace std;

bool correcto(int numero){

	int residuo = 0;
	bool si = true;

	while(si and numero > 9){

		residuo = numero % 10;

		if(!(residuo >= ((numero / 10) % 10))){

			return false;
		}

		numero = (numero / 10);
	}

	return true;
}

int main() {

	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);

	int casos = 0, numero = 0, contador = 0;

	cin >> casos;

	while(casos--){

		cin >> numero;

		while(!correcto(numero)){

			numero--;
		}

		contador++;

		cout << "Case #" << contador << ": " << numero << endl;
	}

	return 0;
}
