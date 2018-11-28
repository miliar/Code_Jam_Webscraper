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
  string s;
  int k;
  cin >> s >> k;
  int cnt = 0;
  REP(i,s.size()) if (s[i] == '-'){
    if (i+k > (int)s.size()){cout << "IMPOSSIBLE" << endl; return;}
    ++cnt;
    REP(j,k) s[i+j] ^= '-'^'+';
  } cout << cnt << endl;
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
