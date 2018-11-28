#include <bits/stdc++.h>
using namespace std;

using Int = int;
#define rep(i, n) for (Int i = 0; i < Int(n); ++i)
#define rep1(i, n) for (Int i = 1; i <= Int(n); ++i)

char neg(char sgn) {
	if (sgn == '+') return '-';
	else return '+';
}

Int solve() {
	string s;
	Int ans = 0, n, k;
	cin >> s >> k;
	n = s.size();
	for (Int i = 0; i <= n-k; ++i) {
		if (s[i] == '+') continue;
		for (Int j = i; j < i+k; ++j) s[j] = neg(s[j]);
		++ans;
	}
	for (Int i = n-k+1; i < n; ++i) if (s[i] == '-') return -1;
	return ans;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(nullptr);
	Int T; cin >> T;
	rep1(t, T) {
		Int res = solve();
		cout << "Case #" << t << ": ";
		if (res == -1) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
}
