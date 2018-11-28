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
map<ll,ll>m;
map<ll,ll>::iterator  it;
int main()
{	
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	ll t,n,k,o,e,maxi,mini,p;
	cin>>t;
	fr(z,1,t)
	{
		cin>>n>>k;
		m.clear();
		m[n]=1;
		while(k>0)
		{
			it=m.end();
			it--;
			p=(*it).fi;
			if(p%2==0){
			mini=(p/2)-1;
			maxi=p/2;
			m[(p/2)-1]+=m[p];
			m[p/2]+=m[p];
			k-=m[p];
			m.erase(p);

			}
			else
			{
				mini=(p/2);
			maxi=p/2;
			
			m[p/2]+=2*m[p];
			k-=m[p];
			m.erase(p);
			}
		}
		printf("Case #%d: ",z);
		cout<<maxi<<" "<<mini<<endl;
	}
	
}  
