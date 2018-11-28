#include <bits/stdc++.h>
#include <time.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> vi;
typedef pair<ll, ll> pii;
typedef vector<pii > vii;
typedef vector<vector<ll> > vvi;
typedef vector<vector<pair<ll, ll> > > vvii;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,s,e) for(ll i=(s);i<(e);++i)
#define repr(i,s,e) for(ll i=(e);i>(s);--i)

const ll MOD = 1e9+7;
const ll INF = 1e14;
const ll TE3 = 1005;
const ll TE5 = 100005;

bool PRINT_TIME_OF_EXEC = false;

ll n;

string g(string s) {
  string t(s);
  rep(i,0,s.size()) {
    t[i]='+'+'-'-s[i];
  }
  return t;
}

ll f(string x, ll k) {
  ll l=x.size();
  ll ans1=0;
  string t(l,'+');
  string s1(x);
  rep(i,0,l-k+1) {
    if(s1[i]=='-') {
      rep(j,i,i+k) {
        s1[j]='+'+'-'-s1[j];
      }
      ++ans1;
    }
  }
  ll ans2=0;
  string s2(x);
  for(ll i=l-1;i>=k-1;--i) {
    // cout<<i<<endl;
    if(s2[i]=='-') {
      for(ll j=i;j>i-k;--j) {
        s2[j]='+'+'-'-s2[j];
      }
      ++ans2;
    }
  }
  // cout<<s2<<endl;
  ll ans;
  if(s1==t && s2==t) return min(ans1,ans2);
  if(s1==t) return ans1;
  if(s2==t) return ans2;
  return -1;
}

int main() {
  ll start_time = clock();
  cin>>n;
  ll k;
  rep(i,0,n) {
    string s;
    cin>>s;
    cin>>k;
    // cout<<endl;
    ll ans=f(s,k);
    cout<<"Case #"<<i+1<<": ";
    if(ans==-1) {
      cout<<"IMPOSSIBLE"<<endl;
    } else {
      cout<<ans<<endl;
    }
  }


  ll end_time = clock();
  if(PRINT_TIME_OF_EXEC) cout<<"Time of exec. "<<((double)end_time-start_time)/CLOCKS_PER_SEC<<endl;
  return 0;
}
