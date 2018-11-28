#include <iostream>
#include <stack>
#include <vector>
using namespace std;

const int MAXN = 25;

int num_componente[MAXN + 2][MAXN + 2];
char mapa[MAXN + 2][MAXN + 2];
vector<char> letras;
int cant_componente;

void init(){
	cant_componente = 0;
	letras.clear();
}

void procesa(int N, int M){
	stack<int> pila;
	stack<char> por_agregar;
	int tam_pila = 0;

	int lim_izq = 1;
	for(int j = 1; j <= M; j++){
		pila.push(0);
		tam_pila = 0;

		for(int i = 1; i <= N; i++){
			if(mapa[i][j] != '?'){
				por_agregar.push(mapa[i][j]);
				pila.push(i);
				tam_pila++;
			}
		}

		while(!por_agregar.empty()){
			letras.push_back(por_agregar.top());
			por_agregar.pop();
		}

		if(tam_pila > 0){
			int i = N;
			while(i > 0 && !pila.empty()){
				num_componente[i][j] = cant_componente;
				if(i == pila.top()){
					pila.pop();
					if(pila.top() != 0) cant_componente++;
				}
				i--;
			}
			cant_componente++;

			for(i = N; i >= 1; i--){
				for(int k = j; k >= lim_izq; k--){
					num_componente[i][k] = num_componente[i][j];
				}
			}

			lim_izq = j + 1;
		}

		pila.pop();
	}

	if(lim_izq <= M){
		//no hubo letra al final
		for(int i = 1; i <= N; i++){
			for(int k = lim_izq - 1; k <= M; k++){
				num_componente[i][k] = num_componente[i][lim_izq - 1];
			}
		}
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;

	for(int caso = 1; caso <= T; caso++){
		cout << "Case #" << caso << ":\n";

		int N, M;
		cin >> N >> M;

		init();

		for(int i = 1; i <= N; i++){
			for(int j = 1; j <= M; j++){
				cin >> mapa[i][j];
			}
		}

		procesa(N, M);

		for(int i = 1; i <= N; i++){
			for(int j = 1; j <= M; j++){
				if(mapa[i][j] == '?'){
					cout << letras[num_componente[i][j]];
				}else cout << mapa[i][j];
			}
			cout << "\n";
		}
	}

	return 0;
}
