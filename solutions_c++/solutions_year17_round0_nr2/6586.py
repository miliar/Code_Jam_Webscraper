//Archit Rai
#include<bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define TR(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define TR(...)
#endif

typedef long long int ll;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a.size())
#define all(c) (c).begin(),(c).end()
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define REP(i,a,b) for(ll i=a;i<b;i++)
#define EPS 1e-12
#define MOD 1000000007
#define endl '\n'
#define PIN(n) printf("%d\n",n)
#define PLLN(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
#define N 200010

inline ll mult(ll a, ll b) { ll x = a; x *= ll(b); if(x >= MOD) x %= MOD; return x; }
inline ll add(ll a , ll b) { return a + b >= MOD ? a + b - MOD : a + b; }
ll powmod(ll a,ll b) { if(b==0)return 1; ll x=powmod(a,b/2); ll y=(x*x)%MOD; if(b%2) return (a*y)%MOD; return y%MOD; }
#define INF ll(1e18)
//Template ends here
int main()
{
  int tc;
  si(tc);
  REP(tt,1,tc+1)
  {
    ll n;
    sll(n);
    ll temp = n;
    vector<int> v;
    int cnt = 0;
    while(temp)
    {
      cnt++;
      v.push_back(temp%10);
      temp/=10LL;
    }
    reverse(all(v));
    ll val = 0;
    for(int i=0;i<cnt-1;i++)
      val = val*10LL + 9LL;
    int ind = -1;
    for(int i=1;i<sz(v);i++)
      if(v[i]<v[i-1])
      {
        ind = i;
        break;
      }
    if(ind==-1)
      val = n;
    ll val2 = 0;
    if(ind!=-1)
    {
      ll tmp = v[ind-1];
      ll ind2=ind-2;
      while(ind2!=-1 && v[ind2]==tmp)
        ind2--;
      ind2++;
      v[ind2]--;
      for(int i=ind2+1;i<sz(v);i++)
        v[i] = 9;
      for(int i=0;i<sz(v);i++)
        val2 = val2*10LL + v[i];
      if(v[0]!=0)
        val = max(val,val2);
    }
    printf("Case #%lld: ",tt);
    PLLN(val);
  }
  return 0;
}
