#include <cstdlib>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

using INT = cpp_int;

string processNaive(INT, INT);
string processOpti(INT, INT);

int main() {
	int T;
	cin >> T;
	for(int l = 0 ; l < T ; l++) {
		INT N, K;
		cin >> N >> K;
		//TRAITEMENT
		cout << "Case #" << l + 1 << ": " << processOpti(N, K) << endl;
		///////////
	}
	return 0;
}

string processNaive(INT N, INT K){
	return string("bonjour");
}

void printMap(map<INT, INT>& m){
	cerr << "MAP" << endl;
	for(auto it = m.rbegin(); it != m.rend(); ++it)
		cerr << it->first << " " << it->second << "\n";
}

string processOpti(INT N, INT K){
	map<INT, INT> spaces;
	spaces[N] = 1;
	INT lastMax;

	while(K > 0) {
		//printMap(spaces);
		INT MAX = spaces.rbegin()->first;
		INT NB = spaces.rbegin()->second;
		lastMax = MAX;

		if((MAX - 1) % 2 == 0) { //Parfait
			if(spaces.find((MAX - 1) / 2) != spaces.end())
				spaces[(MAX - 1) / 2] += 2 * NB;
			else spaces[(MAX - 1) / 2] = 2 * NB;
		}
		else{
			if(spaces.find((MAX) / 2) != spaces.end())
				spaces[(MAX) / 2] += 1 * NB;
			else spaces[(MAX) / 2] = 1 * NB;
			if(spaces.find((MAX - 2) / 2) != spaces.end())
				spaces[(MAX - 2) / 2] += 1 * NB;
			else spaces[(MAX - 2) / 2] = 1 * NB;
		}
		spaces.erase(spaces.find(MAX));
		K -= NB;
	}
	//cerr << "END" << endl;
	//printMap(spaces);
	stringstream ss;
	if((lastMax - 1) % 2 == 0)
		ss << (lastMax - 1) / 2 << " " << (lastMax - 1) / 2;
	else ss << (lastMax) / 2 << " " << (lastMax - 2) / 2;

	////////////////////////////
	return ss.str();
}
