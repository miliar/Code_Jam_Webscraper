/*input
1
878
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
  bio;
  freopen("B-large.in","r",stdin);
  freopen("out.txt","w",stdout);
  ll tc;
  cin>>tc;
  f(tt,1,tc+1){
    cout<<"Case #"<<tt<<": ";
    string s;
    cin>>s;
    ll n=s.size();
    ll arr[20];
    ms0(arr);
    f(i,0,n){
      arr[i]=(s[i]-'0');
    }
    rf(i,n,0){
      ll val=arr[i];
      bool fg=0;
      rf(j,i,0){
        if(arr[j]>val){
          fg=1;
          break;
        }
      }
      if(fg!=0){
        arr[i]=9;
        arr[i-1]=max(0LL,arr[i-1]-1);
        f(j,i,n){
          arr[j]=9;
        }
      }
    }
    ll ans=0;
    ll mul=1;
    rf(i,n,0){
      ans+=arr[i]*mul;
      mul*=10;
    }
    cout<<ans<<endl;
  }
  return 0;
}