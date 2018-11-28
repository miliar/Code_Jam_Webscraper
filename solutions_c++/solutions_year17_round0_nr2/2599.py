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
	ll t,l;
	cin>>t;
	fr(z,1,t)
	{
		cin>>s;
		l=s.size();
		s=" "+s;
		for(int i=l;i>1;i--)
		{
			if(s[i-1]>s[i])
			{
				s[i-1]--;
				fr(j,i,l) s[j]='9';
			}
		}
		ll m;
		for(m=1;m<=l;m++)
		{
			if(s[m]!='0') break;

		}
		printf("Case #%d: ",z);
		for(int i=m;i<=l;i++) cout<<s[i];cout<<endl;
	}

	
}  
