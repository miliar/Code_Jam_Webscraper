#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define X first
#define Y second
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define forn(n) for(ll i=0;i<n;i++)
#define forin(n1,n2) for(ll i=n1;i<n2;i++)
using namespace std;
typedef pair<int,int>pii;
FILE *ptr1=freopen("in.txt","r",stdin);
FILE *ptr2=freopen("out.txt","w",stdout);
int main()
{
// 	ios_base::sync_with_stdio(false); cin.tie(NULL);
	ll tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		ll n;
		cin>>n;
		ll a[6];
		for(int i=0;i<6;i++) cin>>a[i];
		if((n<2*a[0])||(n<2*a[2])||(n<2*a[4]))
		{
		cout<<"Case #"<<t<<": IMPOSSIBLE"<<"\n";
		continue;	
		}
		cout<<"Case #"<<t<<": ";
		ll  r=a[0],y=a[2],b=a[4];
		if(r>=y&&r>=b)
		{
			while(r)
			{
				cout<<"R";
				r--;
				if(y>b)
				{
					cout<<"Y"; y--;
					if((y+b)>r)
					{
						cout<<"B";b--;
					}
				}
				else
				{
					cout<<"B"; b--;
					if((y+b)>r)
					{
						cout<<"Y";y--;
					}
				}
			}
		}
		else
		if(y>=r&&y>=b)
		{
			while(y)
			{
				cout<<"Y";
				y--;
				if(r>b)
				{
//					if(r>0)
					cout<<"R"; r--;
					if((r+b)>y&&b>0)
					{
						cout<<"B";b--;
					}
				}
				else
				{
//					if(b>0)
					cout<<"B"; b--;
					if((r+b)>y)
					{
						cout<<"R";r--;
					}
				}
			}
		}
		else 
		if(b>=y&&b>=r)
		{
			while(b)
			{
				cout<<"B";
				b--;
				if(r>y)
				{
					cout<<"R"; r--;
					if((y+r)>b)
					{
						cout<<"Y";y--;
					}
				}
				else
				{
					cout<<"Y";y--;
					if((y+r)>b)
					{
						cout<<"R";r--;
					}
				}
			}
		}
		cout<<"\n";
	}
	return 0;
}

