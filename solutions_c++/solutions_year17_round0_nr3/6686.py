#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct tSol {
	int sol1; //max(Ls, Rs)
	int sol2; //min(Ls, Rs)
};
struct tDist {
	int dIzq = -1;
	int dDer = -1;
};

tSol resolverCaso(int huecos, int personas);

int main() {
	ifstream entrada("C-small-1-attempt3.in");
	//ifstream entrada("entrada.txt");
	ofstream salida("salida.txt");
	int casos, huecos, personas;
	entrada >> casos;
	//cin >> casos;
	for (int c = 1; c <= casos; ++c) {
		entrada >> huecos >> personas;
		//cin >> huecos >> personas;
		tSol sol;
		sol = resolverCaso(huecos, personas);
		salida << "Case #" << c << ": " << sol.sol1 << " " << sol.sol2 << '\n';
		//cout << "Case #" << c << ": " << sol.sol1 << " " << sol.sol2 << '\n';
	}
	salida.close();
	entrada.close();
	return 0;
}

tSol resolverCaso(int huecos, int personas) {
	tSol solucion = { 0, 0 };
	vector<char> bath(huecos + 2); // '.' ocupado, '_' no ocupado
	bath[0] = bath[huecos + 1] = '.';
	for (int i = 1; i < huecos + 1; ++i) bath[i] = '_';

	for (int p = 0; p < personas; ++p) {

		vector<tDist> distBath(huecos);
		int cont = 0;
		for (int j = 0; j < huecos; ++j) {
			if (bath[j + 1] == '_') {
				distBath[j].dIzq = cont;
				++cont;}
			else {cont = 0;}
		}
		cont = 0;
		for (int j = huecos - 1; j >= 0; --j) {
			if (bath[j + 1] == '_') {
				distBath[j].dDer = cont;
				++cont;}
			else {cont = 0;}
		}

		vector<int> candidatos;
		int max_min = 0;
		for (int s = 0; s < huecos; ++s) {
			int numero_min = std::min(distBath[s].dDer, distBath[s].dIzq); //max(min(Ls, Rs))
			if (numero_min != -1 && numero_min > max_min) max_min = numero_min;
		}
		
		for (int s = 0; s < huecos; ++s) {
			int numero_min = std::min(distBath[s].dDer, distBath[s].dIzq);
			if (numero_min == max_min) candidatos.push_back(s);
		}
		
		int max_max = 0;
		if (candidatos.size() <= 1) {
			if (bath[candidatos[0] + 1] == '_') bath[candidatos[0] + 1] = '.';
			max_max = max_min;
		}
		else {
			bool ya = false;
			for (int i = 0; i < candidatos.size(); ++i) {
				int numero_max = std::max(distBath[candidatos[i]].dDer, distBath[candidatos[i]].dIzq);
				if (numero_max != -1 && numero_max > max_max) max_max = numero_max;
			}
			for (int i = 0; i < candidatos.size() && !ya; ++i) {
				int numero_max = std::max(distBath[candidatos[i]].dDer, distBath[candidatos[i]].dIzq);
				if (numero_max != -1 && numero_max == max_max) {
					if (bath[candidatos[i] + 1] == '_') bath[candidatos[i] + 1] = '.';
					ya = true;
				}
			}
		}
		solucion.sol1 = max_max;
		solucion.sol2 = max_min;
	}
	return solucion;
}