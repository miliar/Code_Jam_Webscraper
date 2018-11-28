#include <bits/stdc++.h>
#define mp make_pair
#define ff first
#define se second
#define pb push_back
#define nn 400100
#define pii pair<int,int>
#define mt make_tuple
#define ll long long int
#define pdd pair<long double,long double>
#define db double
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define inf 10000000000010ll
#define logn 20
#define mod 1000000007
#define mt make_tuple
 
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
    	cout<<"Case #"<<tt<<": ";
    	int n;
    	long db d;
    	cin>>d>>n;
    	pdd p;
    	long db maxt=0,tm=0;
    	for(int i=0;i<n;i++)
    	{
    		cin>>p.ff>>p.se;
    		tm=(d-p.ff)/p.se;
    		maxt=max(tm,maxt);
    	}
    	long db ans=(d/maxt);
    	cout<<fixed<<setprecision(7)<<ans<<endl;
    }
    return 0;
}