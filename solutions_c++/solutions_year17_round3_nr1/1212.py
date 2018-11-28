#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <fstream>
#include <unordered_map>
#include <map>
#include <iterator>
#include <iomanip>
#include <stack>
#include <math.h>
#include <bitset>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;

#define TASK "grants"
#define X first
#define Y second
#define mp make_pair
#define inb push_back
#define INF 2e9
#define LINF 9e18
#define eps 1e-6
#define y1 dfsdfsd

const int M = 1005;
pair<ll, ll> a[M];

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
#endif
	int t;
	cin >> t;
	int n, k;
	for (int p = 1; p <= t; ++p)
	{
		cin >> n >> k;
		for (int i = 0; i < n; ++i) cin >> a[i].X >> a[i].Y;
		sort(a, a + n);
		multiset<ll> s;
		ll ans = 0;
		ll sum = 0;
		for (int i = 0; i < n; ++i)
		{
			if (s.size() < k - 1)
			{
				s.insert(a[i].X * 2 * a[i].Y);
				sum += a[i].X * 2 * a[i].Y;
				continue;
			}
			ans = max(ans, a[i].X * a[i].X + sum + a[i].X * 2 * a[i].Y);
			if (s.size() && a[i].X * 2 * a[i].Y > *s.begin())
			{
				sum -= *s.begin();
				s.erase(s.begin());
				s.insert(a[i].X * 2 * a[i].Y);
				sum += a[i].X * 2 * a[i].Y;
			}
		}
		cout.precision(9);
		cout << "Case #" << p << ": ";
		cout << fixed << (double)ans * acos(-1) << '\n';
	}
}