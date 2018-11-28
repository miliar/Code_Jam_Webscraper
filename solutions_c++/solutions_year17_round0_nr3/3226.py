#include <bits/stdc++.h>
using namespace std;
#define f(i,a,b) for(int i=a;i<b;i++)
#define b(i,a,b) for(int i=a;i>b;i--)
#define mpr(a,b) make_pair(a,b)
#define prll pair<ll,ll>
#define si(s) scanf("%d",&s)
#define pri pair<int,int>
#define ll long long
#define inf INT_MAX/10
#define gmax 1005
#define mod 1000000009
#define mod1 1610612741
#define mod2 1000000009
#define line cout<<"\n"
#define bp __builtin_popcount
#define pb push_back
#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define getfile freopen("C:\\Users\\VISHAL ASHANK\\Desktop\\C-large.in","r",stdin)
#define givefile freopen("C:\\Users\\VISHAL ASHANK\\Desktop\\inp2.txt","w",stdout)
ll fastpow(ll n)
{
    ll ans=1;ll two=2;
    while(n!=0)
    {
        //cout<<two<<" "<<n<<endl;
        if(n&1==1)
        {
            ans=ans*two;
        }
        two=two*two;
        n=n>>1;
    }
    return ans;
}
void ans(ll n)
{
    if(n%2==0)
        cout<<n/2<<" "<<n/2-1<<endl;
    else
        cout<<n/2<<" "<<n/2<<endl;

}
main()
{
    getfile;
    givefile;
    //ll n;cin>>n;cout<<fastpow(n);
    int t,tot;
    cin>>t;tot=t;
    while(t--)
    {
        ll n,k;
        cin>>n>>k;
        ll m=k;int id=0;
        while(m!=0)
        {
            id++;
            m=m>>1;
        }
        //cout<<id<<endl;
        //cout<<fastpow(id-1)<<endl;
        ll pwr=fastpow(id-1);
        ll val=n-pwr+1;
        ll md=val%pwr;
        ll quo=val/pwr;
        //cout<<val<<" "<<md<<" "<<quo<<endl;
        cout<<"Case #"<<tot-t<<": ";
        if(k<=pwr-1+md)
        {
            ans(quo+1);
        }
        else
        {
            ans(quo);
        }
        //cout<<endl;

    }
}
