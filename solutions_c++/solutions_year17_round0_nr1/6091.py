#include <bits/stdc++.h>
using namespace std;

int testcase, k;
char str[11111];

int main() {
	cin >> testcase;
	for (int cs = 1; cs <= testcase; ++cs) {
		scanf(" %s", str);
		scanf("%d", &k);
		
		int l = strlen(str);
		int ans = 0;
		for (int i = 0; i + k - 1 < l; ++i) {
			if (str[i] == '-') {
				for (int j = 0; j < k; ++j) {
					str[i + j] = str[i + j] == '-' ? '+' : '-';
				}
				ans++;
			}
		}
		for (int i = 0; i < l; ++i) {
			if (str[i] == '-') {
				ans = -1;
				break;
			}
		}
		cout << "Case #" << cs << ": ";
		if (ans > -1) {
			cout << ans << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
