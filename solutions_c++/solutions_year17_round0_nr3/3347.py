#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;
typedef long long int Long;

int main(){

	int T;
	Long N,K;
	Long tocan;
	Long menor,mayor;
	Long quedan,potencia;

	optimizar_io(0);

	cin >> T ; 
	for(int caso = 1 ; caso <= T; caso ++){
		cin >> N >> K ;

		potencia = 1;
		quedan = N;
		while( K > potencia){
			quedan -= potencia;
			K -= potencia;
			potencia *= 2LL;
		}

		tocan = quedan/potencia;
		if(K <= quedan%potencia)
			tocan++;

		tocan--;
		menor = mayor= tocan/2LL;
		if(tocan&1LL)
			mayor++;
		cout<< "Case #" << caso << ": "<< mayor << ' ' << menor << '\n';

	}

	return 0;
}