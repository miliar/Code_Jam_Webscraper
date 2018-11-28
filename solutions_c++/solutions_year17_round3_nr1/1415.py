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
vector<pair<ll,ll> > a;
long double pi=3.141592653589793;

bool comp(pair<ll,ll> p1,pair<ll,ll> p2)
{
  return (p1.first)*(p1.second)>(p2.first)*(p2.second);
}

int main()
{
  ll t,n,r,h,k;
  scanf("%lld",&t);
  for(ll o=1;o<=t;++o)
  {   
    v.clear();
    scanf("%lld%lld",&n,&k);
    for(ll i=0;i<n;++i)
    {
      scanf("%lld%lld",&r,&h);
      v.pb({r,h});
    }
    long double ans=0.0;
    for(ll i=0;i<n;++i)
    {
      a.clear();
      for(ll j=0;j<n;++j)
      {
        if(i==j)
          continue;
        if((v[j].first)<=(v[i].first))
          a.pb(v[j]);
      }
      if(a.size()>=(k-1))
      {
        long double cnt=0.0;
        sort(a.begin(),a.end(),comp);
        for(ll j=0;j<k-1;++j)
        {
          cnt=cnt+2.0*pi*a[j].first*a[j].second;
        }
        cnt=cnt+2.0*pi*v[i].first*v[i].second+pi*v[i].first*v[i].first;
        if(cnt-ans>0.0)
          ans=cnt;
      }
    }
    cout<<"Case #"<<o<<": ";
    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout.precision(9);
    cout<<ans<<endl;
  }
  return 0;
}