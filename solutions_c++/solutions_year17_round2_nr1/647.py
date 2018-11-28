#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
int main()
{
	int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		double d;
		int n,i;
		cin>>d>>n;
		vector<pair<double,double> >v;
		for(i=0;i<n;i++)
		{
			double k,s;
			cin>>k>>s;
			v.push_back(make_pair(k,s));
		}
		sort(v.begin(),v.end());
		double val=0;
		for(i=n-1;i>=0;i--)
		{
			val=max(val,(d-v[i].first)/v[i].second);
		}
		val=d/val;
		printf("Case #%d: ",z);
		printf("%.8lf\n",val);
	}
	return 0;
}