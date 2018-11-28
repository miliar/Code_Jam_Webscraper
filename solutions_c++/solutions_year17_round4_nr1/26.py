#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;


const int P = 4;
int cnt[P];

const int N = 105;
int dp[N][N][N][P];

void clear()
{
	memset(cnt, 0, sizeof cnt);
	memset(dp, -1, sizeof dp);
}

int p;

int solve(int k1, int k2, int k3, int rem)
{
	int &cur = dp[k1][k2][k3][rem];
	if (cur != -1) return cur;
	cur = 0;
	
	if (k1 > 0) cur = max(cur, solve(k1 - 1, k2, k3, (rem + 1) % p) );
	if (k2 > 0) cur = max(cur, solve(k1, k2 - 1, k3, (rem + 2) % p) );
	if (k3 > 0) cur = max(cur, solve(k1, k2, k3 - 1, (rem + 3) % p) );

	if (rem == 0) cur++;

	return cur;
}

void solve()
{
	clear();

	int n;
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++)
	{
		int x;
		scanf("%d", &x);
		cnt[x % p]++;
	}

	int answer = cnt[0];
	cnt[0] = 0;

	for (int i = 0; i < p; i++)
		dp[0][0][0][i] = 0;
	answer += solve(cnt[1], cnt[2], cnt[3], 0);

	printf("%d\n", answer);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


