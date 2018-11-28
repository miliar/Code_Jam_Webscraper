#include <bits/stdc++.h>

using namespace std;

#define error(x) cout << #x << " = " << x << "\n"
#define sz(a) int(a.size())

int toNum(string s) {
	int res = 0;
	for (int i = 0; i < sz(s); i++)
		res = res * 10 + s[i]-'0';
	return res;
}

bool isTidy(int x) {
	int last = 9;
	while (x > 0) {
		int digit = x % 10;
		if (digit > last) return 0;
		last = digit;
		x /= 10;
	}
	return 1;
}

int solve(string N) {
	if (sz(N) <= 4) {
		int n = toNum(N);
		for (int i = n; i >= 1; i--)
			if (isTidy(i))
				return i;
	}
	return -1;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);
	int T; cin >> T;
	for (int te = 1; te <= T; te++) {
		string N; cin >> N;
		cout << "Case #" << te << ": " << solve(N) << "\n";
	}

	return 0;
}