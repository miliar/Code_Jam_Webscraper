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

ll solve(ll x) {
  while(x) {
    string s = toString(x);
    string t = s;
    SORT(t);

    if(s == t) return x;
    --x;
  }
  return -1;
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    ll x;
    cin >> x;
    int ans = solve(x);
    printf("Case #%d: %d\n", i, ans);
  }

  return 0;
}
