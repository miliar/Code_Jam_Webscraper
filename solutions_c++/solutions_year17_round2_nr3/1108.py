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

double es[110], ss[110];
double dist[110][110];

double solve() {
  int n, q;

  cin >> n >> q;
  rep(i, n) {
    cin >> es[i] >> ss[i];
  }

  rep(i, n) {
    rep(j, n) {
      cin >> dist[i][j];
    }
  }
  assert(q == 1);
  int u0, v0;
  cin >> u0 >> v0;
  assert(u0 == 1 && v0 == n);


  vector<double> acc(n, 0.0);
  rep(i, n) {
    if(i == 0) {
      acc[i] = 0;
    } else {
      acc[i] = acc[i-1] + dist[i-1][i];
    }
  }

  vector<double> dp(n, 1e14);
  for(int i = n-1; i >= 0; --i) {
    if(i == n-1) {
      dp[i] = 0;
    } else {
      reps(j, i+1, n) {
        double d = acc[j] - acc[i];
        if(d > es[i]) break;
        double time = d / ss[i];
        dp[i] = min(dp[i], time + dp[j]);
      }
    }
  }
  return dp[0];
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    double ans = solve();
    printf("Case #%d: %.8lf\n", i, ans);
  }

  return 0;
}
