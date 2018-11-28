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

ll n, p;
ll need[3];
int ans;
ll have;
int top;

void solve(int nn)
{
	ans = 0;
	top = 0;
	pair <ll, ll> can0[10], can1[10];
	int perm[10];
	bool match[10][10];

	for (int i = 0; i < 10; i++)
		for (int j = 0; j < 10; j++)
			match[i][j] = false;

	cin >> n >> p;

	for (int i = 0; i < p; i++)
		perm[i] = i;

	for (int i = 0; i < n; i++)
		cin >> need[i];
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < p; j++)
		{
			cin >> have;
			if (i == 0)
			{
				ll l = ceil((100.0 * have) / (110.0 * need[0]) - 1e-9);
				ll r = (ll)((100.0 * have) / (90.0 * need[0]) + 1e-9);
				can0[j] = { l, r };
				if (r - l >= 0)
					top++;
			}
			else
			{

				ll l = ceil((100.0 * have) / (110.0 * need[1]) - 1e-9);
				ll r = (ll)((100.0 * have) / (90.0 * need[1]) + 1e-9);
				can1[j] = { l, r };
			}
		}
	}

	if (n == 1)
	{
		cout << "Case #" << nn + 1 << ": " << top;
		cout << endl;
		return;
	}

	for (int i = 0; i < p; i++)
	{
		for (int j = 0; j < p; j++)
		{
			if (!(can1[j].first > can0[i].second || can0[i].first > can1[j].second) && can0[i].second >= can0[i].first && 
																					   can1[j].second >= can1[j].first)
				match[i][j] = true;
		}
	}

	while (next_permutation(perm, perm + p))
	{
		int cc = 0;
		for (int i = 0; i < p; i++)
		{
			if (match[i][perm[i]])
				cc++;
		}
		ans = max(ans, cc);
	}

	int cc = 0;

	for (int i = 0; i < p; i++)
	{
		if (match[i][i])
			cc++;
	}
	ans = max(ans, cc);



	cout << "Case #" << nn + 1 << ": " << ans;
	cout << endl;
	return;
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