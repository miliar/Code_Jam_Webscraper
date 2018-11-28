#include <bits/stdc++.h>
using namespace std;

string s;
int k, ans;

void flip(int l, int r) {
	for (int i = l; i < r; i++) {
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int l = 1; l <= t; l++) {
		cin >> s >> k;
		ans = 0;
		bool flag = false;
		for (int i = 0; i <= (int) s.size() - k; i++) {
			if (s[i] == '-') {
				flip(i, i + k);
				ans++;
			}
		}
		for (int i = s.size() - k + 1; i <= (int) s.size(); i++) {
			if (s[i] == '-') {
				flag = true;
				break;
			}
		}
		if (flag) {
			printf("Case #%d: IMPOSSIBLE\n", l);
		} else
			printf("Case #%d: %d\n", l, ans);
	}

	return 0;
}
