//@Galiève
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
#include <list>
#include <cassert>
#include <map>
#include <unordered_map>
#include <set>
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
typedef pair<int, int> pii;
#endif


struct comp {
	bool operator()(const pair<pii, pii> &izq, const pair<pii, pii> &dch) {
		return (izq.first <dch.first);
	}
};

bool inter(int a, int b) {
	float n = a*0.9;
	float o = a*1.1;
	float be = b;
	return n <= be && be <= o;
}

pair<double, double> intersecc(pair<long long int, llint> &a, pair<long long int, long long int> &b) {
	double t = a.first - b.first;
	if (a.second == b.second) {
		t = INT_MIN;
	}
	else {
		t = t / (b.second - a.second);
	}
	return pair<double, double>(t, a.first + a.second*t);
}

double resol(vector<pair<llint, llint> >& carrera, int d) {
	double dinter = LLONG_MAX;
	int vmax = LLONG_MAX;
	double tlleg = -1;
	double tinter = 0;
	for (int i = 0; i < carrera.size(); ++i) {
		double aux = d - carrera[i].first;
		aux=aux/double(carrera[i].second);
		if (aux > tlleg) {
			tlleg = aux;
		}
	}
	//tlleg = (d - carrera.back().first - carrera.back().second*tinter) / vmax;
	return d/tlleg;
}


void funcion(int i) {
	llint d, n;
	cin >> d >> n;
	vector<pair<llint, llint> > carrera(n);
	for (auto &i : carrera) {
		cin >> i.first >> i.second;
	}
	double answ = resol(carrera, d);
	cout << "Case #" << i << ": " << fixed<<setprecision(6)<<answ << "\n";
}

int main() {
#ifndef DOMJUDGE
	//_CrtsetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
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