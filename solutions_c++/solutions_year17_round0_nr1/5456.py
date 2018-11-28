//DG25 Enrique Román Calvo
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <functional>
#include <utility>
#include <climits>
#include <stack>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <cassert>
using namespace std;

#ifndef DOMJUDGE
#include "checkML.h"
#endif

#ifndef ALIAS_DE_INT
#define ALIAS_DE_INT
#endif

#ifdef ALIAS_DE_INT
typedef long long int llint;
typedef long int lint;
typedef unsigned long long int ullint;
typedef unsigned long int ulint;
typedef unsigned int uint;
typedef unsigned short int usint;
typedef short int sint;
#endif

bool flip(string &pan, int size, int &res, int i) {
	if (i > pan.size() - size) {
		bool ok = true;
		while (i < pan.size() && ok) {
			ok = (pan[i] == '+');
			++i;
		}
		return ok;
	}
	if (pan[i] == '-') {
		++res;
		for (int j = i; j < i + size; ++j) {
			if (pan[j] == '-') {
				pan[j] = '+';
			}
			else {
				pan[j] = '-';
			}
		}
		return flip(pan, size, res, i + 1);
	}
	else {
		return flip(pan, size, res, i + 1);
	}
}


bool flip(string &pan, int size, int &res) {
	res = 0;
	return flip(pan, size, res, 0);
}

void funcion(int i) {
	string pan;
	int size, res = 0;
	cin >> pan >> size;
	if (flip(pan, size, res)) {
		cout << "Case #" << i << ": " << res << "\n";
	}
	else {
		cout << "Case #" << i << ": IMPOSSIBLE\n";
	}
}

int main() {
#ifndef DOMJUDGE
	_CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
	ifstream in("casos.txt");
	auto cinbuf = cin.rdbuf(in.rdbuf());
	ofstream out("answer.txt");
	auto coutbuf = cout.rdbuf(out.rdbuf());
#endif
	int casos;
	cin >> casos;
	for (int i = 0; i < casos; ++i) {
		funcion(i + 1);
	}
#ifndef DOMJUDGE
	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);
	//system("pause");
#endif
	return 0;
}