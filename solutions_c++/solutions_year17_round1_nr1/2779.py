#include <bits/stdc++.h>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("inn.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int r = 0; r < t; r++) {
		int n, m;
		cin >> n >> m;
		string s[n + 3];
		for (int i = 0; i < n; i++) {
			cin >> s[i];
		}
		bool flag = 1;
		for (int j = 0; j < m; j++) {
			if (s[0][j] != '?')
				flag = 0;
		}
		if (flag) {
			flag = 0;
			for (int h = 0; h < m; h++) {
				for (int j = 0; j < n; j++) {
					if (s[j][h] != '?') {
						for (int i = 0; i < n; i++) {
							if(i == j)
								continue;
							if (s[i][h] == '?') {
								s[i][h] = s[j][h];
							} else
								break;
						}
						break;
					}
				}
			}

		}
		for (int i = 0; i < n; i++) {
			flag = 1;
			for (int j = 0; j < m; j++) {
				if (s[i][j] != '?')
					flag = 0;
			}

			for (int j = 0; j < m; j++) {
				if (i > 0 && flag && s[i][j] == '?')
					s[i][j] = s[i - 1][j];
				else if (!flag && s[i][j] != '?') {
					for (int k = j - 1; k >= 0; k--) {
						if (s[i][k] == '?') {
							s[i][k] = s[i][j];
						} else
							break;
					}
					for (int k = j + 1; k < m; k--) {
						if (s[i][k] == '?') {
							s[i][k] = s[i][j];
						} else
							break;
					}
				}
			}

		}
		cout << "Case #" << r + 1 << ": \n";
		for (int i = 0; i < n; i++) {
			cout << s[i] << endl;
		}
	}
}
