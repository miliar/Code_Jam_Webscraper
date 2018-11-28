//SHUBHAM RANA says hello
#include <bits/stdc++.h>
#define sp " "
#define br "\n"
using namespace std;
typedef long long int ll;
typedef set<ll>::iterator si;
typedef map<ll,ll>::iterator mi;
const ll MOD=1000000007;
const ll INF=LLONG_MAX;
const double MU=0.000001;
const double PI=3.14159265359;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	freopen("input_large.txt","r",stdin);
	freopen("output_large.txt","w",stdout);
    ll tt;
    cin>>tt;
    for(ll t=1;t<=tt;t++)
    {
        ll n;
        cin>>n;
        ll k=n;
        ll a[19]={0};
        for(ll i=18;i>=0;i--)
        {
            a[i]=n%10;
            n/=10;
        }
        ll p=19;
        for(ll i=18;i>0;i--)
        {
            if(a[i-1]>a[i])
                p=i;
        }
        if(p!=19)
            a[p-1]--;
        for(ll i=p-1;i>0;i--)
        {
            if(a[i-1]>a[i])
            {
                a[i-1]--;
                a[i]=9;
            }
        }
        for(ll i=p;i<19;i++)
        {
            a[i]=9;
        }
        ll res=0;
        for(ll i=0;i<19;i++)
        {
            res=res*10+a[i];
        }
        cout<< "Case #"<<t<< ": "<<res<<br;
    }
	return 0;
}
