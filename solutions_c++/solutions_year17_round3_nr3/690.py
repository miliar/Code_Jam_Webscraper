#include<bits/stdc++.h>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<ll,ll> P;
const int INF=INT_MAX / 3;
const ll LINF=LLONG_MAX / 3LL;
#define CONST 1000000007
#define EPS (1e-8)
#define PB push_back
#define MP make_pair
#define sz(a) ((int)(a).size())
#define reps(i,n,m) for(int i=(n);i<int(m);i++)
#define rep(i,n) reps(i,0,n)
#define SORT(a) sort((a).begin(),(a).end())
ll mod(ll a,ll m){return (a%m+m)%m;}
int dx[9]={0,1,0,-1,1,1,-1,-1,0},dy[9]={1,0,-1,0,1,-1,1,-1,0};


long double solve() {
  int n, k;
  cin >> n >> k;
  long double u;
  cin >> u;
  vector<long double> ps(n);
  long double dsum = 0;
  rep(i, n) {
    cin >> ps[i];
    dsum += 1.0 - ps[i];
  }
  if(dsum <= u) return 1;
  if(n != k) return 0;
  SORT(ps);
  while(u > 1e-10 && ps[0] < 1.0) {
    int cnt = 0;
    rep(i, n) {
      if(ps[0] == ps[i]) cnt++;
    }
    if(cnt == n) {
      long double du = u / n;
      long double v = min((long double)1.0, ps[0] + du);
      rep(i, n) {
        ps[i] = v;
      }
      u = 0;
    } else {
      long double t = ps[cnt];
      long double pls = t - ps[0];
      if(pls * cnt > u) {
        pls = u / cnt;
      }
      long double v = min((long double)1.0, ps[0] + pls);
      rep(i, cnt) {
        ps[i] = v;
      }
      u -= pls * cnt;
    }
  }
  long double ans = 1.0;
  rep(i, n) {
    ans *= ps[i];
  }
  return ans;
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    long double ans = solve();
    printf("Case #%d: %.10Lf\n", i, ans);
  }

  return 0;
}
