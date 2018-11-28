#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll find(ll l[],ll r[],ll n,ll f[])
{
	vector<ll> v,v1;
	v.clear();v1.clear();
		ll i,ind,m1=-1,m2=-1;
		for(i=0;i<n;i++)
		{
			if(f[i]!=1)
			{
			if(min(l[i],r[i])>m1)
			{
				m1=min(l[i],r[i]);
			}
		   }
		}
		for(i=0;i<n;i++)
		{
			if(min(l[i],r[i])==m1&&f[i]==0)
			v.push_back(i);
		}
		if(v.size()>1)
		{
			for(i=0;i<v.size();i++)
	     	{
	     		if(f[v[i]]==1)
	     		continue;
				if(max(l[v[i]],r[v[i]])>m2)
				{
					m2=max(l[v[i]],r[v[i]]);
				}
		    }
		   // cout<<m2<<endl;
			for(i=0;i<v.size();i++)
			{
				if(f[v[i]]==0&&max(l[v[i]],r[v[i]])==m2)
				v1.push_back(v[i]);
			}
		//	cout<<v1[0]<<endl;
			ind=v1[0];
		}
		else
		ind=v[0];
		return ind;
}
int main()
{
	freopen("inp.in","r",stdin);
			freopen("ou1.out","w",stdout);
	ll t,c=1;
	cin>>t;
	while(t--)
	{
		ll n,k;
		cin>>n>>k;
		ll f[n];
		ll l[n];
		ll r[n],i;
		f[0]=0;f[n-1]=0;
		l[0]=0;r[0]=n-1;
		l[n-1]=n-1;r[n-1]=0;
		for(i=1;i<n-1;i++)
		{
			l[i]=l[i-1]+1;
			r[i]=r[i-1]-1;
			f[i]=0;
		//	cout<<r[i]<<" "<<r[i-1]<<endl;
		}
	//	for(i=0;i<n;i++)
	//	cout<<l[i]<<" "<<r[i]<<endl;
	ll ind;
		for(i=0;i<k;i++)
		{
			 ind=find(l,r,n,f);
			f[ind]=1;
			if(i==k-1)
			break;
		//	cout<<ind<<endl;
			for(ll j=ind+1;j<n;j++)
			{
				if(l[j]==0)
				break;
				if(j==ind+1)
				l[j]=0;
				else
				l[j]=l[j-1]+1;
			}
			for(ll j=ind-1;j>=0;j--)
			{
				if(r[j]==0)
				break;
				if(j==ind-1)
				r[j]=0;
				else
				r[j]=r[j+1]+1;
			}
		//	for(i=0;i<n;i++)
		//	cout<<l[i]<<" "<<r[i]<<endl;
		}
		
		cout<<"Case #"<<c<<": "<<max(l[ind],r[ind])<<" "<<min(l[ind],r[ind])<<endl;
		c++;
	}
}
