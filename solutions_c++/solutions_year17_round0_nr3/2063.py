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

const int maxn = (int)1e5 + 5;

ll n, k, minn, maxx;

map<ll, ll>mp;

void insert(ll x, ll tot)
{
	if (mp.find(x) == mp.end())mp[x] = tot;
	else mp[x] += tot;
}

void bfs()
{
	queue<ll>q;
	q.push(n);

	mp.clear();
	mp[n] = 1;
	ll sum = 0;
	while (!q.empty())
	{
		ll now = q.front();
		q.pop();
		ll tot = mp[now];
		mp[now] = 0;
		sum += tot;
		ll l = (now - 1) / 2;
		ll r = now - l - 1;
		if (sum >= k) {
			maxx = r;
			minn = l;
			return;
		}
		if (mp.find(r) == mp.end())q.push(r);
		if (mp.find(l) == mp.end())q.push(l);
		insert(l, tot);
		insert(r, tot);
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int Case = 1;
	for (T, scanf("%d", &T); T; T--)
	{
		scanf("%lld%lld", &n, &k);
		bfs();
		printf("Case #%d: %lld %lld\n", Case++, maxx, minn);
	}

	return 0;
}
