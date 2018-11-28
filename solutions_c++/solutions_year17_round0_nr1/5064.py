#include <bits/stdc++.h>
using namespace std;


void solve(string s, int k, int t_id) {
	int ans = 0;
	for (int i = 0; i + k <= s.size(); i++) {
		if (s[i] == '-') {
			ans ++;
			for (int j = i; j < i + k; j++) {
				if (s[j] == '+') {
					s[j] = '-';
				} else {
					s[j] = '+';
				}
			}
		}
	}
	for (int i = 0 ; i < s.size(); i++) {
		if (s[i] == '-') {
			ans = -1;
		}
	}
	if (ans == -1) {
		printf("Case #%d: %s\n", t_id, "IMPOSSIBLE");
	} else {
		printf("Case #%d: %d\n", t_id, ans);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin>>t;
	for (int t_id = 1; t_id <= t; t_id++) {
		string s;
		int k;
		cin>>s>>k;
		solve(s, k, t_id);
	}

	return 0;
}
