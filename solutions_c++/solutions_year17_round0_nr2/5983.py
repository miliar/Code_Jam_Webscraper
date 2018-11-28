#include <iostream>
#include <stack>
using namespace std;

const int MAXDIG = 19;

void convierte(int digitos[], long long int N, int& tam){
	stack<int> pila;
	int dig;
	while(N > 0){
		dig = N % 10;
		pila.push(dig);

		N -= dig;

		N /= 10;

		tam++;
	}

	int i = 0;
	while(!pila.empty()){
		digitos[i++] = pila.top();
		pila.pop();
	}
}

void resuelve(long long int N){
	int digitos[MAXDIG + 2];
	int tam = 0;

	convierte(digitos, N, tam);

	int i = tam - 1;
	while(i > 0){
		if(digitos[i] < digitos[i - 1]){
			digitos[i - 1]--;
			for(int j = i; j < tam; j++){
				digitos[j] = 9;
			}
		}
		i--;
	}

	i = 0;
	while(digitos[i] == 0) i++;
	while(i < tam){
		cout << digitos[i++];
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;

	for(int caso = 1; caso <= T; caso++){
		cout << "Case #" << caso << ": ";

		long long int N;
		cin >> N;

		resuelve(N);
		cout << "\n";
	}

	return 0;
}
