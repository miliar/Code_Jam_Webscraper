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

double solve() {
  int n;
  double d;
  double time = 0;
  cin >> d >> n;
  rep(i, n) {
    double x, y;
    cin >> x >> y;
    time = max(time, (d - x) / y);
  }
  return d / time;
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
