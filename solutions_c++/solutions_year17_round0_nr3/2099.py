#include<cstdio>
#include<iostream>
#include<set>
#include<map>
#include<set>
using namespace std;
typedef long long ll;

map<ll, ll> mp;
set<ll> st;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		ll n, k;
		cin >> n >> k;
		cout << "Case #" << (q + 1) << ": ";
		mp.clear();
		st.clear();
		ll cnt = 0;
		ll p1 = n / 2LL, p2 = n / 2LL;
		if (n % 2LL == 0) 
			p2--;
		st.insert(p1);
		st.insert(p2);
		mp[p1]++;
		mp[p2]++;
		cnt++;
		if (cnt == k)
		{
			cout << p1 << " " << p2 << "\n";
		}
		else
		{
			while ((int)st.size() > 0)
			{
				set<ll>::iterator i = st.end();
				i--;
				ll v = *i;
				st.erase(i);
				ll x = mp[v];
				mp[v] = 0;
				if (v > 0)
				{
					p1 = v / 2;
					p2 = v / 2;
					if (v % 2 == 0)
						p2--;
					st.insert(p1);
					st.insert(p2);
					mp[p1] += x;
					mp[p2] += x;
					cnt += x;
					if (cnt >= k)
					{
						cout << p1 << " " << p2 << "\n";
						break;
					}
				}
			}
		}
	}
	return 0;
}