#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;
typedef long long LL;
#define For(i,a,b) for (int i = (a); i <= (b); i++)
#define Cor(i,a,b) for (int i = (a); i >= (b); i--)
#define rep(i,a) for (int i = 0; i < a; i++)
#define Fill(a,b) memset(a,b,sizeof(a))
priority_queue<pair<LL, LL> > Q;
void solve()
{
	while (!Q.empty())
		Q.pop();
	LL n, k;
	scanf("%lld%lld", &n, &k);
	Q.push(make_pair(n, 1));
	LL ans = 0;
	while (k)
	{
		LL cum = 0;
		LL maxL = Q.top().first;
		while (!Q.empty() && Q.top().first == maxL)
		{
			cum += Q.top().second;
			Q.pop();
		}
		if (cum >= k)
		{
			ans = maxL;
			break;
		}
		k -= cum;
		if (maxL & 1)
		{
			if (maxL / 2 > 0)
				Q.push(make_pair(maxL / 2, cum * 2));
		}
		else
		{
			if (maxL / 2 > 0)
				Q.push(make_pair(maxL / 2, cum));
			if (maxL / 2 > 1)
				Q.push(make_pair(maxL / 2 - 1, cum));
		}
	}
	LL ansL, ansR;
	if (ans & 1)
		ansL = ans / 2, ansR = ansL;
	else
		ansL = ans / 2, ansR = ans / 2 - 1;
	printf("%lld %lld\n", ansL, ansR);
}
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for (int i = 1; i <= _; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
