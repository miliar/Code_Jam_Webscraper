#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cout<<setprecision(6)<<fixed;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		vector<double> v;
		double d,n,k,s;
		cin>>d>>n;
		for(int y=0;y<n;y++)
		{
			cin>>k>>s;
			v.push_back((d-k)/s);
		}
		sort(v.begin(),v.end());
		cout<<"Case #"<<z<<": "<<d/v[n-1]<<'\n';
	}

	return 0;
}