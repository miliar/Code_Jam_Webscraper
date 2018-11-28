/*input
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
*/
#include <bits/stdc++.h>
using namespace std;
#define ll long long
//loops
#define f(i,s,n) for(ll i=(ll)s;i<(ll)n;i++)
#define rf(i,n,s) for(ll i=(ll)(n-1);i>=(ll)s;i--)
//reset
#define ms0(X) memset((X), 0, sizeof((X)))
#define ms1(X) memset((X), -1, sizeof((X)))
//IO
#define bio ios_base::sync_with_stdio;cin.tie(NULL)
//STL
#define pb push_back
#define pii pair<ll,ll>
#define vll vector<ll>
#define vpii vector<pii >
#define mll map<ll, ll>
#define mpii map<pii,ll> 
#define msll map<string, ll> 
#define sortv(v) sort(v.begin(),v.end())
#define F first
#define S second
//standard values
#define mod (ll)(1e9+7)
#define INF (ll)1e16
#define MAXN (ll)(1e5+5)
//comparator
bool cmp(pii a,pii b){
  if(a.F==b.F) return a.S<b.S;
  else return a.F<b.F;
}
ll exp(ll a,ll b){ll ans=1;while(b!=0){if(b%2==1)ans=ans*a;a=a*a;b/=2;}return ans;}
/********************************************************************************************************/
pii arr[MAXN];
int main() 
{
  freopen("A-large (1).in","r",stdin);
  freopen("ans.txt","w",stdout);
  ll tc;
  cin>>tc;
  ll tt=0;
  while(tc--){
    tt++;
    cout<<"Case #"<<tt<<": ";
    ll d,n;

    cin>>d>>n;
    f(i,0,n){
      cin>>arr[i].F>>arr[i].S;
    }
    sort(arr,arr+n);
    double maxt=0;
    ll id;
    rf(i,n,0){
      double t=double(d-arr[i].F)/(arr[i].S);
      if(t>=maxt){
        maxt=t;
        id=i;
      }
    }
    double ans=double(d)/(maxt);

    printf("%.15lf\n",ans);
  }
  return 0;
}