#include<bits/stdc++.h>
#define ll long long
#define elif else if
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define lim 1000010
#define sz(a) int(a.size())
#define sc(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld %lld",&a,&b)
#define sc3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define sf(a) scanf("%f",&a)
#define pr(a) printf("%lld",a);
#define pf(a) printf("%f",a);
#define rep(n) for(long long i=0;i<n;i++)
#define forab(a,b) for(long long i=a;i<b;i++)
#define INF 1e18
#define Sort(a) sort(a.begin(),a.end())
using namespace std;
int main()
{
    ll t,k;
    cin>>t;
    string s;
    rep(t)
    {
        cin>>s>>k;
        ll j=0,n=s.length(),ans=0;
        bool flag=true;
        while(j<=n-k)
        {
            if(s[j]=='-')
            {
                ans++;
                for(ll m=j;m<j+k;m++)
                    if(s[m]=='-')
                    s[m]='+';
                    else
                        s[m]='-';
            }
            j++;
        }
        //cout<<s;
        while(j<n)
     {

         if(s[j]=='-')
            {
                flag=false;
                cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
                break;
            }
        j++;
    }
        if(flag)
            cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}
