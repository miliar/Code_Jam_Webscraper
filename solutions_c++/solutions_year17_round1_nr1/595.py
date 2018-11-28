#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

using namespace std;

void solve() {
	int R,C;
	cin >> R >> C;
	vector<string> bd(R);
	for(int i = 0; i < R; i++) cin >> bd[i];
	for(int i = 0; i < R; i++) {
		for(int j = 1; j < C; j++) {
			if(bd[i][j]=='?') bd[i][j] = bd[i][j-1];
		}
		for(int j = C-2; j >= 0; j--) {
			if(bd[i][j]=='?') bd[i][j] = bd[i][j+1];
		}
	}
	for(int j = 0; j < C; j++) {
		for(int i = 1; i < R; i++) {
			if(bd[i][j]=='?') bd[i][j] = bd[i-1][j];
		}
		for(int i = R-2; i>=0; i--) {
			if(bd[i][j]=='?') bd[i][j] = bd[i+1][j];
		}
	}
	cout << endl;
	for(int i = 0; i < R; i++) cout << bd[i] << endl;
}

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		solve();
	}
}

