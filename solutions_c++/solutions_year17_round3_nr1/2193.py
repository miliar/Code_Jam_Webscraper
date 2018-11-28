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
typedef pair<ullint, ullint> pulliulli;
typedef pair<int, pulliulli> pu;
#endif

const double PI = 3.141592653589793238462643383279502884197169399375105820974944592307;
ullint maxR = 1;

struct comp {
	bool operator()(const pulliulli &izq, const pulliulli &dch) const{
		llint aux = dch.first*dch.first - izq.first*izq.first
			+ 2 * dch.second*dch.first - 2 * izq.first*izq.second;
		return aux < 0;

	}
};

struct alt {
	bool operator()(const pulliulli &izq, const pulliulli &dch) const{
		llint aux = dch.second*dch.first - izq.first*izq.second;
		return aux > 0;

	}
};

void funcion(int i) {
	int n, k;
	cin >> n >> k;
	multiset<pulliulli, comp> pan;
	priority_queue<pulliulli, vector<pulliulli>, alt> pcola;
	deque<pulliulli> cola;
	for (int i = 0; i < n; ++i) {
		pulliulli x;
		cin >> x.first >> x.second;
		pan.insert(x);
		pcola.push(x);
	}
	auto it = pan.begin();
	cola.push_front(*pan.begin());
	it = pan.erase(it);
	if (pan.find(pcola.top())==pan.end()) {
		pcola.pop();
	}	
	while (cola.size() < k) {
		if (pcola.top().first < cola.front().first) {
			cola.push_back(pcola.top());
			auto auxit = pan.find(pcola.top());
			if (auxit == it) {
				auto auxit = pan.find(pcola.top());
				it = pan.erase(auxit);
			}
			else {
				pan.erase(pcola.top());
			}
			pcola.pop();
			
		}
		else if (pcola.top().first > it->first) {
			cola.push_back(pcola.top());
			auto auxit = pan.find(pcola.top());
			if (auxit == it) {
				auto auxit = pan.find(pcola.top());
				it = pan.erase(auxit);
			}
			else {
				pan.erase(pcola.top());
			}
			pcola.pop();
		}
		else {
			cola.push_front(*it);
			it = pan.erase(it);
			if (pan.find(pcola.top()) == pan.end()) {
				pcola.pop();
			}
		}
	}
	ullint suma = 0, rm = cola.front().first;
	while (!cola.empty()) {
		rm = max(cola.front().first, rm);
		suma += 2 * cola.front().first*cola.front().second;
		cola.pop_front();
	}
	suma += rm*rm;
	double answ = suma*PI;
	cout << "Case #" << i << ": "<<fixed<<setprecision(15) << answ << "\n";
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