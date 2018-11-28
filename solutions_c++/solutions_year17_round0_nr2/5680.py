#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define maxn 1000


using namespace std;


int num[1000];
int dp[1000][1000];


int dfs(int pos, int pre, int limit)
{
	if(pos == 0)
	{
		return 1;
	}
	if(!limit && dp[pos][pre] != -1)
	{
		return dp[pos][pre];
	}
	int n = limit? num[pos] : 9, ans = 0;
	for(int i = pre; i <= n; i++)
	{
		ans += dfs(pos - 1, i, limit && i == num[pos]);
	}
	if(!limit)
	{
		dp[pos][pre] = ans;
	}
	return ans;
}

int solve(long long n)
{
	int h = 0;
	while(n)
	{
		num[++h] = n % 10;
		n /= 10;
	}
	return dfs(h, 0, 1);
}

int check(long long mid, long long r)
{
	long long cnt = solve(mid);
	if(cnt < r)
	{
		return 1;
	}
	return 0;
}


int main()
{
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++)
	{
		memset(dp, -1, sizeof(dp));
		int k;
		printf("Case #%d: ", cas);
		long long n;
		scanf("%lld", &n);
		if(n < 10)
		{
			printf("%lld\n", n);
			continue;
		}
		long long l = 0, r = n;
		long long u = solve(n);
		while(l < r)
		{
			long long mid = (l + ((r - l) >> 1));
			if(check(mid, u))
			{
				l = mid + 1;
			}
			else
			{
				r = mid;
			}
		}
		cout << r << endl;
	}

	return 0;
}


