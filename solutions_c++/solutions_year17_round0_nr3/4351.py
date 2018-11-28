/*input
1
2 1
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
priority_queue<ll,vll>pq;
int main() 
{
  freopen("C-small-2-attempt0.in","r",stdin);
  freopen("out.txt","w",stdout);
  bio;
  ll tc;
  cin>>tc;
  f(tt,1,tc+1)
  {
    cout<<"Case #"<<tt<<": ";
    while(!pq.empty()){
      pq.pop();
    }
    ll n,k;
    cin>>n>>k;
    pq.push(n);

    ll a1,a2;
    f(i,0,k){
      ll a=pq.top();
      pq.pop();
      a1=a/2;
      a2=(a-1)/2;
      pq.push(a1);
      pq.push(a2);
    }
    cout<<a1<<" "<<a2<<endl;
  }
  return 0;
}