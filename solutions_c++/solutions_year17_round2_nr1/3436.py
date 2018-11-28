#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <utility>
#include <iomanip>

#define FOR(i, n) for(auto i = 0; i < n; ++i)
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef long long ll;

using namespace std;

int main()
{
	cin.sync_with_stdio(false);
	int tests;
	cin >> tests;
	ll n, s;
	double max_speed, k, d;
	FOR(test, tests)
	{
		max_speed = 1e14;
		cin >> d >> n;
		FOR(i, n)
		{
			cin >> k >> s;
			max_speed = min(max_speed, k * s / (d - k) + s);
		}
		cout << "Case #" << test + 1 << ": " << fixed << setprecision(6) << max_speed << endl;
	}
}