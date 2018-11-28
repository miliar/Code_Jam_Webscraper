#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <map>

#define IN_FILE "A-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

char g[31][31];

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; i++)
			cin >> g[i];
		int foundr = -1, foundc = -1;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (g[i][j] != '?') {
					foundr = i;
					foundc = j;
					break;
				}
			}
			if (foundr != -1)
				break;
		}
		for (int i = foundc-1; i >= 0; i--)
			g[foundr][i] = g[foundr][foundc];
		char curr = g[foundr][foundc];
		for (int i = foundc + 1; i < c; i++) {
			if (g[foundr][i] != '?'&&curr != g[foundr][i])
				curr = g[foundr][i];
			else if (g[foundr][i] == '?')
				g[foundr][i] = curr;
		}
		for (int i = 0; i < foundr; i++) {
			for (int j = 0; j < c; j++)
				g[i][j] = g[foundr][j];
		}
		for (int i = foundr + 1; i < r; i++) {
			int found = -1;
			for (int j = 0; j < c; j++) {
				if (g[i][j] != '?') {
					found = j;
					break;
				}
			}
			if (found == -1) {
				for (int j = 0; j < c; j++)
					g[i][j] = g[i - 1][j];
			}
			else {
				for (int j = 0; j < found; j++)
					g[i][j] = g[i][found];
				char curr = g[i][found];
				for (int j = found + 1; j < c; j++) {
					if (g[i][j] != '?'&&curr != g[i][j])
						curr = g[i][j];
					else if (g[i][j] == '?')
						g[i][j] = curr;
				}
			}
		}
		ll ans = 0;

		cout << "Case #" << tc << ":\n";
		for (int i = 0; i < r; i++)
			cout << g[i] << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
