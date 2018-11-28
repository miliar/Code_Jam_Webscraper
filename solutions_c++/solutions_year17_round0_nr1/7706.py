#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#define INF 1000000000

using namespace std;

typedef long long lon;
typedef pair<lon, lon> ll;
typedef pair<lon, ll> lll;
typedef vector<lon> vl;
typedef vector<ll> vll;
typedef vector<lll> vlll;

int main() {
	int nCases;
	cin >> nCases;
	for (int cnum = 1; cnum <= nCases; cnum++) {
		string inp;
		int K;
		cin >> inp >> K;
		int cakes[inp.length()];
		for (int i = 0; i < inp.length(); i++) {
			cakes[i] = inp[i] == '+';
		}
		int y = 0;
		for (int i = 0; i < inp.length()-K+1; i++) {
			if (!cakes[i]) {
				for (int j = 0; j < K; j++) {
					cakes[i+j] ^= 1;
				}
				y++;
			}
		}
		int happy = 1;
		for (int i = 0; i < inp.length(); i++) {
			if (!cakes[i]) happy = 0;
		}
		if (happy)
			cout << "Case #" << cnum << ": " << y << endl;
		else
			cout << "Case #" << cnum << ": IMPOSSIBLE" << endl;
	}
}
