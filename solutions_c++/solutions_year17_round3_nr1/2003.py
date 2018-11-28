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

//first radius
//second height
vector<ii>pancake;
int n, k;

long double solve(int index, int rem, int maxR)
{
	if (index == n || !rem)
	{
		return PI * maxR * maxR;
	}
	return max(solve(index + 1, rem - 1, max(maxR, pancake[index].first)) + 2 * PI * pancake[index].first * pancake[index].second, solve(index + 1, rem, maxR));
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n >> k;
		pancake.resize(n);
		for (int j = 0; j < n; j++)
		{
			cin >> pancake[j].first >> pancake[j].second;
		}
		long double res = solve(0, k, 0);
		cout << "Case #" << i << ": ";
		cout << setprecision(6) << fixed << res << endl;
	}
	return 0;
}
