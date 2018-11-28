#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

void fill(vector<string> &res, int rCur, int cCur, int r, int c, char ch) {
	for (int i = rCur; i <= r; i++)
		for (int j = cCur; j <= c; j++)
			res[i][j] = ch;
}

void solve()
{
	int r, c;
	cin >> r >> c;
	vector<string> g(r), res(r);
	for (int i = 0; i < r; i++) {
		cin >> g[i];
		res[i] = g[i];
	}
	char ch;
	bool first = false, found = false;
	for (int i = 0; i < r; i++) {
		int ncol = 0;
		for (int j = 0; j < c; j++) {
			ch = g[i][j];
			if (ch != '?') {
				found = true;
				int nrow = r;
				
				
				bool f = false;
				for (int k = i + 1; k < r; k++) {
					for (int l = 0; l < c; l++) {
						if (g[k][l] != '?') {
							nrow = k;
							f = true;
							break;
						}
					}
					if (f) break;
				}
				fill(res, !first ? 0 : i, ncol, nrow - 1, c - 1, ch);
				ncol = j + 1;
				
			} 
		}
		if (found) {
			first = true;
		}
	}
	cout << endl;
	for (int i = 0; i < r; i++) {
		cout << res[i];
		if (i != r - 1) cout << endl;
	}
}

int main()
{
	freopen("small.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}