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
	int ac, aj, x, y, x1, y1;
	for (int p = 1; p <= t; ++p)
	{
		cin >> ac >> aj;
		cout << "Case #" << p << ": ";
		if (ac + aj == 1)
		{
			cin >> x >> y;
			cout << 2 << '\n';
			continue;
		}
		if (ac == 2 || aj == 2)
		{
			cin >> x >> y >> x1 >> y1;
			if (max(y, y1) - min(x, x1) <= 720 || max(x, x1) - min(y, y1) >= 720)
				cout << 2 << '\n';
			else
				cout << 4 << '\n';
			continue;
		}
		cin >> x >> y >> x1 >> y1;
		cout << 2 << '\n';
	}
}