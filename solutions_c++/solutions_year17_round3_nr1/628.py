#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ld pi =  3.141592653589793238462643;
const ll maxx = 1e3 + 20;

ll n, k, dp[maxx], r[maxx], ans, h[maxx], sum = 0;
vector <pair<ll, ll> > v;
set<pair<ll, ll> > s;

int main()
{
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out");
//	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	out << setprecision(10) << fixed;
	int t;
	in >> t;
	for(int q = 1; q <= t; q++)
	{
		out << "Case #" << q << ": ";
		in >> n >> k; ans = 0ll ; sum = 0ll;
		s.clear(); v.clear(); fill(dp, dp + maxx, 0ll); //cout << t << " " << v.size() << endl;
		for(ll i = 0; i < n; i++)
		{
			in >> r[i] >> h[i];
			v.push_back({r[i], h[i]});
		}
		sort(v.begin(), v.end());
		for(ll i = 0; i < n; i++)
		{
//			cout << i << "#" << sum << endl;
			ll rr = v[i].first, hh = v[i].second;
			dp[i] = (2ll * rr * hh) + (rr * rr) + sum;
			if (!i) ans = dp[i]; else ans = max(ans, dp[i]);
			s.insert({hh * 2ll * rr, i}); sum += (hh * 2ll * rr);
			if (s.size() > k - 1) 
			{
				pair<ll, ll> u = *s.begin();
				sum -= u.first;
				s.erase(s.begin());
			}
//			if (!i) continue;
			
		}
//		for(int i = 0; i < n; i++)
//			cout << i << " " << dp[i] << endl;
		out << 1ll * ans * pi << '\n';
	}
	return 0;
}
