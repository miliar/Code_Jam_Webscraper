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


int cast(char a) {
	return (int)(a - '0');
}
char cast(int a) {
	return (char)(a + (int)('0'));
}

void minusOne(string &answ, int i) {
	int x = cast(answ[i]);
	if (x == 0) {
		if (i == 0) {
			answ = answ.substr(1, answ.size() - 1);
		}
		else {
			x = 9;
			answ[i] = cast(x);
			minusOne(answ, i - 1);
		}
	}
	else {
		answ[i] = cast(x - 1);
		if (i > 0 && cast(answ[i]) < cast(answ[i - 1])) {
			answ[i] = cast(9);
			minusOne(answ, i - 1);
		}
	}

}

void minusOne(string &answ) {
	int i = answ.size() - 1;
	minusOne(answ, i);
}

string orden(const string &num) {
	int ant = cast(num[0]);
	string answ = "";
	bool ok = false;
	for (int i = 0; i < num.size(); ++i) {
		if (ok) {
			answ.push_back(cast(9));
		}
		else if (cast(num[i]) == ant) {
			answ.push_back(num[i]);
		}
		else if (cast(num[i]) > ant) {
			ant = cast(num[i]);
			answ.push_back(num[i]);
		}
		else {
			minusOne(answ);
			ant = cast(answ.back());
			answ.push_back(cast(9));
			ok = answ.back() == '9' && cast(num[i]) < '9';
			int h = 0;
			for (; h < answ.size() && answ[h] == cast(0); ++h);
			if (h > 0) {
				answ = answ.substr(h, answ.size());
			}
		}

	}
	return answ;
}

void funcion(int i) {
	string num;
	int size, res = 0;
	cin >> num;
	cout << "Case #" << i << ": " << orden(num) << "\n";
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