#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)

const int NON = 1L << 30;

int calc(string S, int K) {
	int n = S.size(), cnt = 0;

	for_(i,0,n-K+1) {
		if (S[i] == '-') {
			++cnt;
			for_(j,i,i+K) {
				if (S[j] == '-') S[j] = '+';
				else S[j] = '-';
			}
		}
	}
	
	if (S.find("-") != S.npos) return NON;
	return cnt;
}

void solve() {
	string S;
	int K;
	cin >> S >> K;
	
	int ans = calc(S, K);
	reverse(S.begin(), S.end());
	ans = min(ans, calc(S, K));
	
	if (ans == NON) cout << "IMPOSSIBLE" << endl;
	else cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	
	for_(i,0,T) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
}