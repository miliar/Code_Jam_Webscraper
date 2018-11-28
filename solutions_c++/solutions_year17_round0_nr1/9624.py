#include <bits/stdc++.h>

#define ff first
#define ss second

using namespace std;

using ll = long long;
using pll = pair<long long, long long>;

inline ll man(string &v, ll k)
{
    ll n=v.size(), odp=0, doteraz = 0;
    bool ocak;
    
    vector<bool>vstup(n), ot(n, false);
    
    for(ll i=0;i<n;++i)
    {
        if(v[i]=='+')vstup[i]=true;
        else vstup[i] = false;
    }
    
    for(ll i=0;i<n-k+1;++i)
    {
        ocak=true;
        if( (doteraz%2) != 0)ocak=false;
        if(ocak != vstup[i])
        {
            odp++;
            ot[i]=true;
            doteraz++;
        }
        if( (i-k+1) >= 0 && ot[i-k+1])doteraz--;
    }
    
    for(ll i=n-k+1;i<n;++i)
    {
        ocak = true;
        if( (doteraz%2) != 0)ocak=false;
        if(ocak != vstup[i])
        {
            return (ll)-1;
        }  
        if( (i-k+1)>=0 && ot[i-k+1])doteraz--;
    }
    
    return odp;
}

int main()
{
    ios_base::sync_with_stdio(false);
    string vstup;
    ll t, k, pom;
    cin >> t;
    
    for(ll f=0;f<t;++f)
    {
        cin >> vstup >> k;
        pom = man(vstup, k);
        cout<<"Case #"<<f+1<<": ";
        if(pom == -1)cout<<"IMPOSSIBLE\n";
        else cout<<pom<<"\n";
    }
    return 0;
}