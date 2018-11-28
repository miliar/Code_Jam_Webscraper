#include <bits/stdc++.h>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		string st;
		int k;
		cin >> st >> k;
		int ans = 0;
		for (int i = 0; i < st.size(); i++) {
			if (st[i] == '-') {
				if (i + k - 1 < st.size()) {
					for (int j = i; j <= i + k - 1; j++) {
						if (st[j] == '-') {
							st[j] = '+';
						} else {
							st[j] = '-';
						}
					}
					ans++;
				} else {
					ans = -1;
					break;
				}
			}
		}
		cout << "Case #" << test << ": ";
		if (ans == -1) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << ans << '\n';
		}
	}
}
