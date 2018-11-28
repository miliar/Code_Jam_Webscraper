#include <bits/stdc++.h>
using namespace std;
double pi = 3.14159265358979323846;

int main()
{
	cout<<setprecision(9)<<fixed;
	int t;
	cin>>t;
	for(int z = 1;z<=t;z++)
	{
		int n,k;
		cin>>n>>k;
		double r,h;
		vector <pair<double,double> > v;
		v.clear();
		for(int i=0;i<n;i++)
		{
			cin>>r>>h;
			double mul = r*h;
			v.push_back(make_pair(mul,r));
		}
		sort(v.begin(),v.end(),greater<pair<double,double> >());
		double area = 0.0,maxr = 0.0;
		for(int i=0;i<k-1;i++)
		{
			area += v[i].first;
			maxr = max(maxr,v[i].second);
		}
		double finarea = 0.0;
		for(int i=k-1;i<n;i++)
		{
			finarea = max(finarea,2*pi*area + 2*pi*v[i].first + pi*v[i].second*v[i].second);
		}
		area += v[k-1].first;
		finarea = max(finarea,2*pi*area + pi*maxr*maxr);
		cout<<"Case #"<<z<<": "<<finarea<<endl;
	}
	return 0;
}