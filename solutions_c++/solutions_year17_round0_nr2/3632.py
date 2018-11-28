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
    ll t,n;
    string s;
    cin>>t;
    rep(t)
    {
        cin>>s;
        n=s.length();
        if(n==1)
            cout<<"Case #"<<i+1<<": "<<s<<endl;
        else
        {
            for(ll j=0;j<n-1;j++)
            {
                if(s[j+1]<s[j])
                {
                    while(j>0 && s[j-1]==s[j])
                        j--;
                    s[j]--;
                    j++;
                    while(j<n)
                        {
                            s[j]='9';
                            j++;
                        }
                    break;
                }
            }
            cout<<"Case #"<<i+1<<": ";
            ll j=0;
            while(s[j]=='0')
                j++;
            while(j<n)
            {
                cout<<s[j];
                j++;
            }
            cout<<endl;
        }
    }
    return 0;
}
