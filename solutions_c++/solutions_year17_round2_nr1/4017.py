#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
typedef long long ll;
bool cmp(pair<ll,ll> p1,pair<ll,ll> p2)
{
    return p1.first<p2.first;
}
int main()
{
    int t;
    cin>>t;
    for(int u=1;u<=t;u++)
    {
        ll d,n;
        cin>>d>>n;
        vector<pair<ll,ll> > v;
        for(int i=0;i<n;i++)
        {
            ll k,s;
            cin>>k>>s;
            v.pb(mp(k,s));
        }
        sort(v.begin(),v.end(),cmp);
        int maxi=n-1;
        for(int i=n-1;i>0;i--)
        {
            if(v[i-1].second>v[i].second)
            {
                double t=(double)(v[i].first-v[i-1].first)/(double)(v[i-1].second-v[i].second);
                double d2=v[i-1].first+ t*v[i-1].second;
                if(d2<=d)
                {
                   maxi=i;
                }
                else
                {
                    maxi=i-1;
                }
            }
            else
            {
                maxi=i-1;
            }

        }
        double ans=0.0;
        ans=(double)(d*v[maxi].second)/(double)(d-v[maxi].first);
        cout<<"Case #"<<u<<": "<<fixed<<setprecision(10)<<ans<<endl;
    }
  return 0;
}
