/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

void print_ans(int &K, int res) {
	if (res == -1) {
		cout << "Case #" << K++ << ": " << "IMPOSSIBLE" << endl;
	} else {
		cout << "Case #" << K++ << ": " << res << endl;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, K = 1;
	cin >> T;
	while (T--) {
		string s;
		int n, k, res = 0, i, j;
		cin >> s >> k;

		n = s.size();

		for (i = 0; i <= n - k; ++i) {
			if (s[i] == '-') {
				for (j = i; j < i + k; ++j) {
					s[j] = (s[j] == '+' ? '-' : '+');
				}
				++res;
			}
		}

		for (; i < n; ++i) {
			if (s[i] == '-') {
				print_ans(K, -1);
				goto NXT;
			}
		}

		print_ans(K, res);

		NXT:;
	}
	return 0;
}
