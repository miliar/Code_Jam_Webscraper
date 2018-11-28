#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vl vector<ll>

#ifndef ONLINE_JUDGE
#  define dbg(x) (cerr << #x << " = " << (x) << endl)
#define dbg2(x,y) (cerr<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<endl)
#else
#define dbg(x) 0
#define dbg2(x,y) 0
#endif

#define N 1234567

string s;
ll n,sz,pw[19];

void pre()
{
    s.clear();
    while(n)
    {
        s.push_back((n%10)+'0');
        n=n/10;
    }
    reverse(s.begin(),s.end());
    pw[0]=1;
    for(ll i=1; i<=18; i++)
        pw[i]=pw[i-1]*10;
    sz=s.size();
}

ll solve(ll idx,ll val,ll alreadyGrt)
{
    ll currVal=s[idx]-'0';
    if(idx==sz-1)
    {
        if(alreadyGrt==0)
        {
            if(val<=currVal)
                return val;
            return -1;
        }
        else
            return 9;
    }
    if(alreadyGrt==1)
    {
        return 9*pw[sz-1-idx]+solve(idx+1,9,1);
    }
    else
    {
        if(val>currVal)
            return -1;
        else if(val<currVal)
        {
            return (val*pw[sz-1-idx]+solve(idx+1,9,1));
        }
        else
        {
            ll ans=-1;
            for(ll i=val; i<=9; i++)
            {
                ll tmp=solve(idx+1,i,0);
                if(tmp!=-1)
                    ans=max(ans,pw[sz-1-idx]*val+tmp);
            }
            return ans;
        }
    }
}

int main()
{
    ll t,i;
    freopen("IP.txt","r",stdin);
    freopen("OPPP","w",stdout);
    cin>>t;
    ll K=1;
    while(t--)
    {
        cin>>n;
        cout<<"Case #"<<K++<<": ";
        pre();
        ll ans=0;
        if(sz>=2)
        {
            for(ll i=1; i<sz; i++)
                ans=ans*10+9;
        }
        for(ll i=1; i<=9; i++)
            ans=max(ans,solve(0,i,0));
        cout<<ans<<endl;
    }
}

