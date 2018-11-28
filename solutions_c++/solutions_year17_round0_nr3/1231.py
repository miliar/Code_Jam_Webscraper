#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define endl '\n'

using dvojice = pair<long long int, long long int>;


map<dvojice, dvojice> mapa;

dvojice Spocti(dvojice vstup) {
	if (mapa.find(vstup) != mapa.end()) {
		return mapa[vstup];
	}

	if (vstup.second == 1) {
		return make_pair(vstup.first / 2, (vstup.first - 1) / 2);
	}

	if (vstup.second == 2) {
		return Spocti(make_pair(vstup.first / 2, 1));
	}

	mapa[vstup] = min(Spocti(make_pair(vstup.first / 2, vstup.second / 2)), Spocti(make_pair((vstup.first - 1) / 2, (vstup.second - 1) / 2)));
	return mapa[vstup];

}



void main() {
	std::ios::sync_with_stdio(false);


	long long int t, n, m,  k;
	string s;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.



	for (int i = 1; i <= t; ++i) {

		cin >> k >> n;

		dvojice vysledek = Spocti(make_pair(k, n));

		
		cout << "Case #" << i << ": " << vysledek.first << " " << vysledek.second<< endl;
		


	}
}