#include<bits/stdc++.h>
#include<iostream>
#define ll long long int
#define pb push_back
#define mp make_pair
//#define for(i,n) for(int i=0;i<n;i++)
#define start() int t;cin>>t;while(t--)
#define mod 1000000007

using namespace std;
int main()
{    freopen("A-large.in","r",stdin);
      freopen("s.txt","w",stdout);
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		ll d,n;
		double sum,ti;
		double ans;
		double x,y=0;
		cin>>d>>n;
	priority_queue<pair<ll,ll>, vector<pair<ll,ll> >, greater<pair<ll,ll> > >v;
	  for(ll i=0;i<n;i++)
	  {  ll a,b;
	  cin>>a>>b;
	   v.push(mp(b,a));
	  x=(d-a)/(float)b;
	  y=max(y,x); 
	  }
	  //cout<<v.top().first<<" "<<v.top().second;
	  ll s=v.top().first;
	  ll k=v.top().second;
	  sum=d-(k);
	  ans=(double)d/y;
	  cout<<"Case #"<<j<<": ";
	    std::cout << std::fixed << std::showpoint;
    std::cout << std::setprecision(6);
    cout<<ans<<endl;
    
	}
}
