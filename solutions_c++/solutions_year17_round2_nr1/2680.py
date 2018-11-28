#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define max 100010
#define pii pai<ll,ll>
#define vec vector<ll>
#define dl long double
ll i,j,k,t,n;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ansl1.txt","w",stdout);
cin>>t;
for(i=1;i<=t;i++)
  {
  	dl dest;
  cin>>dest;
  cin>>n;
  dl maxi=-1.000;
  for(j=1;j<=n;j++)
  {
  	dl a,b;
  	cin>>a>>b;
  	dl kase=1.0*(dest-a)/b;
  	if(kase>maxi)
  	maxi=kase;
  }

  cout<<"Case #"<<i<<": ";
  dl ans=dest/maxi;
  cout<<setprecision(9)<<ans<<endl;
  //printf("%0.9llf\n",ans);
  }
}
