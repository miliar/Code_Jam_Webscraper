#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int resolverCaso(vector<int> const& l, int num);
bool isTidy(int num);
int resolver(vector<int> const& l, int num, int ini, int fin);
vector<int> construirNum(int num);

int main() {
	ofstream salida("resultado.txt");
	ifstream entrada("B-small-attempt0.in");
	vector<int> tidynumbers;
	int valormax = 1000;
	for (int i = 1; i <= valormax; ++i) {
		if (isTidy(i)) {
			tidynumbers.push_back(i);
		}
	}
	int casos, num;
	entrada >> casos;
	for (int c = 1; c <= casos; ++c) {
		entrada >> num;
		salida << "Case #" << c << ": " << resolverCaso(tidynumbers, num) << '\n';
	}
	return 0;
}

int resolverCaso(vector<int> const& l, int num) {
	return resolver(l, num, 0, l.size() - 1);
}

bool isTidy(int num) {
	int dig_d, dig_i;
	dig_d = num % 10;
	dig_i = dig_d;
	while (num > 0) {
		dig_d = dig_i;
		num = num / 10;
		dig_i = num % 10;
		if (num != 0 && dig_d < dig_i) return false;
	}
	return true;
}

int resolver(vector<int> const& l, int num, int ini, int fin) {
	if (fin - ini == 0) return l[ini];
	else if (fin - ini == 1) {
		if (num >= l[fin]) return l[fin];
		else return l[ini];
	}
	else {
		int m = (ini + fin) / 2;
		if (l[m] > num) resolver(l, num, 0, m);
		else if (l[m] < num) resolver(l, num, m, fin);
		else return l[m];
	}
}