#include <iostream>
using namespace std;

const int MAXN = 1000;

void voltea(string &S, int ini, int fin){
	for(int i = ini; i < fin; i++){
		S[i] = (S[i] == '+' ? '-' : '+');
	}
}

int resuelve(string S, int K){
	int N = S.size();

	int respuesta = 0;

	for(int i = 0; i <= N - K; i++){
		if(S[i] == '-'){
			voltea(S, i, i + K);
			respuesta++;
		}
	}

	for(int i = N - K + 1; i < N; i++){
		if(S[i] == '-'){
			return -1;
		}
	}

	return respuesta;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		cout << "Case #" << caso << ": ";

		string S;
		int K;
		cin >> S;
		cin >> K;

		int respuesta = resuelve(S, K);

		if(respuesta == -1){
			cout << "IMPOSSIBLE";
		}else{
			cout << respuesta;
		}

		cout << "\n";
	}

	return 0;
}
