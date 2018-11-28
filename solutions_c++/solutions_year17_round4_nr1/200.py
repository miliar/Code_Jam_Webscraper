#include <stdio.h>
#include <iostream>
#include <vector>
#include <assert.h>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <memory.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
typedef long long ll;
const int o = 100;
int n, k, v[100], f[4];
map<ll, char> dp;
int calc(int s, int a, int b, int c, int d) {
	if (!a && !b && !c && !d)
		return 0;
	ll st = ((((ll)s * 1000ll + a) * 1000ll + b) * 1000ll + c) * 1000ll + d;
	if (dp.find(st) != dp.end())
		return dp[st];
	char &ret = dp[st];
	ret = 0;
	if (a)
		ret = max((int)ret, (s == 0) + calc(s, a - 1, b, c, d));
	if (b)
		ret = max((int)ret, (s == 0) + calc((s + 1) % k, a, b - 1, c, d));
	if (c)
		ret = max((int)ret, (s == 0) + calc((s + 2) % k, a, b, c - 1, d));
	if (d)
		ret = max((int)ret, (s == 0) + calc((s + 3) % k, a, b, c, d - 1));
	return ret;
}
int main()
{
	freopen("C:/Users/ASUS/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d:", tt);
		scanf("%d%d", &n, &k);
		memset(f, 0, sizeof(f));
		for (int i = 0; i < n; ++i) {
			scanf("%d", &v[i]);
			v[i] %= k;
			++f[v[i]];
		}
		dp.clear();
		printf(" %d\n", calc(0, f[0], f[1], f[2], f[3]));
	}
	return 0;
}