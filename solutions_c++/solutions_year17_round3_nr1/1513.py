#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <limits>
#include <functional>
#include <iomanip>
#include <fstream>

using namespace std;
typedef long long ll;
typedef long double ld;
int const INF = numeric_limits<int>::max();
ll const LLINF = numeric_limits<ll>::max();
int const N = 1005;


int main()
{
	ios::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++)
	{
		
		int n, k;
		cin >> n >> k;
		vector<pair<ll, ll>> v(n);
		for (int i = 0; i < n; i++)
		{
			cin >> v[i].first >> v[i].second;
		}
		sort(v.begin(), v.end(), greater<pair<int, int>>());
		ll mx = 0;
		for (int i = 0; i < n - k + 1; i++)
		{
			ll s = v[i].first * v[i].first + v[i].second * 2 * v[i].first;
			multiset<ll, greater<ll>> se;
			for (int j = i + 1; j < n; j++)
			{
				se.insert(v[j].second * 2 * v[j].first);
			}
			auto it = se.begin();
			for (int j = 0; j < k - 1; j++)
			{
				s += *it;
				it++;
			}
			mx = max(mx, s);
		}
		

		cout << "Case #" << test << ": " << fixed << setprecision(10) << mx * asin(1) * 2 << endl;
	}
	return 0;
}

