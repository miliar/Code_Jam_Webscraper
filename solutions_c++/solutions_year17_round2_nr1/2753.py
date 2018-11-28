#include<bits/stdc++.h>
using namespace std;
long long t,d,n,i,tt,a,v;
double mi;
int main()
{
	freopen("r1bain.txt","r",stdin);
	freopen("r1baout.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		tt++;
		cin>>d>>n;
		mi=999999999999999;
		for(i=1;i<=n;i++)
		{
			scanf("%lld %lld",&a,&v);
			mi=min(mi,(double)d/(double)((double)(d-a)/(double)v));
		}
		printf("Case #%lld: ",tt);
		cout<<fixed<<setprecision(10)<<mi<<endl;
	}
}
