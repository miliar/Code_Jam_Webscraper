//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

const int N = 55;

char c[N][N];

inline void solve() {
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> c[i][j];
		}
	}
	char ch;
	bool assigned = 0;
	for (int j = 0; j < m; j++) {
		ch = '?';
		for (int i = 0; i < n; i++) {
			if (c[i][j] == '?') {
				c[i][j] = ch;
			}
			else {
				ch = c[i][j]; 
			}
		}
		if (ch != '?') {
			for (int i = n - 1; i >= 0; i--) {
				if (c[i][j] == '?') {
					c[i][j] = ch;
				}
				else {
					ch = c[i][j];
				}
			}
			assigned = 1;
		}
		else if (assigned) {
			for (int i = 0; i < n; i++) {
				c[i][j] = c[i][j - 1];
			}
		}
	}
	for (int j = m - 1; j >= 0; j--) {
		if (c[0][j] == '?') {
			for (int i = 0; i < n; i++) {
				c[i][j] = c[i][j + 1];
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << c[i][j];
		}
		cout << endl;
	}
}

int main() {
	freopen (fname"A-large.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ":\n";
		solve();
	}
	return 0;
}
