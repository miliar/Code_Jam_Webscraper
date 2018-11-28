#include<bits/stdc++.h>
using namespace std;
 
// Numeric Constants
#define MOD 1000000007
#define maxs 250005
#define mins 1005
#define eps 0.000000000001
#define imax 2000000200
#define llmax 1000000002000000000ll
 
// Others
#define ll long long int
#define pb push_back
#define gc getchar_unlocked
#define iosbase ios_base::sync_with_stdio(false)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ppi pair<pair<int,int>,int>
#define ppl pair<pll,ll>
#define vi vector<int>
#define sc scanf
#define pr printf
#define lld I64d
#define F first
#define S second
#define siter set<int>::iterator
#define p_pq priority_queue
#define ub upper_bound
#define lb lower_bound

vector<pair<ll,ll> > v;

// bool comp(pair<ll,ll> p1,pair<ll,ll> p2)
// {
//     if(p1.first==p2.first)
//         return p1.second>p2.second;
//     return p1.first>p2.first;
// }

int main()
{
	ll t,d,n,s,k;
    scanf("%lld",&t);
    for(ll o=1;o<=t;++o)
    {   
        v.clear();
        scanf("%lld%lld",&d,&n);
        for(ll i=0;i<n;++i)
        {
            scanf("%lld%lld",&k,&s);
            v.pb({k,s});
        }
       // cout<<d<<" "<<v[0].first<<" "<<v[0].second<<endl;
        long double ans=(d*1.0-1.0*v[0].first)/(1.0*v[0].second);
        long double tt;
        for(ll i=1;i<n;++i)
        {
            tt=(d*1.0-1.0*v[i].first)/(1.0*v[i].second);
            if(tt-ans>0.0)
            {
               // cout<<i<<endl;
                ans=tt;
            }
        }
        //cout<<ans<<endl;
        long double ss=(1.0*d)/ans;
        cout<<"Case #"<<o<<": ";
        cout.setf(ios::fixed);
        cout.setf(ios::showpoint);
        cout.precision(6);
        cout<<ss<<endl;
        // printf("Case #%lld:\n",o);
    }
	return 0;
}