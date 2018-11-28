#include <bits/stdc++.h>

using namespace std;

string diminuir(string numero){
	
	bool ok = false;
		
	while(!ok){
		ok = true;
		
		for (int i = 0; i < numero.length() - 1; i++)
			if (numero[i] > numero[i + 1]){
				ok = false;
				break;
			}
		
		if (ok)
			continue;
		else{
			for (int i = numero.length() - 1; i >= 0; i--){
				if (string(1, numero[i]) != "0"){
					numero[i]--;
					break;
				}else{
					numero[i] = '9';
				}
			}		
		}	
	}	
	
	string aux = "";
		
	for (int i = 0; i < numero.length(); i++)
		if (!(string(1, numero[i]) == "0" && aux == ""))
			aux += numero[i];
			
	numero = aux;
			
	return numero;			 
}

int main(){

	int t, caso = 0;
	string numero;
	
	cin >> t;
	
	while(t--){
		caso++;
		
		cin >> numero;	 
		
		printf("Case #%d: ", caso);
		
		cout << diminuir(numero) << endl;
	}
	
	return 0;
}
