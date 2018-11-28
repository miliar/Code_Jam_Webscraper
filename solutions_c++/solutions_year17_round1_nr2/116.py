#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
	int N, P;
	cin >> N >> P;
	vector<int> need(N);
	for(auto &x : need) cin >> x;
	vector<deque<ll>> ingr(N, deque<ll>(P));
	for(auto &x : ingr)
	{
		for(auto &y : x) cin >> y;
		sort(x.begin(), x.end());
	}

	int cnt = 0;
	while(ingr[0].size())
	{
		ll minamount = 1;
		for(int i = 0; i < N; ++i)
		{
			while(ingr[i].size() && ingr[i].front() < need[i] * minamount * 9 / 10)
				ingr[i].pop_front();

			if(ingr[i].size())
			{
				if(ingr[i].front() > minamount * need[i] * 11 / 10)
				{
					minamount = (ingr[i].front() * 10 + need[i] * 11 - 1) / (need[i] * 11);
					i = -1;
				}
			}
			else
				ingr[0].clear();
		}

		if(ingr[0].size())
		{
			//cerr << minamount << ": ";
			for(int i = 0; i < N; ++i)
			{
				//cerr << ingr[i].front() << " ";
				ingr[i].pop_front();
			}
			//cerr << endl;
			cnt ++;
		}
	}
	cout << cnt << "\n";
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
}
