#include <bits/stdc++.h>

using namespace std;

int n, m, t, h = 1;

int main() {
	cin >> t;
while (t--) {
	char c[30][30];
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> c[i][j];
	int r = 0;
	for (int j = 0; j < m; j++) {
		if (c[0][j] != '?') {
			for (int k = r; k < j; k++)
				c[0][k] = c[0][j];
			r = j + 1;
		}
	}
	if (r)
		for (int j = r; j < m; j++)
			c[0][j] = c[0][r - 1];
	for (int i = 1; i < n; i++) { 
		int l = 0;
		for (int j = 0; j < m; j++) 
			if (c[i][j] != '?') {
				for (int k = l; k < j; k++)
					c[i][k] = c[i][j];
				l = j + 1;
			}
		if (l == 0)
			for (int j = 0; j < m; j++)
				c[i][j] = c[i - 1][j];
		else
			for (int k = l; k < m; k++)
				c[i][k] = c[i][l - 1];
	}
	for (int i = n - 2; i >= 0; i--) {
		int p = 0;
		for (int j = 0; j < m; j++) 
			if (c[i][j] == '?')
				p++;
		if (p == m)
			for (int j = 0; j < m; j++)
				c[i][j] = c[i + 1][j]; 
	}
	cout << "Case #" << h++ << ":" << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cout << c[i][j];
		cout << endl;
	}
}
	return 0;
}
