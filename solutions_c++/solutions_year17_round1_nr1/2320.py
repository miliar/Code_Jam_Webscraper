#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll TC, R, C;
char S[30][30];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> TC;
	for (ll tc = 1; tc <= TC; tc++) {
		cin >> R >> C;
		for (ll i = 0; i < R; i++) {
			for (ll j = 0; j < C; j++) {
				cin >> S[i][j];
			}
		}

		for (ll i = 0; i < R; i++) {
			for (ll j = 1; j < C; j++) {
				if (S[i][j] == '?' && S[i][j-1] != '?') {
					S[i][j] = S[i][j-1];
				}
			}
			for (ll j = C-2; j >= 0; j--) {
				if (S[i][j] == '?' && S[i][j+1] != '?') {
					S[i][j] = S[i][j+1];
				}
			}
		}

		for (ll i = 0; i < R; i++) {
			for (ll j = 1; j < C; j++) {
				if (S[i][j] == '?' && S[i][j-1] != '?') {
					S[i][j] = S[i][j-1];
				}
			}
			for (ll j = C-2; j >= 0; j--) {
				if (S[i][j] == '?' && S[i][j+1] != '?') {
					S[i][j] = S[i][j+1];
				}
			}
		}

		for (ll i = 1; i < R; i++) {
			for (ll j = 0; j < C; j++) {
				if (S[i][j] == '?' && S[i-1][j] != '?') {
					S[i][j] = S[i-1][j];
				}
			}
		}
		for (ll i = R-2; i >= 0; i--) {
			for (ll j = 0; j < C; j++) {
				if (S[i][j] == '?' && S[i+1][j] != '?') {
					S[i][j] = S[i+1][j];
				}
			}
		}

		cout << "Case #" << tc << ":\n";
		for (ll i = 0; i < R; i++) {
			for (ll j = 0; j < C; j++) {
				cout << S[i][j];
			}
			cout << "\n";
		}
	}
	
	return 0;
}
