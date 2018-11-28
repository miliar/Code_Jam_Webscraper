#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int N, M, score, modifications;
struct model {
	char type;
	int line, col;
};

vector<model> V;
char ST[105];

void process() {
	cin >> M;
	model temp;
	int i;
	int pivotpos = -1;
	
	//leitura do estado inicial da primeira linha
	for(i=0;i<M;++i) {
		cin >> temp.type >> temp.line >> temp.col;
		ST[temp.col] = temp.type;
		if (temp.type == 'o' || temp.type == 'x') {
			pivotpos = temp.col;
		}
	}
	
	//nenhum x ou o, cria um o na primeira casa
	if (pivotpos == -1) {
		pivotpos = 1;
		++modifications;
		temp.type = 'o'; temp.line = 1; temp.col = 1;
		V.push_back(temp);
		ST[1] = 'o';
	}
	
	//promove um x para o, preenche o resto com +
	for(i=1;i<=N;++i) {
		if (ST[i] == 'x') {
			++modifications;
			temp.type = 'o'; temp.line = 1; temp.col = i;
			V.push_back(temp);
			ST[i] = 'o';
		} else if (!ST[i]) {
			++modifications;
			temp.type = '+'; temp.line = 1; temp.col = i;
			V.push_back(temp);
			ST[i] = '+';
		}
	}
	
	int j = (pivotpos%N)+1;
	//diagonal do x
	for(i=2; i<=N-1; ++i) {
		++modifications;
		temp.type = 'x'; temp.line = i; temp.col = j;
		V.push_back(temp);
		j = (j%N)+1;
	}
	
	//última linha
	//primeiro continuar a diagonal, ver se ela caiu na ponta
	if (N>1) { //heh
		++modifications;
		if (j==1 || j==N) temp.type = 'x';
		else				temp.type = 'o';
		temp.line = N; temp.col = j;
		V.push_back(temp);
	} else { //1x1 é melhor só ter o
		if (ST[1] != 'o') {
			++modifications;
			temp.type = 'o';
			temp.line = 1; temp.col = 1;
			V.push_back(temp);
		}
	}

	for(i=2; i<=N-1; ++i) {
		if (i!=j) { //acabei de colocar um 'o' aqui
			++modifications;
			temp.type = '+'; temp.line = N; temp.col = i;
			V.push_back(temp);
		}
	}
	
	score = (3*N)-min(N,2);
	
	memset(ST, 0, sizeof(ST));
}

int main() {
	int tc, t, i;
	cin >> t;
	for(tc=1; tc <= t; ++tc) {
		cin >> N;
		score = 0;
		modifications = 0;
		process();
		
		cout << "Case #" << tc << ": " << score << " " << modifications << endl;
		for(i=0;i<V.size();++i) {
			cout << V[i].type << " " << V[i].line << " " << V[i].col << endl;
		}
		V.clear();
	}
	return 0;
}