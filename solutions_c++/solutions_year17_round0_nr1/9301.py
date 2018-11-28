#include <iostream>
#include <cstdio>
using namespace std;

char voltear(char galleta){

	if(galleta == '+'){

		return '-';
	}

	return '+';
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int horneadas = 0, espatula = 0, contador = 0, caso = 0;
	string galletas = "";
	bool posible = true;

	cin >> horneadas;

	while(horneadas--){

		cin >> galletas;
		cin >> espatula;

		contador = 0;
		caso++;
		posible = true;

		for(int i = 0; i < galletas.length(); i++){

			if(galletas[i] == '-' and (i + espatula) <= galletas.length()){

				contador++;

				for(int j = i; j < (espatula + i); j++){

					galletas[j] = voltear(galletas[j]);
				}
			}
		}

		for(int k = (galletas.length() - espatula); k < galletas.length(); k++){

			if(posible and galletas[k] == '-'){

				posible = false;
			}
		}

		if(posible){

			cout << "Case #" << caso << ": " << contador << endl;
		}

		else {

			cout << "Case #" << caso << ": IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
