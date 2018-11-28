#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

void solve()
{
	long long n, k;
	cin >> n >> k;
	long long x = n;
	long long x_cnt = 1;
	long long y = n + 1;
	long long y_cnt = 0;
	long long i;
	for (i = 1; i < k; i *= 2)
	{
		k -= i;
		long long nx = (x - 1)/2;
		long long ny = y/2;
		long long nx_cnt = x_cnt;
		long long ny_cnt = y_cnt;
		if (x % 2 == 1)
		{
			nx_cnt += x_cnt;
		}
		else
		{
			ny_cnt += x_cnt;
		}
		if (y % 2 == 1)
		{
			ny_cnt += y_cnt;
		}
		else
		{
			nx_cnt += y_cnt;
		}
		x = nx;
		y = ny;
		x_cnt = nx_cnt;
		y_cnt = ny_cnt;
//		cout << x << " " << x_cnt << " " << y << " " << y_cnt << endl;
	}
//	cout << k <<endl;
	if (y_cnt >= k)
	{
		cout << y/2 << " " << (y - 1)/2;
	}
	else
	{
		cout << x/2 << " " << (x - 1)/2;
	}
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
