/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>
//#include "sort.h"

#define ll long long
#define ld double
#define pii pair <int, int>
#define pll pair <ll, ll>
#define mp make_pair

using namespace std;

const int maxn = 50;
char c[maxn][maxn];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;

	cin >> t;

	for (int ttt = 1; ttt <= t; ttt++) {
		printf("Case #%d:\n", ttt);

		int n, m;

		scanf("%d %d", &n, &m);

		for (int i = 0; i < n; i++) {
			scanf("%s", c[i]);
		}

		for (int i = 0; i < n; i++) {
			char last = '?';

			for (int j = 0; j < m; j++) {
				if (c[i][j] == '?') {
					c[i][j] = last;
				} else {
					last = c[i][j];
				}
			}

			last = '?';

			for (int j = m - 1; j >= 0; j--) {
				if (c[i][j] == '?') {
					c[i][j] = last;
				} else {
					last = c[i][j];
				}
			}
		}

		for (int i = 1; i < n; i++) {
			if (c[i][0] == '?' && c[i - 1][0] != '?') {
				for (int j = 0; j < m; j++) {
					c[i][j] = c[i - 1][j];
				}
			}
		}

		for (int i = n - 2; i >= 0; i--) {
			if (c[i][0] == '?' && c[i + 1][0] != '?') {
				for (int j = 0; j < m; j++) {
					c[i][j] = c[i + 1][j];
				}
			}
		}

		for (int i = 0; i < n; i++) {
			printf("%s\n", c[i]);
		}
	}

	return 0;
}
