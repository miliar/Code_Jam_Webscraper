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

const int oo = 1e9;

int hd, ad, hk, ak, b, d;

int memo[105][205][105][105];
bool bio[105][205][105][105];
int dp(int h, int a, int hh, int aa){
  if (aa < 0) aa = 0;
  h -= aa;
  if (hh <= 0) return 0;
  if (h <= 0) return oo;
  int &r = memo[h][a][hh][aa];
  if (bio[h][a][hh][aa]++) return r;
  r = oo;

  if (a >= hh) return r = 1;

  r = min(r, 1+dp(h , a  , hh-a, aa  ));
  r = min(r, 1+dp(h , a+b, hh  , aa  ));
  r = min(r, 1+dp(hd, a  , hh  , aa  ));
  r = min(r, 1+dp(h , a  , hh  , aa-d));

  return r;
  
}

void solve(){

  cin >> hd >> ad >> hk >> ak >> b >> d;
  memset(bio, 0, sizeof bio);
  int sol = dp(hd+ak, ad, hk, ak);
  if (sol == oo) cout << "IMPOSSIBLE" << endl;
  else cout << sol << endl;

}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
