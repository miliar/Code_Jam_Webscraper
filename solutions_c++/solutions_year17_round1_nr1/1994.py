//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <string.h>
#include <memory.h>
using namespace std;
#define MAXN 2010
#define MAXM 128
#define oo 1e9
#define MOD 1000000007
typedef long long LL;
string arr[100];
int cnt[MAXM];
int a[MAXM], b[MAXM], c[MAXM], d[MAXM];
int n, m;
bool in(int x, int y, int k) {
	return x >= a[k] && x <= c[k] && y >= b[k] && y <= d[k];
}
bool inter(int x, int y) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (in(i, j, x) && in(i, j, y)) {
				return true;
			}
		}
	}
	return false;
}
bool can(int x, int y, char ch) {
	arr[x][y] = ch;
	for (int i = 0; i < MAXM; i++) {
		if (!cnt[i]) {
			continue;
		}
		a[i] = oo;
		b[i] = oo;
		c[i] = -oo;
		d[i] = -oo;
		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < m; ++k) {
				if (arr[j][k] == i) {
					a[i] = min(a[i], j);
					b[i] = min(b[i], k);
					c[i] = max(c[i], j);
					d[i] = max(d[i], k);
				}
			}
		}
	}
	for (int i = 0; i < MAXM; ++i) {
		if (!cnt[i]) {
			continue;
		}
		for (int j = i + 1; j < MAXM; ++j) {
			if (!cnt[j]) {
				continue;
			}
//			cout << (char) i << ", " << (char) j << " "
//					<< (inter(i, j) || inter(j, i)) << endl;
//			cout << a[i] << " " << b[i] << " " << c[i] << " " << d[i] << endl;
//			cout << a[j] << " " << b[j] << " " << c[j] << " " << d[j] << endl;
			if (inter(i, j) || inter(j, i)) {
				arr[x][y] = '?';
				return false;
			}
		}
	}
	arr[x][y] = '?';
	return true;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> n >> m;
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < n; ++i) {
			cin >> arr[i];
			for (int j = 0; j < m; ++j) {
				if (arr[i][j] != '?') {
					++cnt[(int) arr[i][j]];
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (arr[i][j] != '?') {
					continue;
				}
				for (int k = 0; k < MAXM; ++k) {
					if (!cnt[k]) {
						continue;
					}
					if (can(i, j, k)) {
						arr[i][j] = (char) k;
						break;
					}
				}
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < n; ++i) {
			cout << arr[i] << endl;
		}
	}
	return 0;
}
