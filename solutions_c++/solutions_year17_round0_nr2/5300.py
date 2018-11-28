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

ll nod(ll number)
{
    ll digits = 0;
    if (number < 0) digits = 1; // remove this line if '-' counts as a digit
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}

ll g(ll x) {
  stringstream ss;
  string s(x,'9');
  ss<<s;
  ll y;
  ss>>y;
  return y;
}

// ll f(ll x) {
//   stringstream ss;
//   ss<<x;
//   string s;
//   ss>>s;
//   ll l=s.size();
//   string t;
//   rep(i,0,l) {
//
//   }
// }

string f(string y) {
  // ll y=0;
  // string y;
  // stringstream ss;
  // ss<<x;
  // ss>>y;
  string z(y);
  ll l=y.size();
  for(ll i=l-1;i>0;--i) {
    if(z[i]<z[i-1]) {
      z[i-1]=z[i-1]-1;
      for(ll j=i;j<l;++j) z[j]='9';
    }
  }
  ll zz=z.size();
  ll i;
  for(i=0;i<zz;++i) {
    if(z[i]!='0') break;
  }
  return z.substr(i,zz-i);
}

int main() {
  ll start_time = clock();

  ll n;
  cin>>n;
  rep(i,0,n) {
    string x;
    cin>>x;
    cout<<"Case #"<<i+1<<": "<<f(x)<<endl;
  }

  ll end_time = clock();
  if(PRINT_TIME_OF_EXEC) cout<<"Time of exec. "<<((double)end_time-start_time)/CLOCKS_PER_SEC<<endl;
  return 0;
}
