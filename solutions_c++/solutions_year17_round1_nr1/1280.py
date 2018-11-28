/*input
1
6 2
??
??
?A
?D
?B
EC
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define F(i,a,b) for(ll i = a; i <= b; i++)
#define RF(i,a,b) for(ll i = a; i >= b; i--)
#define pii pair<ll,ll>
#define PI 3.14159265358979323846264338327950288
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define P(x) printf("%d\n",x)
#define all(v) v.begin(),v.end()
char arr[30][30];
int main() 
{
	std::ios::sync_with_stdio(false);
	freopen("is1.txt","r",stdin);
	freopen("os1.txt","w",stdout);
	ll tc=1;
	ll t;
	cin>>t;
	//S(t);
	while(t--)
	{
		cout<<"Case #"<<tc++<<":"<<endl;
		ll r,c;
		cin>>r>>c;
		F(i,1,r)
		{
			F(j,1,c)
			{
				cin>>arr[i][j];
			}
		}
		F(i,1,r)
		{
			bool emptyy = 1;
			F(j,1,c)
			{
				if(arr[i][j]!='?')
					emptyy = 0;
			}
			if(!emptyy)
			{
				F(j,2,c)
				{
					if(arr[i][j]=='?')
						arr[i][j] = arr[i][j-1];
				}
				RF(j,c-1,1)
				{
					if(arr[i][j]=='?')
						arr[i][j] = arr[i][j+1];
				}
			}
			if(emptyy)
			{
				if(i > 1)
				{
					F(j,1,c)
						arr[i][j] = arr[i-1][j];
				}
			}
		}
		RF(i,r,1)
		{
			bool emptyy = 1;
			F(j,1,c)
			{
				if(arr[i][j]!='?')
					emptyy = 0;
			}
			if(!emptyy)
			{
				F(j,2,c)
				{
					if(arr[i][j]=='?')
						arr[i][j] = arr[i][j-1];
				}
				RF(j,c-1,1)
				{
					if(arr[i][j]=='?')
						arr[i][j] = arr[i][j+1];
				}
			}
			if(emptyy)
			{
				if(i < r)
				{
					F(j,1,c)
						arr[i][j] = arr[i+1][j];
				}
			}	
		}
		F(i,1,r)
		{
			F(j,1,c)
				cout<<arr[i][j];
			cout<<endl;
		}
	}
	return 0;
}