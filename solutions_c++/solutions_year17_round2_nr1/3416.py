#include<bits/stdc++.h>
using namespace std;
bool sortinrev(const pair<double,double> &a, 
               const pair<double,double> &b)
{
       return (a.first > b.first);
}
int main()
{
	int t;
	cin>>t;
	int tn=1;
	while(t--)
	{
		double d;
		int n;
		cin>>d>>n;
		vector<pair<double ,double> >p;
		for(int i=0;i<n;i++)
		{
			double b;
			double c;
			cin>>b>>c;
			p.push_back(make_pair(b,c));
		}
		sort(p.begin(),p.end(),sortinrev);
		double time=0;
		for(int i=0;i<n;i++)
		{
			double dist=d-p[i].first;
			double  t=dist/p[i].second;
			if(t>=time)
				time=t;
		}
		double res=d/time;
		cout<<"Case #"<<tn<<": ";
		printf("%.6f\n",res);
		tn++;
	}
}
				
