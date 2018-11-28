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
ll n,m;
string solve(string s, int k) {
  int n = s.size();
  int ans = 0;
  for(int i = 0; i + k <= n; i++) {
    if (s[i] == '-') {
      ans += 1;
      for(int j = i; j < i + k; ++j) {
        s[j] = (s[j] == '+') ? '-' : '+';
      }
    }
  }

  for(int i = 0; i < n; i++) {
    if (s[i] != '+') {
      return "IMPOSSIBLE";
    }
  }
  return toString(ans);
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    string s;
    int k;
    cin >> s >> k;
    string ans = solve(s, k);
    printf("Case #%d: %s\n", i, ans.c_str());
  }

  return 0;
}
