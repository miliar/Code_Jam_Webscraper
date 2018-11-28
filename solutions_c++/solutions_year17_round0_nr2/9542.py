#include<bits/stdc++.h>
#define MOD 1000000007
using namespace std;
typedef long long int ll;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll T,p;
	cin>>T;
	for(p=1;p<=T;p++)
	{
		ll n;
		cin>>n;
		ll a[500],i=0,x;
		while(n>0)
		{
			x=n%10;
			a[i]=x;
			n=n/10;
			i++;
		}
		ll k,y;
		for(k=0;k<i-1;k++)
		{
			if(a[k]<a[k+1])
			{
				a[k+1]=a[k+1]-1;
				for(y=0;y<=k;y++)
				{
					a[y]=9;
				}	
			}
		}
		ll z;
		sort(a,a+i);
		if(a[0]==0)
		{
			cout<<"Case #"<<p<<": ";
			for(z=1;z<i;z++)
			{
				cout<<a[z];
			}
		}
		else
		{
			cout<<"Case #"<<p<<": ";
			for(z=0;z<i;z++)
			{
				cout<<a[z];
			}
		}
		cout<<endl;
	}
	
	return 0;
}


