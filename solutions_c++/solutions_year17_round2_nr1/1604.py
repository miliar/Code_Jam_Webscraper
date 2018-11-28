#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define ll double
#define mp make_pair
#define MAX 100005
#define inf 1e18
#define mod 1000000007
#define pb push_back
#define INF 1000005
#define pii pair<ll,ll>

//ll a[MAX];

/*ll gcd(ll a, ll b)
{
    if (a == 0)
        return b;
    return gcd(b%a, a);
}*/

pii a[MAX];

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("beta.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n,t;
    cin>>t;

    ll k,d;

    for(int k=1;k<=t;k++)
    {
        cout<<"Case #"<<k<<": ";
        cin>>d>>n;
        ll ans;
        int i;
        for(i=0;i<n;i++)
        {
            cin>>a[i].f>>a[i].s;
        }

        sort(a,a+n);
        ll tim=0,maxm=-1;
        /*if(n==1)
        { tim=(d-a[0].f)/a[0].s;
           ans=d/tim;
           cout<<ans<<endl;
           continue;
        }*/
        for(i=n-1;i>=0;i--)
        {
            tim=(d-a[i].f)/a[i].s;
            if(tim>maxm)
                maxm=tim;
        }
        cout<<fixed;
        cout<<setprecision(10);
        cout<<d/maxm<<endl;
    }

    return 0;
}
