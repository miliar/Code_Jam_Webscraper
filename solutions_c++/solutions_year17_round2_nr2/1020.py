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

const int M = 1001;
int n;
char c[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
int a[6];

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
		cin >> n;
		for (int i = 0; i < 6; ++i) cin >> a[i];
		string ans = "";
		int i = a[0], j = a[2], k = a[4];
		while (i && j && k) ans += 'R', ans += 'Y', ans += 'B', --i, --j, --k;
		while (i && j || i && k || j && k)
		{
			if (i) ans += 'R', --i;
			if (j) ans += 'Y', --j;
			if (k) ans += 'B', --k;
		}
		int s = 0;
		while (s < ans.size())
		{
			char x = ans[s], y = ans[(s - 1 + ans.size()) % ans.size()];
			if (i && x != 'R' && y != 'R' || j && x != 'Y' && y != 'Y' || k && x != 'B' && y != 'B')
			{
				string u = ans.substr(0, s);
				if (i) u += 'R', --i;
				if (j) u += 'Y', --j;
				if (k) u += 'B', --k;
				u += ans.substr(s, ans.size() - s);
				ans = u;
			}
			++s;
		}
		cout << "Case #" << p << ": ";
		if (i || j || k) cout << "IMPOSSIBLE\n";
		else cout << ans << '\n';
	}
}