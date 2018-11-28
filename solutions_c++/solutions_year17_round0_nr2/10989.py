#include <iostream>
using namespace std;

int isTidy(int number){
	int auxiliar = -1, numero = number, auxiliar2;
	auxiliar = number % 10;
	number = number / 10;
	while(number != 0){
		auxiliar2 = auxiliar;
		auxiliar = number % 10;
		number = number / 10;
		if (auxiliar > auxiliar2){
			return 0;
		}
	}
	return numero;
}

int main(){
	int t, n,count=1, aux;
	cin >> t;
	while (t){
		cin >> n;
		for (int i = n; i > -1; i--){
			aux = isTidy(i);
			if (aux != 0){
				cout << "Case #" << count << ":" << " " << aux << endl;
				count++;
				break;
			}
		}
		t--;
	}
	return 0;
}