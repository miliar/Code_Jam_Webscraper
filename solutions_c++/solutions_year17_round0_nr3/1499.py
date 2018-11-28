/*
Hanit Banga
*/

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false)

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int N = 1e5 + 5;
const ll inf = 3e18;

void add(set <pll, greater <pll>> &s, ll x, ll y);

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		ll n, k;
		cin >> n >> k;
		set <pll, greater <pll>> s;
		s.insert({n, 1});
		while (k > 1)
		{
			ll x = s.begin()->first, y = s.begin()->second;
			s.erase(s.begin());
			if (y < k)
			{
				add(s, x / 2, y);
				add(s, (x - 1) / 2, y);
				k -= y;
			}

			else
			{
				add(s, x / 2, k - 1);
				add(s, (x - 1) / 2, k - 1);
				add(s, x, y - k + 1);
				k = 1;
			}
		}

		ll x = s.begin()->first;
		cout << x / 2 << ' ' << (x - 1) / 2 << endl;
	}	
}

void add(set <pll, greater <pll>> &s, ll x, ll y)
{
	auto temp = s.lower_bound({x, inf});
	if (temp == s.end() or temp->first != x)
		s.insert({x, y});

	else
	{
		pll p = {x, y + temp->second};
		s.erase(temp);
		s.insert(p);
	}
}