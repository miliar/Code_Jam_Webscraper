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

const int maxn = 55;
int v[maxn];
int q[maxn][maxn];
int l[maxn], r[maxn];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;

	cin >> t;

	for (int ttt = 1; ttt <= t; ttt++) {
		printf("Case #%d: ", ttt);

		int n, p;

		scanf("%d %d", &n, &p);

		int maxcnt = 2000000;

		for (int i = 0; i < n; i++) {
			scanf("%d", &v[i]);

			maxcnt = min(maxcnt, 2000000 / v[i]);
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				scanf("%d", &q[i][j]);
			}

			sort(q[i], q[i] + p);
		}

		memset(l, 0, sizeof l);
		memset(r, 0, sizeof r);

		int ans = 0;

		for (int cnt = 1; cnt <= maxcnt; cnt++) {
			for (int i = 0; i < n; i++) {
				int now = v[i] * cnt;
				
				while (l[i] < p && q[i][l[i]] * 10 < 9 * now) {
					l[i]++;
				}

				while (r[i] < p && q[i][r[i]] * 10 <= 11 * now) {
					r[i]++;
				}
			}

			int res = p;

			for (int i = 0; i < n; i++) {
				res = min(res, r[i] - l[i]);
			}

			ans += res;

			for (int i = 0; i < n; i++) {
				l[i] += res;
			}
		}

		printf("%d\n", ans);
	}

	return 0;
}

