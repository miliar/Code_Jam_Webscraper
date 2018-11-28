#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cfloat>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

#define MOD 1000000007
#define PI 3.14159265359
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,n,m) for(int i = n; i < m; ++i)
#define ll long long

using namespace std;

void func(vector<string> &cake) {
	vector<bool> nochar(cake.size(), true);
	REP(i, cake.size()) {
		REP (j, cake[i].size()) {
			if (cake[i][j] == '?') continue;
			nochar[i] = false;
			//cout << cake[i][j] << endl;
			for (int r=j-1; r>=0 && cake[i][r] == '?'; --r) cake[i][r] = cake[i][j];
			for (int r=j+1; r<cake[i].size() && cake[i][r] == '?'; ++r) cake[i][r] = cake[i][j];
		}
	}
	int first = -1;
	//REP(i, cake.size()) cout << nochar[i] << endl;
	//for (const auto s:cake) cout << s << endl;
	FOR(i, 0, cake.size()) {
		if (first == -1 && !nochar[i]) first = i;
		if (i < cake.size()-1 && nochar[i+1] && !nochar[i]) {
			cake[i+1] = cake[i];
			nochar[i+1] = false;
		}
	}
	for(int i = first-1; i>=0; --i) cake[i] = cake[first];
	//for (const auto s:cake) cout << s << endl;
}

int main() {
	int t, row, col;
	string str;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> row;
		cin >> col;
		vector<string> cake;
		REP (j, row) {
			cin >> str;
			cake.push_back(str);
		}
		func(cake);
		cout << "Case #" << i << ":" << endl;
		REP (j, row) {
			cout << cake[j] << endl;
		}
	}
	return 0;
}
