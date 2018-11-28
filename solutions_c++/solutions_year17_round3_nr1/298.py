#include <iostream>
#include <sstream>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
const double PI = acos(-1.);


void solve()
{

	return;
}

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("a.out", "w+", stdout);
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
		ll n, k;
		cin >> n >> k;
		vector <pair <ll, ll> > v(n);
		vector <pair <ll, int> > s(n);
		pair <ll, ll> mr = make_pair(-1, -1);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i].second >> v[i].first;
			s[i] = make_pair(v[i].second * v[i].first, i);
			if (v[i].second > mr.second)
				mr = make_pair(i, v[i].second);
		}
		sort(s.rbegin(), s.rend());
		double res = 0;
		ll mmr = -1;
		bool fl = false;
		for (int i = 0; i < k - 1; ++i)
		{
			res += s[i].first;
			mmr = max(mmr, v[s[i].second].second);
			fl |= s[i].second == mr.first;
		}
		double res2 = res + (v[mr.first].first * v[mr.first].second);
		res2 *= 2 * PI;
		res2 += PI * mr.second * mr.second;

		res += s[k - 1].first;
		res *= 2 * PI;
		mmr = max(mmr, v[s[k-1].second].second);
		res += PI * mmr * mmr;
		if (fl)
			res2 = res;
		cout << "Case #" << t << ": ";
		printf("%.9lf\n", max(res, res2));
	}
	return 0;
}