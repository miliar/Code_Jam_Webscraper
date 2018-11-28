#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define x first
#define y second

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

void solve(){
  ll x;
  cin >> x;
  ll sol = 0;
  int curr = 0;
  for (int i = 17; i >= 0; --i){
    ll tmp = 0;
    REP(j,i+1) tmp = 10*tmp+1;
    while (curr < 9 && sol + (curr+1) * tmp <= x) ++curr;
    sol += curr * (tmp - tmp/10);
  } assert(sol <= x); cout << sol << endl;
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
