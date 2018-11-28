#include<bits/stdc++.h>
using namespace std;
#define ll                  long long
#define ld                  long double
#define rep(i,n)            for(ll i=0;i<n;i++)
#define hell                1000000007LL
#define vi                  vector<ll>
#define vii                 vector< vi >
#define pb                  push_back
#define mp                  make_pair
#define fi                  first
#define se                  second
#define pii                 pair<ll,ll>
#define all(c)              c.begin(),c.end()
#define sz(c)               c.size()
ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }
ll power(ll x, ll y,ll p)
{
    ll res=1;
    x=x%p;
    while(y>0)
    {
        if(y&1)
            res=((res%p)*(x%p))%p;
        y=y>>1;
        x=((x%p)*(x%p))%p;
    }
    return res;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t,T;
    cin>>t;
    T=t;
    while(t--)
    {
        string s;
        ll k,flag1=1,flag2=1,c1=0,c2=0;
        cin>>s>>k;
        string temp=s;
        rep(i,sz(s))
        {
            if(sz(temp)-i<k) break;
            else if(temp[i]=='-')
            {
                c1++;
                ll in=-1;
                rep(j,k)
                {
                    if(temp[j+i]=='-') temp[j+i]='+';
                    else
                    {
                        if(in==-1) in=j+i;
                        temp[j+i]='-';
                    }
                }
                if(in!=-1) i=max(i,in-1);
            }
        }
        rep(i,sz(s)) if(temp[i]=='-') flag1=0;
        reverse(all(s));
        temp=s;
        reverse(all(s));
        rep(i,sz(s))
        {
            if(sz(temp)-i<k) break;
            else if(temp[i]=='-')
            {
                c2++;
                ll in=-1;
                rep(j,k)
                {
                    if(temp[j+i]=='-') temp[j+i]='+';
                    else
                    {
                        if(in==-1) in=j+i;
                        temp[j+i]='-';
                    }
                }
                if(in!=-1) i=max(i,in-1);
            }
        }
        rep(i,sz(s)) if(temp[i]=='-') flag2=0;
        if(flag1==0 && flag2==0) cout<<"Case #"<<T-t<<": "<<"IMPOSSIBLE"<<endl;
        else if(flag1==1 && flag2==1) cout<<"Case #"<<T-t<<": "<<min(c1,c2)<<endl;
        else if(flag1==1) cout<<"Case #"<<T-t<<": "<<c1<<endl;
        else cout<<"Case #"<<T-t<<": "<<c2<<endl;
    }
    return 0;
}

