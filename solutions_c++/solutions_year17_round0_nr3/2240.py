#include <algorithm>
#include <bitset>
#include <cassert>
#include <deque>
#include <queue>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <float.h>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<unsigned> vu;
typedef vector<ll> vl;
typedef vector<pi> vp;
typedef vector<string> vs;
typedef set<int> si;
typedef map<int, int> mi;
typedef map<ll, ll> ml;

void solve(int t)
{
	ll n, k;
	cin >> n >> k;

	ml ranges;
	ranges[-n] = 1;

	ll res_min, res_max;

	while (k > 0)
	{
		ml::iterator it = ranges.begin();
		ll cnt = it->second;
		if (it->first & 1)
		{
			if (k > cnt)
			{
				ranges[it->first / 2] += 2 * cnt;
				k -= cnt;
				ranges.erase(it);
			}
			else
			{
				ranges[it->first / 2] += 2 * k;
				it->second -= k;
				res_min = res_max = -it->first / 2;
				k = 0;
			}
		}
		else
		{
			if (k > cnt)
			{
				ranges[it->first / 2] += cnt;
				ranges[it->first / 2 + 1] += cnt;
				k -= cnt;
				ranges.erase(it);
			}
			else
			{
				ranges[it->first / 2] += k;
				ranges[it->first / 2 + 1] += k;
				res_min = -it->first / 2 - 1;
				res_max = -it->first / 2;
				it->second -= k;
				k = 0;
			}
		}
	}

	cout << "Case #" << t + 1 << ": " << res_max << " " << res_min << endl;
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		solve(i);
	}
	return 0;
}
