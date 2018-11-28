#define _author "zys"
#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

#include<iostream>
#include<queue>
#include<stack>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<algorithm>
#define mem(a, x) mesmet(a, x, sizeof(a))
using namespace std;

typedef long long ll;
typedef long long LL;
typedef unsigned long long ull;
typedef unsigned int ui;

typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;
typedef pair<string, int> Psi;

const int INF = 0x3fffffff;
const double eps = 1e-6;
const int mod = 1000000007;
const double pi = acos(-1.0);

const int maxn = (int)20 + 5;

ll n, res;
int len;
int bit[maxn], ans[maxn];

int calc(ll x)
{
	int len = 0;
	while (x)
	{
		bit[len++] = x % 10;
		x /= 10;
	}
	return len;
}

ll dfs(int now, bool flag)
{
	ll ret = 0;
	if (now == 0)
	{
		for (int i = len - 1; i >= 0; i--)
			ret = ret * 10 + ans[i];
		return ret;
	}
	int fx = flag ? bit[now - 1] : 9;
	for (int i = fx; i >= ans[now]; i--)
	{
		ans[now - 1] = i;
		ret = dfs(now - 1, flag && i == fx);
		if (ret)return ret;
	}
	return 0;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int Case = 1;
	for (T, scanf("%d", &T); T; T--)
	{
		scanf("%lld", &n);
		len = calc(n);
		res = 0;
		for (int i = 1; i < len; i++)
			res = res * 10 + 9;

		ans[len] = 1;
		res = max(res, dfs(len, 1));
		printf("Case #%d: %lld\n", Case++, res);
	}

	return 0;
}