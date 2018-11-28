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
using namespace std;

pair<int, int> pair_min(pair<int, int> a, int first, int second)
{
	if (a.first < first)
	{
		return a;
	}
	if (a.first == first && a.second < second)
	{
		return a;
	}
	return make_pair(first, second);
}

void solve()
{
	int n, c, m;
	cin >> n >> c >> m;

	vector<int> v1;
	v1.resize(n + 1);
	vector<int> v2 = v1;
	int sum1 = 0, sum2 = 0;
	for (int i = 0; i < m; ++i)
	{
		int a, b;
		cin >> a >> b;
		if (b == 1)
		{
			v1[a]++;
			sum1++;
		}
		else
		{
			v2[a]++;
			sum2++;
		}
	}
	int cnt_rides = max(v1[1] + v2[1], max(sum1, sum2));
	int promot = 0;
	for (int i = 2; i <= n; ++i)
	{
		if (v1[i] + v2[i] > cnt_rides)
		{
			promot += v1[i] + v2[i] - cnt_rides;
		}
	}
	cout << cnt_rides << ' ' << promot << ' ';
}

int main()
{
	freopen("input3.txt", "r", stdin);
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