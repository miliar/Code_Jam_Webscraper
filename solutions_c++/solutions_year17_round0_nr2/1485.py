#include <bits/stdc++.h>

using namespace std;

string correct(string S, int pos) {
	while (pos > 0 && S[pos] == S[pos - 1]) {
		pos--;
	}
	S[pos]--;
	for (int i = pos + 1; i < (int) S.size(); i++) {
		S[i] = '9';
	}

	return S;
}

string solve(string S) {
	S = string("0") + S;

	int pos = 0;
	while (pos + 1 < (int) S.size() && S[pos] <= S[pos + 1]) {
		pos++;
	}
	if (pos < (int) S.size() - 1) {
		S = correct(S, pos);
	}

	while (S[0] == '0') {
		S = S.substr(1);
	}
	return S;
}

int main() {
	assert(freopen("B.in", "r", stdin));
	assert(freopen("B.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		string N;
		cin >> N;
		auto ans = solve(N);
		cout << ans << endl;
		
		cerr << t << endl;
	}

	return 0;
}
