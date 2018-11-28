#include<iostream>
#include<fstream>
#include<string>
using namespace std;

void volteartortita(char&t) {
	switch (t) {
	case '-': {t = '+'; break; }
	case '+': {t = '-'; break; }
	}
}

void voltear(string&caso, int pos, int k) {
	for (int ctrl = 0; ctrl < k; ctrl++) {
		volteartortita(caso[ctrl + pos]);
	}
}

void resolver(ifstream&entrada, ofstream&salida) {
	int k;
	string caso;
	entrada >> caso;
	entrada >> k;
	int cont = 0;
	for (int ctrl = 0; ctrl < caso.length() - k + 1; ctrl++) {
		if (caso[ctrl] == '-') {
			voltear(caso, ctrl, k);
			cont++;
		}
	}
	for (int ctrl = 0; ctrl < caso.length(); ctrl++) {
		if (caso[ctrl] == '-') {
			salida << "IMPOSSIBLE\n";
			return;
		}
	}
	salida << cont << '\n';
}

int main() {
	ifstream entrada;
	entrada.open("A-large.in");
	ofstream salida;
	salida.open("output.txt");
	int casos;
	entrada >> casos;
	for (int ctrl = 0; ctrl < casos; ctrl++) {
		salida << "case #" << ctrl + 1 << ':' << ' ';
		resolver(entrada, salida);
	}
}