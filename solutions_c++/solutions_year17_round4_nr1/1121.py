#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm>
#include <iostream> 
#include <string.h> 
#include <stdlib.h>
#include <complex>
#include <sstream> 
#include <fstream>
#include <numeric>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
using namespace std;

#define pi acos(-1.0)
#define eps 1e-9
#define mod 1000000007

int T, n, p, a[4];
int dp[101][101][101][4];

int solve(int rem1, int rem2, int rem3, int cur)
{
	if(rem1 + rem2 + rem3 == 0) return 0;
	int& res = dp[rem1][rem2][rem3][cur];
	if(res == -1)
	{
		res = 0;
		if(rem1 > 0)
			res = max(res, (cur == 0) + solve(rem1 - 1, rem2, rem3, (cur + p - 1) % p));
		if(rem2 > 0)
			res = max(res, (cur == 0) + solve(rem1, rem2 - 1, rem3, (cur + p - 2) % p));
		if(rem3 > 0)
			res = max(res, (cur == 0) + solve(rem1, rem2, rem3 - 1, (cur + p - 3) % p));
	}
	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		memset(dp, -1, sizeof(dp));
		memset(a, 0, sizeof(a));
		scanf("%d %d", &n, &p);
		for(int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			a[x%p]++;
		}
		int res = solve(a[1], a[2], a[3], 0) + a[0];
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}