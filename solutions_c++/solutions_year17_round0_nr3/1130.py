#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		ll n,i,k;
		cin>>n>>k;
		ll a[2],b[2];
		a[0]=n;
		a[1]=1;
		b[0]=n-1;
		b[1]=0;
		ll temp=k,cnt=0;
		while(temp>0)
		{
			cnt++;
			temp/=2;
		}
		ll sub=0,m=1;
		for(i=1;i<cnt;i++)
		{
			ll u[2],v[2];
			u[0]=a[0]/2;
			v[0]=u[0]-1;
			if(a[0]%2==1)
			{
				u[1]=2*a[1]+b[1];
				v[1]=b[1];
			}
			else
			{
				u[1]=a[1];
				v[1]=a[1]+2*b[1];
			}
			a[0]=u[0];
			a[1]=u[1];
			b[0]=v[0];
			b[1]=v[1];
			sub+=m;
			m*=2;
		}
		sub=k-sub;
		ll ans1,ans2;
		if(sub<=a[1])
		{
			ans1=a[0]/2;
			ans2=a[0]-ans1-1;
		}
		else
		{
			ans1=b[0]/2;
			ans2=b[0]-ans1-1;
		}
		cout<<"Case #"<<z<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}