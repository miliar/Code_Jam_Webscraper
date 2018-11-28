#include <bits/stdc++.h>
using namespace std;

void solve(int tc) {
	int n, m;
	cin >> n >> m;
	
	vector <string> s(n);
	for (int i = 0; i < n; i++)
		cin >> s[i];
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (s[i][j] == '?') continue;
			// fill top
			int k = j - 1;
			while (k >= 0 && s[i][k] == '?')
				s[i][k--] = s[i][j];
			// fill bottom
			k = j + 1;
			while (k < m && s[i][k] == '?')
				s[i][k++] = s[i][j];
		}
	}
	
	for (int i = 0; i < n; i++) {
		if (s[i][0] == '?') continue;
		int k = i - 1;
		while (k >= 0 && s[k][0] == '?') {
			for (int j = 0; j < m; j++)
				s[k][j] = s[i][j];
			k--;
		}
		k = i + 1;
		while (k < n && s[k][0] == '?') {
			for (int j = 0; j < m; j++)
				s[k][j] = s[i][j];
			k++;
		}
	}
	
	cout << "Case #" << tc << ":\n";
	for (int i = 0; i < n; i++)
		cout << s[i] << "\n";	
}

int main() {
	int t;
	cin >> t;
	
	for (int tc = 1; tc <= t; tc++) 
		solve(tc);
	
	return 0;
}