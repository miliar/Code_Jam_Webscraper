#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <complex>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <bitset>
#include <cstdio>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include<deque>
typedef long long ll;
using namespace std;
const int N = 100+10;
int n;
double dp[N][N * 10];
bool vis[N][N * 10];
int dis[N], speed[N],nxt[N];
double calc(int i, int HIdx,ll distance) {
	if (i == n - 1)
		return 0;
	double &ret = dp[i][HIdx];
	if (vis[i][HIdx])
		return ret;
	vis[i][HIdx] = true;
	ret = 1e15;
	if (nxt[i] <= dis[i])
		ret = nxt[i] / (double)speed[i] + calc(i + 1, i,nxt[i]);
	if (nxt[i] + distance <= dis[HIdx])
		ret = min(ret, nxt[i] / (double)speed[HIdx] + calc(i + 1, HIdx, distance + nxt[i]));
	return ret;
}

int main() {
#ifndef ONLINE_JUDGE
//	freopen("myfile.in", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		memset(vis, 0, sizeof vis);
		printf("Case #%d: ", cas);
		int q;
		scanf("%d%d", &n, &q);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", dis + i, speed + i);
		for(int i=0;i<n;++i)
			for(int x,j=0;j<n;++j){
				scanf("%d", &x);
				if (i + 1 == j)
					nxt[i] = x;
			}
		for (int x,y, i = 0; i < q; ++i) 
			scanf("%d%d", &x, &y);
		double ans = calc(1, 0, nxt[0])+nxt[0]/(double)speed[0];
		printf("%.9lf\n", ans);

	}
	return 0;
}

