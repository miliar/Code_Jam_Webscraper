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

typedef pair<int, int> pii;
int busq(vector<pii> &vec, pii &par, int i, int j) {
	if (i == j) {
		par = vec[i];
		return i;
	}
	else {
		pii izq;
		pii dch;
		int ib, db, m = (i + j) / 2;
		ib = busq(vec, izq, i, m);
		db = busq(vec, dch, m + 1, j);
		int mini = min(izq.first, izq.second), maxi = min(izq.first, izq.second);
		int mind = min(dch.first, dch.second), maxd = max(dch.first, dch.second);
		if (mini < mind || (mini == mind && maxi < maxd) || (mini == maxi && maxi == maxd && db < ib)) {
			par = dch;
			return db;
		}
		else {
			par = izq;
			return ib;
		}
	}
}
int busq(vector<pii> &vec) {
	pii aux;
	return busq(vec, aux, 0, vec.size() - 1);
}

pair<int, int> urinario(int uri, int pers) {
	vector<pii> mascara= vector<pii>(uri);
	for (int i = 0; i < uri; ++i) {
		mascara[i] = { i,uri - i - 1 };

	}
	pii answ;
	for (int i = 0; i < pers; ++i) {
		int b = busq(mascara);
		answ = mascara[b];
		pii MIN = { INT_MIN,INT_MIN };
		mascara[b] = { INT_MIN,INT_MIN };
		for (int i = b + 1; i < mascara.size() && mascara[i] != MIN; ++i) {
			mascara[i].first = i - b - 1;
		}
		for (int i = b - 1; i >=0 && mascara[i] != MIN; --i) {
			mascara[i].second = b - 1 - i;
		}

	}
	return answ;
}

void funcion(int i) {
	int pers, uri;
	cin >> uri >> pers;
	auto it = urinario(uri,pers);
	cout << "Case #" << i << ": " << max(it.first, it.second)<<" "<< min(it.first, it.second) << "\n";
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