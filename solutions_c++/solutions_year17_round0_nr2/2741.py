#include<fstream>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

struct numero {
	long long int valor;
	vector<int>digitos;
	long long int orden;
};

void descomponer(long long int n, vector<int>&lista) {
	long long int m = n;
	vector<long long int>prueba;
	while (m != 0) {
		prueba.push_back(m % 10);//tenemos el numero al reves;
		m /= 10;
	}
	for (long long int ctrl = prueba.size()-1; ctrl>=0; ctrl--) {
		lista.push_back(prueba[ctrl]);
	}
}

void hacer9(vector<int>&digits, int pos) {
	for (int ctrl = pos; ctrl < digits.size(); ctrl++) {
		digits[ctrl] = 9;
	}
}

long long int digitrepresentedbyvector(const vector<int>&digits) {
	long long int total = 0;
	long long int mul = 1;
	for (int ctrl = digits.size() - 1; ctrl >= 0; ctrl--) {
		total += digits[ctrl] * mul;
		mul *= 10;
	}
	return total;
}

void findfirstuntidy(vector<int>&lista) {
	bool ya = false;
	for(int ctrl=1;ctrl<lista.size()&&!ya;ctrl++){
		if (lista[ctrl] < lista[ctrl - 1]) {
			lista[ctrl-1]--;
			hacer9(lista, ctrl);
			findfirstuntidy(lista);
			ya = true;
		}
	}
}

long long int resolver(long long int n) {
	vector<int>lista;
	descomponer(n, lista);
	findfirstuntidy(lista);
	return digitrepresentedbyvector(lista);
}

int main() {
	int casos;
	ifstream entrada;
	ofstream salida;
	salida.open("output.txt");
	entrada.open("B-large.in");
	entrada >> casos;
	long long int n;
	//entrada>>casos;
	for (int ctrl = 0; ctrl < casos; ctrl++) {
		//entrada >> n;
		entrada >> n;
		salida << "Case #" << ctrl + 1 << ':' << ' ';
		salida << resolver(n) << '\n';
	}

}