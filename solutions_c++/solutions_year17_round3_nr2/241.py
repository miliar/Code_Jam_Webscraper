#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
//const double PI = atan(1) * 4;

const int INF = 123456;


int must[1444];
int D[1444][2][744];



int go(int t, int c, int r) {
	if (r == -1) return INF;
	if (t == -1) return r==0 ? 0 : INF;

	int &ret = D[t][c][r];
	if (ret != -1) return ret;

	if (c == 0) {
		if (must[t] == 1) return ret = INF;
		int a0 = go(t-1, 0, r-1);
		int a1 = go(t-1, 1, r-1) + 1;
		return ret = min(a0, a1);
	}
	else {
		if (must[t] == 0) return ret = INF;
		int a0 = go(t-1, 0, r) + 1;
		int a1 = go(t-1, 1, r);
		return ret = min(a0, a1);
	}
}


int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);

		MEMSET(D, -1);
		MEMSET(must, -1);

		int Ac, Aj; scanf("%d%d", &Ac, &Aj);
		FOR(i, Ac + Aj) {
			int b, e; scanf("%d%d", &b, &e);
			for (int t=b; t<e; t++)
				must[t] = i < Ac;
		}

		
		int a0 = go(1439, 0, 720);
		if (a0 & 1) a0++;

		int a1 = go(1439, 1, 720);
		if (a1 & 1) a1++;

		int ans = min(a0, a1);
		printf("%d\n", ans);
	}

	return 0;
}
