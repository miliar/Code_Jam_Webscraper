#include<bits/stdc++.h>

using namespace std;

int n,k;

long double recurs(int curr, long double v, int last, pair<long double, long double> a[] )
{
	if(k==curr||last==n-1)
	{
		return v;
	}
	long double ans = v;
	for(int i=last+1;i<n;i++)
	{
		long double tmp;
		if(curr) tmp = recurs(curr+1, v + a[i].first*a[i].second*2*M_PI , i, a);
		else tmp = recurs(curr+1, v + (long double)(a[i].second*2+a[i].first)*a[i].first*M_PI, i, a);
		ans = max(ans,tmp);
	}
	return ans;
}

int main()
{
	int t;
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout<<std::fixed<<std::showpoint<<std::setprecision(9);
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		cin>>n>>k;

		pair<long double, long double> a[n];
		for(int i=0;i<n;i++)
		{
			cin>>a[i].first>>a[i].second;
			
		}
		sort(a,a+n);
		for(int i=0;i<n/2;i++) swap(a[i],a[n-i-1]);
		cout<<"Case #"<<cas<<": "<<recurs(0,0,-1,a)<<'\n';
	}
	return 0;
}
