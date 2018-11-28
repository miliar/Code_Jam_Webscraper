//algorithmic approach
#include<bits/stdc++.h>
#define ll long long int
using namespace std;
inline bool check(string s)
{
    for(ll i=0;i<s.length()-1;i++)
    {
        if(s[i]>s[i+1])
            return false;
    }
    return true;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    ll t;
    cin>>t;
    for(ll tt=1;tt<=t;tt++)
    {
        string s;
        ll n;
        cin>>s;
        n=s.length();
        while(!check(s))
        {
            for(ll i=0;i<n-1;i++)
            {
                if(s[i]>s[i+1])
                {
                    s[i]=s[i]-1;
                    for(ll j=i+1;j<n;j++)
                        s[j]='9';
                    break;
                }
            }
        }
        ll ans=0;
        for(ll i=0;i<n;i++)
            ans=ans*10+(s[i]-'0');
        printf("Case #%lld: ",tt);
        cout<<ans<<endl;
    }
    return 0;
}