#include <bits/stdc++.h>
using namespace std;

string s;
int K;

int solve() {
	int N = s.size();
	int moves = 0;
	for (int i = 0; i < N; i++) {
		if (s[i] == '-') {
			if (i+K > N) return -1;
			moves++;
			for (int j = i; j < i+K; j++) {
				s[j] = (s[j] == '-') ? '+' : '-'; // flip
			}
		}
	}
	return moves;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> s >> K;
		int res = solve();
		cout << "Case #" << icase << ": ";
		if (res != -1) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
