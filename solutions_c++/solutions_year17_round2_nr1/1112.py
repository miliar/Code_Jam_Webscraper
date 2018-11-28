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

const int M = 1005, N = 100;
int n;
pii a[M];

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
	for (int p = 1; p <= t; ++p)
	{
		double d;
		cin >> d >> n;
		for (int i = 0; i < n; ++i) cin >> a[i].X >> a[i].Y;
		double l = 1e-6, r = 1e18;
		for (int q = 0; q < N; ++q)
		{
			double m = (l + r) / 2;
			bool f = 0;
			for (int i = 0; i < n; ++i)
			{
				double x = m * a[i].X / (m - a[i].Y);
				if (0 < x && x < d)
					f = 1;
			}
			if (f)
				r = m;
			else
				l = m;
		}
		cout << "Case #" << p << ": ";
		cout.precision(9);
		cout << fixed << l << '\n';
	}
}