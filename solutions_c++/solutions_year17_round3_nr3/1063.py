#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<vector>
#include<cstdio>
#include<iomanip>
#include<cmath>

using namespace std;

#define ii pair<int, int>
#define mp make_pair
#define ll long long
#define pp push_back
#define PI (long double)(3.14159265358979323846)

long double s = 0, e = 1;
long double mid, eps = 1e-9;

int n;
long double extra;
long double cur[55];

bool canAcheive(long double d)
{
	long double x = extra;
	for (int i = 0; i < n; i++)
	{
		if (d - cur[i] > eps)
			x -= (d - cur[i]);
		if (x < eps)
			return 0;
	}

	return 1;
}
int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n >> n;
		cin >> extra;
		for (int j = 0; j < n; j++)
			cin >> cur[j];
		e = 1, s = 0;
		while (e - s > eps)
		{
			mid = s + (e - s) / 2;
			if (canAcheive(mid))
				s = mid;
			else
				e = mid;
		}
		long double res = 1;
		for (int j = 0; j < n; j++)
		{
			res *= max(mid, cur[j]);
		}

		cout << "Case #" << i << ": ";
		cout << setprecision(6) << fixed << res << endl;

	}
	return 0;
}
