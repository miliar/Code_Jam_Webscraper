#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		ll K, N;
		cin >> N >> K;
		map<ll, ll> intervals;
		intervals[N]++;

		/*cerr << "---" << endl;
		for(auto x : intervals)
			cerr << x.first << " " << x.second << endl;
		cerr << "---" << endl;*/

		while(K > 1)
		{
			auto back = intervals.rbegin();
			ll len = back->first;
			ll cnt = back->second;
			if(cnt < K)
			{
				intervals.erase(len);

				intervals[(len - 1) / 2] += cnt;
				intervals[len - 1 - (len - 1) / 2] += cnt;

				K -= cnt;
				/*cerr << "--- " << K << endl;
				for(auto x : intervals)
					cerr << x.first << " " << x.second << endl;
				cerr << "---" << endl;*/
			}
			else 
				break;
			
		}
		auto back = intervals.rbegin();
		ll len = back->first;

		ll L = (len - 1) / 2;
		ll R = len - 1 - (len - 1) / 2;

		cout << max(L, R) << " " << min(L, R) << "\n";
	}
}
