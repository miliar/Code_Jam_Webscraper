#include <iostream>
#include <string>

using namespace std;

int solve(const string&, int);

int main() {
	// Boost
	ios_base::sync_with_stdio(false);

	int tc;
	cin >> tc;

	for (int t = 1; t <= tc; ++t) {
		string x;
		int y;

		cin >> x >> y;
		const int ans = solve(x, y);

		cout << "Case #" << t << ": ";
		if (ans == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}

	return 0;
}

int T[1005], tlen;

int solve(const string& S, int K) {
	int ans = 0;
	tlen = 0;

	for (const char ch: S) {
		T[tlen++] = (ch == '+');
	}
	
	for (int i = 0; i <= tlen - K; ++i) {
		if (!T[i]) {
			++ans;
			for (int j = 0; j < K; ++j) {
				T[i + j] = 1 - T[i + j];
			}
		}
	}

	for (int i = tlen - K + 1; i < tlen; ++i) {
		if (!T[i]) return -1;
	}

	return ans;
}