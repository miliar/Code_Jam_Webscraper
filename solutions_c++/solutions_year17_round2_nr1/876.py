#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<string.h>
#include<set>
#include<iomanip>
using namespace std;
vector<pair<double,double> >v;
int main()
{
	int t;
	cout<<fixed;
	cin>>t;
	for(int o=1;o<=t;o++)
	{
		int n;
		double d;
		cin>>d>>n;
		v.clear();
		for(int i=0;i<n;i++)
		{
			int x,y;
			cin>>x>>y;
			v.push_back(make_pair(x,y));
		}
		sort(v.begin(),v.end());
		double sol=0,nt=0,rq=0;
		nt=(d-v[n-1].first)/(v[n-1].second);
		for(int i=n-2;i>=0;i--)
		{
			rq=(d-v[i].first)/(nt);
			if(rq>=v[i].second)
			{
				nt=(d-v[i].first)/(v[i].second);
			}
		}
		rq=(d)/(nt);
		cout<<setprecision(7)<<"Case #"<<o<<": "<<rq<<endl;
	}
}