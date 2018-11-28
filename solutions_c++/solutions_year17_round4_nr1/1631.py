#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <list>
#include <algorithm>
#include <cmath>
#include <queue>
using namespace std;

pair<int, int> f[101][101][101];
int p;
void init()
{
	for (int i = 0; i < 101; ++i)
	{
		for (int j = 0; j < 101; ++j)
		{
			for (int k = 0; k < 101; ++k)
			{
				f[i][j][k] = make_pair(0, -100000);
			}
		}
	}
}

void dp(int a1, int a2, int a3)
{
	for (int i = a1; i >= 0; i--)
	{
		for (int j = a2; j >= 0; j--)
		{
			for (int k = a3; k >= 0; k--)
			{
				int ost = f[i][j][k].first;
				int cnt = f[i][j][k].second;
				int add_1 = 0;
				if (ost == 0)
				{
					add_1 = 1;
				}
				if (i > 0)
				{
					f[i - 1][j][k].second = max(f[i][j][k].second + add_1, f[i - 1][j][k].second);
					f[i - 1][j][k].first = (ost + 1) % p;
				}
				if (j > 0)
				{
					f[i][j - 1][k].second = max(f[i][j][k].second + add_1, f[i][j - 1][k].second);
					f[i][j - 1][k].first = (ost + 2) % p;
				}
				if (k > 0)
				{
					f[i][j][k - 1].second = max(f[i][j][k].second + add_1, f[i][k][k - 1].second);
					f[i][j][k - 1].first = (ost + 3) % p;
				}
			}
		}
	}
}

void solve()
{
	init();
	int n;
	cin >> n >> p;
	int a[4];
	a[0] = a[1] = a[2] = a[3] = 0;
	for (int i = 0; i < n; ++i)
	{
		int v;
		cin >> v;
		int k = v % p;
		++a[k];
	}
	int ans = a[0];
	f[a[1]][a[2]][a[3]] = make_pair(0, 0);
	dp(a[1], a[2], a[3]);
	ans += f[0][0][0].second;
	cout << ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}