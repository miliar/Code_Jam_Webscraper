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

//Template ends here
int main()
{
  int tc;
  cin>>tc;
  REP(tt,1,tc+1)
  {
    string s;
    int k;
    cin>>s;
    cin>>k;
    int ans = 0;
    for(int i=0;i<s.size()-k+1;i++)
    {
      if(s[i]=='+')
        continue;
      for(int j=i;j<i+k;j++)
      {
        if(s[j]=='+')
          s[j]='-';
        else
          s[j]='+';
      }
      ans++;
    }
    bool f = false;
    for(int i=0;i<sz(s);i++)
      if(s[i]=='-')
        f=true;
    cout<<"Case #"<<tt<<": ";
    if(f)
      cout<<"IMPOSSIBLE\n";
    else
      cout<<ans<<"\n";
  }
  return 0;
}
