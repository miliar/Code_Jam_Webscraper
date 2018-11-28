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

int n, p;
int g[105];

map<vector<int>, int> M;

int dp(vector<int> cnt){
  if (M.count(cnt)) return M[cnt];

  for (auto t : cnt) if (t < 0) return -1e9;

  bool check = true;
  for (auto t : cnt) if (t) check = false;
  if (check) return 0;

  int &r = M[cnt] = 1;

  if (p == 2){
    int a = cnt[1];
    if (a >= 2) r = max(r, 1+dp({0, a-2}));
  }

  if (p == 3){
    int a = cnt[1];
    int b = cnt[2];
    if (a && b) r = max(r, 1+dp({0, a-1, b-1}));
    if (a >= 3) r = max(r, 1+dp({0, a-3, b}));
    if (b >= 3) r = max(r, 1+dp({0, a, b-3}));
  }

  if (p == 4){
    int a = cnt[1];
    int b = cnt[2];
    int c = cnt[3];
    if (a >= 4) r = max(r, 1+dp({0, a-4, b, c}));
    if (c >= 4) r = max(r, 1+dp({0, a, b, c-4}));
    if (b >= 2) r = max(r, 1+dp({0, a, b-2, c}));
    if (a >= 2 && b) r = max(r, 1+dp({0, a-2, b-1, c}));
    if (c >= 2 && b) r = max(r, 1+dp({0, a, b-1, c-2}));
    if (a && c) r = max(r, 1+dp({0, a-1, b, c-1}));
  }

  return r;
}

int solve(){
  cin >> n >> p;
  REP(i,n) cin >> g[i];

  vector<int> cnt(p, 0);
  REP(i,n) ++cnt[g[i]%p];
  int sol = cnt[0]; cnt[0] = 0;
  M.clear();
  return sol + dp(cnt);
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": " << solve() << endl;

  return 0;
}
