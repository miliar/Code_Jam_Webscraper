#include <bits/stdc++.h>

using ll = long long;
using ull = unsigned long long;
using std::cout;
using std::cin;

void solve(int t) {
	std::string str;
	int K, ans = 0;
	cin >> str >> K;

	for (int i = 0; i < str.size(); ++i) {
		if (str[i] == '-') {
			if ((str.size() - i) < K) {
				cout << "Case #" << t << ": IMPOSSIBLE\n";
				return;
			}
			else {
				ans++;
				for (int j = 0; j < K; ++j) {
					str[j + i] = (str[j + i] == '+') ? '-' : '+';
				}
			}
		}
	}
	cout << "Case #" << t << ": " << ans << "\n";
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		solve(t + 1);
	}
	return 0;
}

/***

3
---+-++- 3
+++++ 4
-+-+- 4

***/