#include <bits/stdc++.h>

using namespace std;

#define error(x) cout << #x << " = " << x << endl
#define sz(a) int(a.size())

bool isHappy(string S) {
	for (int i = 0; i < sz(S); i++)
		if (S[i] == '-') return 0;
	return 1;
}

void dq(int pos, string S, int K, int cur, int & res) {
	if (pos > sz(S)-K) {
		if (isHappy(S))
			res = min(res, cur);
		return;
	}
	dq(pos+1, S, K, cur, res);
	for (int i = pos; i < pos+K; i++)
		if (S[i] == '+')
			S[i] = '-';
		else 
			S[i] = '+';
	dq(pos+1, S, K, cur+1, res);
}

void solve(string S, int K) {
	int n = sz(S);
	if (n <= 0) {
		int res = 1e9;
		dq(0, S, K, 0, res);
		if (res == 1e9) cout << "IMPOSSIBLE\n";
		else cout << res << "\n";
	}
	else {
		int res = 0;
		for (int i = 0; i+K-1 < n; i++) {
			if (S[i] == '+') continue;
			res++;
			for (int j = i; j < i+K; j++)
				if (S[j] == '+') 
					S[j] = '-';
				else 
					S[j] = '+';
		}
		if (isHappy(S)) cout << res << "\n";
		else cout << "IMPOSSIBLE\n";
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);
	int T; cin >> T;
	for (int te = 1; te <= T; te++) {
		string S; int K; 
		cin >> S >> K;
		cout << "Case #" << te << ": ";
		solve(S, K);
	}

	return 0;
}