/*input
3
---+-++- 3
+++++ 4
-+-+- 4
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
int main() 
{
  freopen("A-large.in","r",stdin);
  freopen("out.txt","w",stdout);
  bio;
  ll tc;
  cin>>tc;
  f(t,0,tc){
    ll cnt=0;
    string s;
    ll k;
    cin>>s>>k;
    ll n=s.size();
    f(i,0,n-k+1){
      if(s[i]=='-'){
        cnt++;
        f(j,i,i+k){
          if(s[j]=='-'){
            s[j]='+';
          }
          else{
            s[j]='-';
          }
        }
      }
    }
    bool fg=0;
    f(i,0,n){
      if(s[i]=='-'){
        fg=1;
      }
    }
    cout<<"Case #"<<t+1<<": ";
    if(fg){
      cout<<"IMPOSSIBLE"<<endl;
    }
    else{
      cout<<cnt<<endl;
    }
  }
  return 0;
}