#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

#define X first
#define Y second
#define N 1010
#define M 500010

typedef long long ll;
const int INF = 1<<30;
const int Mod = 1000000007;
const double pi = acos(-1);

struct node
{
	ll r, h;
	bool operator < (const node &t)const
	{
		return r * h > t.r * t.h;
	}
}p[N], q[N];

bool cmp(node x, node y)
{
	return x.r > y.r;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int T, n, K; 
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas)
	{
		printf("Case #%d: ", cas);
		scanf("%d %d", &n, &K);
		for (int i = 1; i <= n; ++i) scanf("%I64d %I64d", &p[i].r, &p[i].h);
		sort(p + 1, p + n + 1, cmp);
		ll res = 0;
		for (int i = 1; i + K - 1 <= n; ++i)
		{
			for (int j = i + 1; j <= n; ++j) q[j] = p[j];
			sort(q + i + 1, q + n + 1);
			ll tmp = (2 * p[i].r * p[i].h + p[i].r * p[i].r) ;
			for (int j = i + 1; j <= i + K - 1; ++j) tmp += 2 * q[j].r * q[j].h;
			res = max(res, tmp);
		}
		printf("%.9lf\n", res * pi);
	}
	
	return 0;
}
