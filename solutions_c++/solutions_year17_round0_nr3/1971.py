#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define ff first
#define mp make_pair
#define ss second
#define mm(a,b) memset(a,b,sizeof(b))
#define pp pair<ll,ll>
#define mp make_pair
using namespace std;

pp answer(ll n)
{
    if(n%2==1)
        return mp((n-1)/2,(n-1)/2);
    return mp(n/2,(n-1)/2);
}

pp solve(ll n,ll k)
{
    map<ll,ll> a,b;
    a.clear();
    b.clear();

    a[n]=1;
    ll dn=1;

    while(1)
    {
        if(dn >= k)
        {
            ll cnt = dn/2;
            for (auto it = a.rbegin(); it != a.rend(); ++it)
            {
                cnt+=it->ss;
                if(cnt>=k)
                    return answer(it->ff);

            }
        }

        b.clear();

        for(auto it=a.begin();it!=a.end();it++)
        {
            ll vl = it->ff , cnt = it->ss;
            if(vl%2==1)
                b[(vl-1)/2]+=cnt*2;
            else
            {
                b[(vl-1)/2]+=cnt;
                b[vl/2]+=cnt;
            }
        }

        a.clear();
        a = b;
        dn = dn*2+1;
    }

}

int main()
{

    freopen("C-large.in", "r", stdin);    freopen("output.txt", "w", stdout);

    ll t;
    cin>>t;

    for(ll cs=1;cs<=t;cs++)
    {
        ll n,k;
        cin>>n>>k;
        pp ans = solve(n,k);
        cout<<"Case #"<<cs<<": "<<ans.ff<<" "<<ans.ss<<"\n";
    }


}
