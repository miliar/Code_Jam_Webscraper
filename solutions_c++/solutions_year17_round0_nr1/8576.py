#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int resolverCaso(ifstream & e);

int main() {
	ifstream entrada("A-large.in");
	ofstream salida("salida.txt");
	int casos;
	entrada >> casos;
	for (int c = 1; c <= casos; ++c) {
		int sol = resolverCaso(entrada);
		salida << "Case #" << c << ": ";
		sol == -1 ? salida << "IMPOSSIBLE" : salida << sol;
		salida << '\n';
	}
	entrada.close();
	salida.close();
	return 0;
}

int resolverCaso(ifstream & e) {
	string word = "";
	int happy = 0;
	e >> word;
	int k;
	e >> k;
	int cont = 0;
	for (int i = 0; i < word.size(); ++i) if (word[i] == '+') ++happy;
	if (happy == word.size()) return 0;
	else {
		happy = 0;
		for (int i = 0; i < word.size() + 1 - k; ++i) {
			if (word[i] == '-') {
				for (int j = i; j < i + k; ++j) word[j] = word[j] == '+' ? '-' : '+';
				++cont;
			}
		}
		for (int i = 0; i < word.size(); ++i) if (word[i] == '+') ++happy;
		if (happy == word.size()) return cont;
		else return -1;
	}
	
}