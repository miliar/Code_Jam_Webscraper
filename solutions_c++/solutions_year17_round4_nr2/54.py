#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

const int Maxn = 1005;
const int Maxc = 1005;

int T;
int N, C, M;
int has[Maxc];
int tk[Maxn];

bool Check(int x)
{
	int cur = 0;
	for (int i = 1; i <= N; i++) {
		cur += x;
		cur -= tk[i];
		if (cur < 0) return false;
	}
	return true;
}

int Solve(int x)
{
	int res = 0;
	for (int i = 1; i <= N; i++)
		if (tk[i] > x) res += tk[i] - x;
	return res;
}

int main()
{
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d %d", &N, &C, &M);
		fill(has, has + Maxc, 0); fill(tk, tk + Maxn, 0);
		for (int i = 0; i < M; i++) {
			int p, b; scanf("%d %d", &p, &b);
			has[b]++; tk[p]++;
		}
		int lef = 0, rig = M - 1;
		int res = M;
		for (int i = 1; i <= C; i++)
			lef = max(lef, has[i]);
		while (lef <= rig) {
			int m = lef + rig >> 1;
			if (Check(m)) { res = m; rig = m - 1; }
			else lef = m + 1;
		}
		int res2 = Solve(res);
		printf("Case #%d: %d %d\n", tc, res, res2);
	}
	return 0;
}