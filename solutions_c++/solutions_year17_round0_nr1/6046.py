#include <iostream>
#include <cstdio>

using namespace std;

string s;
int t, k;

int main() {
	#ifdef LOCAL	
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cin >> s >> k;
		cout << "Case #" << i << ": ";
		int n = s.size();
		if (n < k) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			bool ok = true;
			int ans = 0;
			for (int j = 0; j < n; ++j) {
				if (s[j] == '-') {
					if (j + k - 1 >= n) {
						ok = false;
						break;
					} else {
						ans++;
						for (int x = j, z = 0; z < k; ++x, ++z) {
							if (s[x] == '-')
								s[x] = '+';
							else
								s[x] = '-';
						}
					}
				}
			}

			if (!ok) {
				cout << "IMPOSSIBLE" << endl;
			} else {
				cout << ans << endl;
			}
		}
	}

	return 0;
}