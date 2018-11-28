#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>

using namespace std;

void solve() {
	int h, w;
	cin >> h >> w;

	vector<string> g(h);
	for (int i = 0; i < h; i++) {
		cin >> g[i];
	}

	for (int i = 0; i < h; i++) {
		char prev = '?';
		for (int j = 0; j < w; j++) {
			if (g[i][j] != '?') {
				prev = g[i][j];
				break;
			}
		}
		if (prev == '?') {
			continue;
		}
		for (int j = 0; j < w; j++) {
			if (g[i][j] == '?') {
				g[i][j] = prev;
			} else {
				prev = g[i][j];
			}
		}
	}

	for (int ii = 0; ii < h; ii++) {
		for (int i = 0; i < h; i++) {
			if (g[i][0] == '?') {
				if (i - 1 >= 0 && g[i - 1][0] != '?') {
					for (int j = 0; j < w; j++) {
						g[i][j] = g[i - 1][j];
					}
				} else if (i + 1 < h && g[i + 1][0] != '?') {
					for (int j = 0; j < w; j++) {
						g[i][j] = g[i + 1][j];
					}
				}
			}
		}
	}
	
	cout << endl;
	for (int i = 0; i < h; i++) {
		cout << g[i] << endl;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "case #" << i << ": ";
		solve();
	}
}