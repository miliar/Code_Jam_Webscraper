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
#define A 2000003
#define PIE 3.141592653589793238462643383279502884197169399
#define BLOCK 800 // ~sqrt(N)
#define pa pair<ll,ll>
// __builtin_popcount() }
string s;
int main()
{	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	ll t,k,l,ans,d,j,c;
	cin>>t;
	fr(z,1,t)
	{	ans=0;c=0;
		cin>>s;cin>>k;
		s=" "+s;
		l=s.size();
		for(int i=1;i<=l-k+1;i++)
		{
			if(s[i]=='-')
			{
				ans++;
				d=k;j=i;
				while(d--)
				{
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
					j++;
				}
			}
		}
		printf("Case #%d: ",z);
		fr(i,1,l) if(s[i]=='-') c++;
			if(c>0) cout<<"IMPOSSIBLE\n";
		else cout<<ans<<endl;
	}

	
}  
