#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

set<ll> s;
map<ll, ll> m;
ll t, n, k;

int main()
{
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out");
	in >> t;
	for(ll i = 1; i <= t; i++)
	{
		in >> n >> k; out << "Case #" << i << ": "; 
		s.clear(); m.clear();
		s.insert(-n); m[n]++;
		while (true)
		{
			ll x = *s.begin();
			s.erase(s.begin()); x = -x;
//			out << ": " << x << " " << k << endl;
			ll e1, e2;
			e1 = x / 2ll, e2 = x - e1 - 1ll;
			if (e1 < e2) swap(e1, e2);
			if (m[x] >= k) 
			{
				out << e1 << " " << e2 << endl;
				break;
			}
			ll g = m[x];
			k -= g;
			s.insert(-e1); s.insert(-e2);
			if (m.find(e1) == m.end()) m[e1] = g;
			else					m[e1] += g;
//			if (e1 == e2) continue;
			if (m.find(e2) == m.end()) m[e2] = g;
			else					m[e2] += g;
 		}
	}
	return 0;
}
