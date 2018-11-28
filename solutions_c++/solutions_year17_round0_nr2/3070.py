#include <bits/stdc++.h>
using namespace std;
const int N = 20;

string s;
string v[N];
string dp[N][N][2][2];

void build () {
	for (int i = 0; i < 10; ++i) {
		stringstream ss; ss << i;
		ss >> v[i];
	}
}

string max (const string &a, const string &b) {
	if (a.length() > b.length())
		return a;
	if (b.length() > a.length())
		return b;
	for (int i = 0; i < a.length(); ++i) {
		if (a[i] > b[i])
			return a;
		if (b[i] > a[i])
			return b;
	}
	return a;
}

string solve (const int &pos, const int &last, const bool &less, const bool &positive) {
	if (pos == s.length())
		return "";
	if (dp[pos][last][less][positive] != "-1")
		return dp[pos][last][less][positive];
	string ans = "";
	if (less) {
		for (int i = 0; i < 10; ++i) {
			if (i >= last) {
				ans = max(ans, ((positive | i) ? v[i] : "") + solve(pos + 1, i, true, positive | i));
			}
		}
	}
	else {
		int j = s[pos] - '0';
		for (int i = 0; i < j; ++i) {
			if (i >= last) {
				ans = max(ans, ((positive | i) ? v[i] : "") + solve(pos + 1, i, true, positive | i));
			}
		}
		if (j >= last) {
			ans = max(ans, ((positive | j) ? v[j] : "") + solve(pos + 1, j, false, positive | j));
		}
	}
	return dp[pos][last][less][positive] = ans;
}

int main () {
	build();
	int test; scanf("%d", &test);
	for (int t = 1; t <= test; ++t) {
		cin >> s;
		printf("Case #%d: ", t);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				for (int k = 0; k < 2; ++k)
					for (int l = 0; l < 2; ++l)
						dp[i][j][k][l] = "-1";
		cout << solve(0, 0, false, false) << '\n';
	}
	return 0;
}