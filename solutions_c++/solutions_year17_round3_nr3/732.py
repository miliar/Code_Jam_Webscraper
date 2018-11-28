#include<bits/stdc++.h>

using namespace std;

const double eps = 1e-18;

void solve()
{
	int n, k;
	double u, p, tmp = 0.0, ans = 1.0;
	map<double, int> mp;
	cin>>n>>k>>u;
	for(int i=0; i<n; i++) 
		cin>>p,
		mp[p]++,
		tmp += 1.0-p;

	cout<<fixed<<setprecision(12);
	if(tmp-u<eps) {
		cout<<ans<<endl;
		return;
	}

	int cnt;
	double curr, nxt;
	while(u>eps) {
		cnt = mp.begin()->second;
		curr = mp.begin()->first;
		mp.erase(mp.begin());

		if(mp.size()) 
			nxt = mp.begin()->first;
		else 
			nxt = 1.0;

		tmp = min(u, 1.0*cnt*(nxt-curr));

		mp[curr+tmp/(1.0*cnt)] += cnt;

		if(u-tmp<eps) 
			break;
		else 
			u -= tmp;
	}

	for(auto it: mp) 
		for(int i=0; i<it.second; i++) ans *= min(1.0, it.first);

	cout<<ans<<endl;
}

int main()
{
	int T;
	cin>>T;

	for(int i=1; i<=T; ++i)
		cout<<"Case #"<<i<<": ",
		solve();
	return 0;
}