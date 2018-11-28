#include <iostream>
#include <string>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iterator>
#include <functional>
#include <vector>
#include <algorithm>

using namespace std;

pair<long long, long long> divide(long long w)
{
	if (w % 2 == 1)
	{
		w = (w - 1) / 2;
		return make_pair(w, w);
	}
	else
	{
		w /= 2;
		return make_pair(w, w - 1);
	}
}

void solve()
{
	long long n, k; cin >> n >> k; --k;
	map<long long, long long> a;
	a[n] = 1;

	while (k)
	{
		long long w = a.rbegin()->first;
		long long cnt = a.rbegin()->second;

		long long div_cnt = min(cnt, k);
		pair<long long, long long> d = divide(w);

		if (cnt == div_cnt)
		{
			a.erase(w);
		}
		k -= div_cnt;
		auto & sib1 = a[d.first];
		sib1 += div_cnt;
		auto & sib2 = a[d.second];
		sib2 += div_cnt;
	}

	long long f = a.rbegin()->first;
	if (f % 2 == 1)
	{
		f /= 2;
		cout << f << " " << f << endl;
	}
	else
	{
		f /= 2;
		cout << f << " " << f - 1 << endl;
	}
}

int main()
{
	//freopen("i:/input.txt", "rt", stdin);
	//freopen("i:/input.out", "wt", stdout);

	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}