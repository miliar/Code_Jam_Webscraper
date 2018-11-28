#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	int j,t;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		lli n,i;
		double d,a,b;
		cin>>d>>n;
		vector< pair<double,double> > v;
		double t[n];
		for(i=0;i<n;i++)
		{
			cin>>a>>b;
			v.push_back(make_pair(a,b));
		}
		sort(v.begin(), v.end());
		for(i=0;i<n;i++)
		{
			t[i]=(d-v[i].first)/v[i].second;
		}
		for(i=n-2;i>=0;i--)
		{
			if(t[i]<t[i+1])
			t[i]=t[i+1];
		}
	    double r=d/t[0];
		printf("Case #%d: %.7f\n",j,r);
		//cout<<"Case #"<<j<<": "<<r<<endl;
	}
	return 0;
}
