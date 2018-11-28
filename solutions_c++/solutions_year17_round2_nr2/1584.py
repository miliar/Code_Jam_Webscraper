#include <bits/stdc++.h>
#define ll long long int
#define ld long double 
#define MOD 1000000007 
#define mem(a) memset(a,0,sizeof(a))
#define pb push_back
#define ff first
#define ss second 
#define ios ios_base::sync_with_stdio(false);

using namespace std;

ll a[9010];
string ans;

// void f(ll m, ll r, ll y, ll b)
// {
// 	if(m==r)
// 		ans+="R";
// 	else if(m==y)
// 		ans+="Y";
// 	else if(m==b)
// 		ans+="B";
// }

int main()
{
	ll t;
	ll n,r,o,y,g,b,v;
	cin>>t;
	for(ll i=1; i<=t; i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>n>>r>>o>>y>>g>>b>>v;
		// mem(a);
		ans="";
		for(ll i=0; i<=3*n+5; i++)
			ans+=" ";
		if(max(r,max(y,b))>n/2)
			cout<<"IMPOSSIBLE"<<endl;
		else if(r!=0 && y!=0 && b!=0)
		{
			pair<ll,char> mx,mn,md;
			 mx.ff=max(r,max(y,b));
			mn.ff=min(r,min(y,b));
			md.ff=r+y+b-mx.ff-mn.ff; 
			// cout<<md.ff<<endl;
			if(r==y && y==b)
			{
				mx.ss='R';
				md.ss='Y';
				mn.ss='B';
			}
			else if(mn.ff==md.ff)
			{
				if(mx.ff==r)
				{
					mx.ss='R';
					mn.ss='Y';
					md.ss='B';
				}
				else if(mx.ff==y)
				{
					mx.ss='Y';
					mn.ss='R';
					md.ss='B';
				}
				else if(mx.ff==b)
				{
					mx.ss='B';
					mn.ss='R';
					md.ss='Y';
				}
			}
			else if(mx.ff==md.ff)
			{
				if(mn.ff==r)
				{
					mn.ss='R';
					mx.ss='Y';
					md.ss='B';
				}
				else if(mn.ff==y)
				{
					mn.ss='Y';
					mx.ss='R';
					md.ss='B';
				}
				else if(mn.ff==b)
				{
					mn.ss='B';
					mx.ss='R';
					md.ss='Y';
				}
			}
			else
			{
				if(mx.ff==r)
					mx.ss='R';
				else if(mx.ff==b)
					mx.ss='B';
				else 
					mx.ss='Y';
				if(md.ff==r)
					md.ss='R';
				else if(md.ff==b)
					md.ss='B';
				else 
					md.ss='Y';
				if(mn.ff==r)
					mn.ss='R';
				else if(mn.ff==b)
					mn.ss='B';
				else 
					mn.ss='Y';
			}
			ll ind=0;
			
			for(ll i=0; i<3*mx.ff; i+=3)
			{
				ans[i]=mx.ss;
			}
			for(ll i=3*(mx.ff-1)+1; i>=3*(mx.ff-md.ff)+1; i-=3)
			{
				ans[i]=md.ss;
			}
			for(ll i=2; i<3*(mn.ff)+2; i+=3)
			{
				ans[i]=mn.ss;
			}
			for(ll i=0; i<=3*(mx.ff)+4; i++)
			{
				if(ans[i]!=' ')
				cout<<ans[i];
				// if(a[i]==mx)
				// {
				// 	f(mx,r,y,b);
				// }
				// else if(a[i]==md)
				// {
				// 	f(mx,r,y,b);
				// }
				// else if(a[i]==mn)
				// {
				// 	f(mx,r,y,b);
				// }
			}
			cout<<endl;
			// cout<<ans<<endl;
		}
		else if(r==0 or y==0 or b==0)
		{
			ll mx=max(r,max(y,b));
			ll mn=min(r,min(y,b));
			ll md=r+y+b-mx-mn;
			char bb[3];
			if(r==0)
			{
				bb[0]='Y';
				bb[1]='B';
			}
			else if(y==0)
			{
				bb[0]='B';
				bb[1]='R';
			}
			else if(b==0)
			{
				bb[0]='Y';
				bb[1]='R';
			}
			if(md!=mx)
			{
				cout<<"IMPOSSIBLE";
			}
			else
			{
				ll ind=0;
				for(ll i=0; i<md; i++)
				{
					ans[ind++]=bb[0];
					ans[ind++]=bb[1];
				}
				for(ll i=0; i<2*md+5; i++)
				{
					if(ans[i]!=' ')
						cout<<ans[i];
				}
				cout<<endl;
			}
		}
		else if((r==0 && y==0) || (b==0 && y==0) || (r==0 && b==0))
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}