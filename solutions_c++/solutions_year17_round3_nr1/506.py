#define _USE_MATH_DEFINES 
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <ll> vl;
typedef vector <pair <ll, ll>> vll;

const ld pi = M_PI;
ll a, b;

void solve(int nn)
{
	vector <pair <ld, ld>> vec;
	ll n, k;
	ld ans = 0;
	cin >> n >> k;
	ld temp1, temp2;
	for (int i = 0; i < n; i++)
	{
		cin >> temp1 >> temp2;
		vec.push_back({ 2 * pi * temp1 * temp2, pi * temp1 * temp1 });
	}

	sort(vec.rbegin(), vec.rend());

	for (int i = 0; i < n; i++)
	{
		ld cur = 0;
		int kol = 1;
		int ind = 0;
		cur += vec[i].first;
		cur += vec[i].second;
		while (ind < n && kol < k)
		{
			if (ind == i)
			{
				ind++;
				continue;
			}
			cur += vec[ind].first;
			ind++;
			kol++;

		}
		ans = max(ans, cur);
	}
	
	cout << "Case #" << nn + 1 << ": " << ans;
	
	cout << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cout << setprecision(9) << fixed;
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i);
	return 0;
}