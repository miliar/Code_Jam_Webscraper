#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int T, K;
string S;

int main () {
	cin >> T;

	int _ = 0;
	while (++_ <= T) {
		cin >> S >> K;

		int cnt = 0;
		bool imp = false;
		for (int i = 0; i < S.size(); ++i) {
			if (S[i] == '-') {
				if (i + K > S.size()) { imp = true; break; }
				for (int j = i; j < i + K; ++j) {
					S[j] = S[j] == '+' ? '-' : '+';
				}
				++cnt;
			}
		}

		cout << "Case #" << _ << ": ";
		if (imp) { cout << "IMPOSSIBLE" << endl; }
		else { cout << cnt << endl; }
	}
	return 0;
}

