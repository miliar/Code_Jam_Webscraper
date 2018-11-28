#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	for (int l = 1; l<= t; l++){
		string cadena;
		int tam;
		int contador = 0;
		bool imposible = false;
		cin >> cadena;
		cin >> tam;
		for (int i = 0; i <= (cadena.length() - tam) ; i++){
			if (cadena[i] == '-'){
				//si ultimo elemento es '-' entonces damos la vuelta a las tortitas
				for (int ta = 0; ta < tam; ta++){
					if (cadena[i + ta] == '-')
						 cadena[i + ta] = '+';
					else
						 cadena[i + ta] = '-';
				}
				contador++;
			}
		}
		int i = cadena.length() - tam;
		while(!imposible && i < cadena.length()){
			if (cadena[i] == '-')
				imposible = true;
			i++;
		}

		if (imposible)
			cout << "Case #" << l << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << l  << ": " << contador << endl;
		

		
	} 

return 0;
}
