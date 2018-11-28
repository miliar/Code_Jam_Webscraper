/*input
1
15 20 0 10 0 11 0
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vll;
int main()
{
	ios::sync_with_stdio(false);
	ll t;
	cin>>t;
	for(ll test=1; test<=t; test++)
	{
		ll n,r,o,y,b,g,v;
		cin>>n;
		string s="";
		cin>>r>>o>>y>>g>>b>>v;
		if(r+b<y || b+y<r || y+r<b)
			{
				cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
				continue;
			}

		vector<pair<ll,string> > vp;
		vp.push_back(make_pair(r,"R"));
		vp.push_back(make_pair(y,"Y"));
		vp.push_back(make_pair(b,"B"));
		sort(vp.rbegin(), vp.rend());
		while(vp[0].first!=0)
		{
			s+=vp[0].second;
			vp[0].first--;
			if(vp[1].first)
			{
				s+=vp[1].second;
				vp[1].first--;
			}

			sort(vp.rbegin(), vp.rend());
		}
		if(s[0]==s[s.length()-1])
		swap(s[s.length()-1], s[s.length()-2]);
		cout<<"Case #"<<test<<": "<<s<<endl;

	}
}