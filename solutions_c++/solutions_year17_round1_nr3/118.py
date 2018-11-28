#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
	ll Hd, Ad, Hk, Ak, B, D;
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	
	set<tuple<ll, ll, ll, ll>> done;
	priority_queue<tuple<ll, ll, ll, ll, ll>> next;
	next.emplace(0, Hd, Ad, Hk, Ak);

	while(next.size())
	{
		ll turns, hd, ad, hk, ak;
		tie(turns, hd, ad, hk, ak) = next.top();
		next.pop();

		if(done.count(make_tuple(hd, ad, hk, ak)))
			continue;
		done.emplace(hd, ad, hk, ak);

		if(hk <= 0)
		{
			cout << -turns << "\n";
			return;
		}
		if(hd <= 0)
			continue;
		
		{ //attack
			ll nhd = hd - ak;
			ll nad = ad;
			ll nhk = hk - ad;
			ll nak = ak;
			next.emplace(turns - 1, nhd, nad, nhk, nak);
		}
		{ //buff
			ll nhd = hd - ak;
			ll nad = ad + B;
			ll nhk = hk;
			ll nak = ak;
			next.emplace(turns - 1, nhd, nad, nhk, nak);
		}
		{ //cure
			ll nhd = Hd - ak;
			ll nad = ad;
			ll nhk = hk;
			ll nak = ak;
			next.emplace(turns - 1, nhd, nad, nhk, nak);
		}
		{ //debuff
			ll nak = max(0ll, ak - D);
			ll nhd = hd - nak;
			ll nad = ad;
			ll nhk = hk;
			next.emplace(turns - 1, nhd, nad, nhk, nak);
		}
	}
	cout << "IMPOSSIBLE\n";
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
