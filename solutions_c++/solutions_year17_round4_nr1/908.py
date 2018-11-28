#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const string filename = "A-large";
int Test, N, M;
int cnt[10], f[110][110], g[110][110][110];

int solve2()
{
	return cnt[0] + (cnt[1] + 1) / 2;
}

int solve3()
{
	return cnt[0] + f[cnt[1]][cnt[2]];
}

int solve4()
{
	return cnt[0] + g[cnt[1]][cnt[2]][cnt[3]];
}
	

int main(int argv, char* argc[])
{
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);
	memset(f, -2, sizeof(f));
	f[0][0] = 0;
	for (int i = 0; i <= 100; i ++) {
		for (int j = 0; j <= 100; j ++) {
			int x = 0;
			if ((i * 1 + j * 2) % 3 == 0) x = 1;
			f[i+1][j] = max(f[i+1][j], f[i][j]+x);
			f[i][j+1] = max(f[i][j+1], f[i][j]+x);
		}
	}
	memset(g, -2, sizeof(g));
	g[0][0][0] = 0;
	for (int i = 0; i <= 100; i ++) {
		for (int j = 0; j <= 100; j ++) {
			for (int k = 0; k <= 100; k ++) {
				int x = 0;
				if ((i * 1 + j * 2 + k * 3) % 4 == 0) x = 1;
				g[i+1][j][k] = max(g[i+1][j][k], g[i][j][k]+x);
				g[i][j+1][k] = max(g[i][j+1][k], g[i][j][k]+x);
				g[i][j][k+1] = max(g[i][j][k+1], g[i][j][k]+x);
			}
		}
	}
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d%d", &N, &M);
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < N; i ++) {
			int x;
			scanf("%d", &x);
			cnt[x % M] ++;
		}
		int ret = 0;
		if (M == 2) {
			ret = solve2();
		} else if (M == 3) {
			ret = solve3();
		} else {
			ret = solve4();
		}
		printf("Case #%d: %d\n", Case, ret);
	}
	return 0;
}
