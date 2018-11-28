/*input
1
2 2
AC
DB
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vll;
int main()
{
	ios::sync_with_stdio(false);
	ll test;
	cin>>test;
	for(ll case1 = 1; case1 <=test; case1++)
	{
		ll r,c;
		cin>>r>>c;
		vector<string> v(r,""),ne(r,"");
		for(ll i=0; i<r; i++)
		{
			cin>>v[i];
			ne[i]=v[i];
		}
		for(ll i=0; i<r; i++)
		{
			ll count=0;
			for(ll j=0; j<c; j++)
			{
				if(v[i][j]!='?')
				{
					ll x=j,y=i;
					while(x>0 && ne[y][--x]=='?')
					{
						ne[y][x]=v[i][j];
					}

				    x=j,y=i;
					while(x<c-1 && ne[y][++x]=='?')
					{
						ne[y][x]=v[i][j];
					}						
				}
			}
		}
		for(ll i=1; i<r; i++)
			if(ne[i][0] == '?')
			{
				ne[i]=ne[i-1];
			}

		for(ll i=r-2; i>=0; i--)
			if(ne[i][0] == '?')
			{
				ne[i]=ne[i+1];
			}




		cout<<"Case #"<<case1<<":\n";
		for(ll i=0; i<r; i++)
			cout<<ne[i]<<endl;
	}
}