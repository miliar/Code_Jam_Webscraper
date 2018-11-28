#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fast cin.sync_with_stdio(0);cin.tie(0)
pair<double ,double>p[100010];
inline bool comp(pair<double,double>p1,pair<double,double>p2)
{
	return p1.first<p2.first;
}
int main()
{
	int viv=0;
	int t;
	cin>>t;
	while(t--)
	{
		double d;
		ll n,i,r,o,y,g,b,v,cc;
		viv++;
		cout<<"Case #"<<viv<<": ";
		ll put,arr[100010];
		cin>>n>>r>>o>>y>>g>>b>>v;
		ll xx=min(r,min(y,b));
		if(xx==r)
		{
			put=82;
			r=99999999999;
		}
		else if(xx==y)
		{
			put=89;
			y=99999999999;
		}
		else if(xx==b)
		{
			put=66;
			b=99999999999;
		}
		for(i=1;i<=n;i++)
			arr[i]=-1;
		i=1;
		while(xx)
		{
			arr[i]=put;
			xx--;
			i+=2;
		}
		xx=min(r,min(y,b));
		if(xx==r)
		{
			put=82;
			r=99999999999;
		}
		else if(xx==y)
		{
			put=89;
			y=99999999999;
		}
		else if(xx==b)
		{
			put=66;
			b=99999999999;
		}
		while(xx)
		{
			arr[i]=put;
			xx--;
			i+=2;
			if(i>n)
			i=2;
		}


		xx=min(r,min(y,b));
		if(xx==r)
		{
			put=82;
			r=99999999999;
		}
		else if(xx==y)
		{
			put=89;
			y=99999999999;
		}
		else if(xx==b)
		{
			put=66;
			b=99999999999;
		}

		for(i=1;i<=n;i++)
		{
			if(arr[i]==-1)
				arr[i]=put;
		}
		bool ok=true;
		for(i=1;i<n;i++)
		{
			if(arr[i]==arr[i+1])
				ok=false;
		}
		if(arr[1]==arr[n])
			ok=false;
		if(!ok)
		{
			cout<<"IMPOSSIBLE";
		}
		else
		{
			for(i=1;i<=n;i++)
				cout<<(char)arr[i];
		}
		cout<<endl;
	}
}	