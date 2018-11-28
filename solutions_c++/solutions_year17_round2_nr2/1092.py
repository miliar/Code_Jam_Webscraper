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

string solve() {
  const string col("ROYGBV");
  int arr[6];
  int n;
  cin >> n;
  rep(i, 6) {
    cin >> arr[i];
  }
  assert(arr[1] +  arr[3] + arr[5] == 0);

  string s = "";
  int prev = -1;
  rep(i, n) {
    int v = 0;
    int mxi = -1;
    rep(i, 6) {
      if (i != prev && v < arr[i]) {
        mxi = i;
        v = arr[i];
      } else if(i != prev && v == arr[i] && sz(s) != 0 && s[0] == col[i]) {
        mxi = i;
      }
    }
    if(mxi == -1) return "IMPOSSIBLE";
    s += col[mxi];
    arr[mxi] -= 1;
    prev = mxi;
  }
  if(s[0] != s[n-1]) return s;
  return "IMPOSSIBLE";
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    string ans = solve();
    printf("Case #%d: %s\n", i, ans.c_str());
  }

  return 0;
}
