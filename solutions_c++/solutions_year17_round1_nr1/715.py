#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
long long n, t, k, p, m, y;
char a[30][30];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	while (p++ < t) {
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> a[i][j];
		for (int i = 0; i < n; ++i)
			for (int j = 1; j < m; ++j)
				if (a[i][j] == '?' && a[i][j - 1] != '?')
					a[i][j] = a[i][j - 1];
		for (int i = 0; i < n; ++i)
			for (int j = m - 2; j >= 0; --j)
				if (a[i][j] == '?' && a[i][j + 1] != '?')
					a[i][j] = a[i][j + 1];
		for (int i = 1; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (a[i][j] == '?' && a[i - 1][j] != '?')
					a[i][j] = a[i - 1][j];
		for (int i = n - 2; i >= 0; --i)
			for (int j = 0; j < m; ++j)
				if (a[i][j] == '?' && a[i + 1][j] != '?')
					a[i][j] = a[i + 1][j];
		cout << "Case #" << p << ": \n";
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j)
				cout << a[i][j];
			cout << endl;
		}
	}
}