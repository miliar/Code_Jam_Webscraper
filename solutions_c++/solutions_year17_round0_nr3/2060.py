#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <functional>
#include <random>
#include <ctime>
#include <cassert>
#include <unordered_map>

using namespace std;

#define N 100000
#define M 1850
mt19937 gen;
#define forn(i, n) for (int i = 0; i < n; i++)
#define piii pair<int, pair<int, int>>
#define pii pair<int, int>
#define forlrv(i, l, r) for (int i = r; i >= l; i--)
#define y(p) p.second
#define mp make_pair
#define mpp(a, b, c) mp(a, mp(b, c))
typedef long long ll;
#define forlr(i, l, r) for (int i = l; i <= r; i++)
#define p p2

pair<ll, ll> solve(ll n, ll k)
{
	map<ll, ll, greater<ll>> m;
	k--;
	m[n] = 1;
	while (k)
	{
		pair<ll, ll> p = *m.begin();
		m.erase(p.first);

		m[(p.first - 1) / 2] += min(p.second, k);
		m[(p.first / 2)] += min(p.second, k);

		if (p.second <= k)
			k -= p.second;
		else
		{
			m[p.first] = p.second - k;
			break;
		}
	}

	pair<ll, ll> p = *m.begin();

	ll mx = (p.first - 1) / 2, mn = (p.first) / 2;
	return mp(mn, mx);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	ll n, k;
	forn(i, t)
	{
		scanf("%lld %lld", &n, &k);
		pair<ll, ll> p = solve(n, k);
		printf("Case #%d: %lld %lld\n", i + 1, p.first, p.second);
	}
}