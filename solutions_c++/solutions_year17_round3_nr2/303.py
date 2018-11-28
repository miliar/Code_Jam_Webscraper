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
	freopen("B-large (1).in", "r", stdin);
	freopen("a.out", "w+", stdout);
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
		int ac, aj;
		cin >> ac >> aj;
		ll tc = 0, allttc = 0, tj = 0, allttj = 0;
		ll tsm = 0;
		ll res = 0;
		vector <pair <ll, int> > v(2 * (ac + aj));
		for (int i = 0; i < ac; ++i)
		{
			cin >> v[2 * i].first >> v[2 * i + 1].first;
			v[2 * i].second = 3;
			v[2 * i + 1].second = 1;
		}
		for (int i = ac; i < ac + aj; ++i)
		{
			cin >> v[2 * i].first >> v[2 * i + 1].first;
			v[2 * i].second = 4;
			v[2 * i + 1].second = 2;
		}
		sort(v.begin(), v.end());
		v.push_back(v[0]);
		v[v.size() - 1].first += 24 * 60;
		vector <ll> ttj, ttc;
		for (int i = 0; i < v.size() - 1; ++i)
		{
			if ((v[i].second ^ v[i + 1].second) & 1)
			{
				tsm += v[i + 1].first - v[i].first;
				res++;
			}
			else
			{
				if (v[i].second == 3)
					tc += v[i+1].first-v[i].first;
				if (v[i].second == 4)
					tj += v[i + 1].first - v[i].first;
				if (v[i].second == 1)
				{
					ttc.push_back(v[i + 1].first - v[i].first);
					allttc += v[i + 1].first - v[i].first;
				}
				if (v[i].second == 2)
				{
					ttj.push_back(v[i + 1].first - v[i].first);
					allttj += v[i + 1].first - v[i].first;
				}
			}
		}
		sort(ttc.rbegin(), ttc.rend());
		sort(ttj.rbegin(), ttj.rend());
		ll ptr = 0;
		while (tc + allttc > 720)
		{
			allttc -= ttc[ptr];
			res+=2;
			ptr++;
		}
		while (tj + allttj > 720)
		{
			allttj -= ttj[ptr];
			res+=2;
			ptr++;
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}