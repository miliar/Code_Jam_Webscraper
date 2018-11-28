#pragma comment(linker, "/STACK:268435456")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <assert.h>
#include <stack>
#include <deque>
#include <limits.h>
#include <memory.h>
#include <time.h>
//#include <unordered_map>
//#include <unordered_set>
using namespace std;

void prepare(string q)
{
#ifdef _DEBUG
	//system("color F0");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (q.size() != 0)
	{
		freopen((q + ".in").c_str(), "r", stdin);
		freopen((q + ".out").c_str(), "w", stdout);
	}
#endif
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	cin.tie(false);
}

typedef long long ll;

void solve()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		ll n, k;
		cin >> n >> k;
		ll ans1, ans2;
		map <ll, ll> v;
		v[n] = 1;
		while (true)
		{
			auto it = v.end();
			--it;
			ll ost = it->second;
			ll m = it->first / 2;
			ll z1 = (it->first - (m + 1));
			ll z2 = m;
			if (ost >= k)
			{
				ll m = it->first / 2;
				ans1 = z2;
				ans2 = z1;
				break;
			}
			k -= ost;
			v[z1] += ost;
			v[z2] += ost;
			v.erase(it);
		}

		cout << "Case #" << tt << ": " << ans1 << ' ' << ans2 << endl;
	}
}

int main()
{
	prepare("");
	solve();
	return 0;
}