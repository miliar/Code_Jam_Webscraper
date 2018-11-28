#include <bits/stdc++.h>

using namespace std;

int n, m;
string s[30];

int main() {
	int _T;
	cin >> _T;
	for(int _t = 1; _t <= _T; _t++) {
		cout << "Case #" << _t << ":\n";
		cin >> m >> n;
		cin.ignore();
		for(int i=0; i<m; i++) 
			cin >> s[i];
		for(int i=0; i<m; i++) {
			for(int j=1; j<n; j++) {
				if (s[i][j] == '?' && s[i][j - 1] != '?')
					s[i][j] = s[i][j - 1];
			}
			for(int j = n - 2; j >= 0; j--) {
				if (s[i][j] == '?' && s[i][j + 1] != '?')
					s[i][j] = s[i][j + 1];
			}
		}
		for(int j=0; j<n; j++) {
			for(int i=1; i<m; i++) {
				if (s[i][j] == '?' && s[i - 1][j] != '?')
					s[i][j] = s[i - 1][j];
			}
			for(int i = m - 2; i >= 0; i--) {
				if (s[i][j] == '?' && s[i + 1][j] != '?')
					s[i][j] = s[i + 1][j];
			}
		}
		for(int i=0; i<m; i++)
			cout << s[i]<< "\n";
	}
	return 0;
}