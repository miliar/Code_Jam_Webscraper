#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(v) v.begin(),v.end()
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin>>t;
    ll l=0;
    while(l<t)
    {
        string s;
        ll k;
        cin>>s>>k;
        ll ans=0;
        for(ll i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                ll j=0;
                while(j<k)
                {
                    s[i+j]=(s[i+j]=='-')?'+':'-';
                    j++;
                }
                ans++;
            }
        }
//        cout<<s<<endl;
        int f=0;
        for(ll i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                f=1;
                cout<<"Case #"<<l+1<<": "<<"IMPOSSIBLE"<<endl;
                break;
            }
        }
        if(!f)
        {
            cout<<"Case #"<<l+1<<": "<<ans<<endl;
        }
        l++;
    }
    return 0;	
}

