/*Abhilash Tayade
	CSE MNNIT-ALLAHABAD 
	3rd yr :D  */
 
#include<bits/stdc++.h>			
using namespace std;
#define mk make_pair
#define pb push_back
#define ll long long int
#define lf double
#define M  1000000007
#define INF 1e18
#define fi first
#define se second
#define fr(u,v,w) for(int u=v;u<=w;u++)
#define frr(u,v,w) for(int u=v;u>=w;u--)
#define S 123456
#define A 200003
#define PIE 3.141592653589793238462643383279502884197169399
#define BLOCK 800 // ~sqrt(N)
#define pa pair<ll,ll>
// __builtin_popcount() }
string s[A];ll a[A];
int main()
{	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	ll t,r,c,co,k;
	cin>>t;
	fr(z,1,t)
	{
		cin>>r>>c;
		fr(i,0,r-1) cin>>s[i],a[i]=0;
		fr(i,0,r-1)
		{	co=0;
			fr(j,0,c-1)
			{
				if(s[i][j]=='?') co++;
			}
			if(co==c) a[i]=1;
			else
			{
				fr(j,0,c-1)
				{
					if(s[i][j]!='?')
					{
						k=j-1;
						while(k>=0&&s[i][k]=='?')
							s[i][k]=s[i][j],k--;
						k=j+1;
						while(k<=c-1&&s[i][k]=='?')
							s[i][k]=s[i][j],k++;
					}
				}
			}
		}int d;
		if(a[0]==1)
		{
			fr(i,1,r-1)
			{
				if(a[i]==0) {d=i; break;}
			}
			frr(i,d,1)
		{	a[i-1]=0;
			fr(j,0,c-1) s[i-1][j]=s[i][j];
		}
		}
		
		fr(i,0,r-1)
		{
			if(a[i]==1)
			{
				if(i==0)
				{
					fr(j,0,c-1) s[i][j]=s[i+1][j];
				} 
				else 
				{
					fr(j,0,c-1) s[i][j]=s[i-1][j];
				}
			}
		}
		printf("Case #%d: \n",z);
		fr(i,0,r-1) cout<<s[i]<<endl;
	}
	
}  
