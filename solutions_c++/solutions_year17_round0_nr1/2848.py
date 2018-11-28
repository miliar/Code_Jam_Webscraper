/**
 * Unproved.
 */
#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int cases; cin >> cases;
	for (int cc = 0; cc < cases; ++cc) {
		cout << "Case #" << cc + 1 << ": ";
		string s; int K;
		cin >> s >> K;

    vector<bool> flipEnd(s.size(), 0);
		int flipCount = 0, steps = 0;
		bool failed = false;

		for (int i = 0; i < s.size(); ++i) {
		  bool isMinus = ((s[i] == '+' ? 0 : 1) + flipCount) & 1;
		  if (isMinus) {
		    if (i + K - 1 >= s.size()) {failed = true; break;}
		    flipEnd[i + K - 1] = true; ++flipCount; ++steps;
		  }
		  if (flipEnd[i]) --flipCount;
		}

		if (failed) cout << "IMPOSSIBLE";
		else cout << steps;
		cout << "\n";
	}
	return 0;
}
