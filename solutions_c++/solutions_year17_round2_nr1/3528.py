#include <bits/stdc++.h>

using namespace std;

bool compare(const pair<int,int>& a,const pair<int,int>& b)
{
	return a.first<b.first; 
}

int main()
{
	long long int i,u,t,a,b,d,n;
	double curmax;
	std::cout << std::fixed;
    std::cout << std::setprecision(7);
	cin>>t;
	for(u=0;u<t;u++)
	{
		vector<pair<int,int> > v;
		cin>>d>>n;
		int dist[n];
		double time[n];
		for(i=0;i<n;i++)
		{
			cin>>a>>b;
			v.push_back(make_pair(d-a,b)); 
		}
		curmax = 0;
		sort(v.begin(),v.end(),compare);

		for(i=v.size()-1;i>=0;i--)
		{
			time[i] = max(curmax,((v[i].first)*1.0/(v[i].second)));
			curmax = time[i];
		}
		cout<<"Case #"<<u+1<<": "<<float(d*1.0/time[0])<<"\n";
	}
}