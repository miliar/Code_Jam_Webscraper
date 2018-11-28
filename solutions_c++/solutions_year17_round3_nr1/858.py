#include<bits/stdc++.h>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<double,double> P;
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
  int n, k;
  cin >> n >> k;
  vector<P> data(n);
  rep(i, n) {
    cin >> data[i].first >> data[i].second;
  }

  SORT(data);

  double ans = -1;
  reps(i, k-1, n) {
    double t = data[i].first * data[i].first;
    t += data[i].first * data[i].second * 2;
    priority_queue<double> pq;
    rep(j, i) {
      pq.push(data[j].first * data[j].second * 2);
    }
    rep(j, k-1) {
      t += pq.top();
      pq.pop();
    }
    ans = max(ans, t);
  }
  //cerr<<ans<<endl;
  return ans * M_PI;
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    double ans = solve();
    printf("Case #%d: %.9lf\n", i, ans);
  }

  return 0;
}
