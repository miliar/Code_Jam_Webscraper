#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define N ((ll)1050)
#define INF ((ll)3e18)

ifstream fin("input.in");
ofstream fout("output.txt");

ll t,d,n;
pair <ld,ld> b[N];
pair <ll,ll> a[N];

bool check(ld x)
{
	for(int i=0;i<n;i++)b[i]=a[i];
	b[0].second=x;
	while(1)
	{
		ld mini=INF;
		ll min_id=0;
		for(int i=0;i<n-1;i++)
		{
			ld dis=b[i+1].first-b[i].first;
			ld s_dif=b[i].second-b[i+1].second;
			if(s_dif>0 && (ld)dis/s_dif<mini)mini=(ld)dis/s_dif,min_id=i;
		}
//		cout<<min_id<<" "<<mini<<"\n";
		for(int i=0;i<n;i++)b[i].first+=b[i].second*mini;
		if(b[0].first>=d)return 1;
		if(min_id==0)return 0;
		b[min_id].second=b[min_id+1].second;
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	fin>>t;
	for(int q=1;q<=t;q++)
	{
		fin>>d>>n;
		for(int i=1;i<=n;i++)fin>>a[i].first>>a[i].second;
		sort(a+1,a+n+1);
		n++;
	//	cout<<check(99.6)<<"\n";
		ld l=0,r=INF;
		for(int i=0;i<150;i++)
		{
			ld mid=(l+r)/2;
			if(check(mid))l=mid;
			else r=mid;
		}
		fout<<"Case #"<<q<<": ";
		fout<<fixed<<setprecision(14)<<l<<"\n";
	}
	
	return 0;
}
