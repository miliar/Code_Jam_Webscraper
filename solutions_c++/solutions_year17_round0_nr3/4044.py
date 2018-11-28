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

P split(ll n) {
  if(n % 2 == 0) {
    return P(n/2, n/2 + - 1);
  }
  return P(n/2, n/2);
}

P solve(const ll n, const ll k) {
  ll t = 0;
  priority_queue<ll> pq;
  map<ll, ll> mp;
  mp[n] = 1;
  pq.push(n);

  while(!pq.empty()) {
    ll r = pq.top();
    pq.pop();
    ll cnt = mp[r];
    if(cnt == 0) continue;
    mp[r] = 0;
    P p = split(r);
    if(k <= t + cnt) {
      return p;
    }
    t += cnt;
    if(p.first != 0) {
      mp[p.first] += cnt;
      pq.push(p.first);
    }

    if(p.second != 0) {
      mp[p.second] += cnt;
      pq.push(p.second);
    }

  }
}

int main(){
  ll T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    ll n, k;
    cin >> n >> k;
    P ans = solve(n, k);
    printf("Case #%d: %lld %lld\n", i, ans.first, ans.second);
  }

  return 0;
}
