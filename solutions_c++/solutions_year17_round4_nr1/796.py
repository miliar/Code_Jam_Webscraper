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
typedef vector <ll> vl;
typedef vector <pair <ll, ll>> vll;

void solve(int nn)
{
	ll ans = 1;
	ll n, p, temp;
	ll vec[1000];
	fill(vec, vec + 100, 0);
	cin >> n >> p;
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		vec[temp % p]++;
	}

	if (p == 2)
	{
		cout << "Case #" << nn + 1 << ": " << n - vec[1] / 2;
		cout << endl;
		return;
	}

	ans += vec[0];
	vec[0] = 0;
	ll m = min(vec[1], vec[p - 1]);
	ans += m;
	vec[1] -= m;
	vec[p - 1] -= m;
	if (p == 4)
	{
		ll kol = vec[2] / 2;
		ans += kol;
		vec[2] -= 2 * kol;
	}

	ll cur = 0;

	if (vec[2] > 0)
	{
		cur = 2;
		vec[2]--;
	}

	temp = 3;
	while (temp > 0)
	{
		if (vec[temp] > 0)
		{
			vec[temp]--;
			cur += temp;
			if (cur % p == 0)
				ans++;
		}
		else
			temp--;
	}

	if (cur % p == 0)
		ans--;

	cout << "Case #" << nn + 1 << ": " << ans;
	cout << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i);
	return 0;
}