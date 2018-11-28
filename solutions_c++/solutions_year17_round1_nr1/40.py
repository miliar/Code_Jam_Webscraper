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

int r, c;
string mat[55];
string out[55];

void solve(){

  cin >> r >> c;
  REP(i,r) cin >> mat[i];

  REP(i,r){
    out[i].clear();
    bool check = false;
    for (auto a : mat[i]) if (a != '?') check = true;
    if (!check) continue;
    char prev = '?';
    out[i] = mat[i];
    for (auto &a : out[i]) if (a != '?') prev = a; else a = prev;
    reverse(out[i].begin(), out[i].end()); prev = '?';
    for (auto &a : out[i]) if (a != '?') prev = a; else a = prev;
    reverse(out[i].begin(), out[i].end());
  }

  string prev = "";
  REP(i,r) if (out[i] != "") prev = out[i]; else out[i] = prev;
  reverse(out, out+r); prev = "";
  REP(i,r) if (out[i] != "") prev = out[i]; else out[i] = prev;
  reverse(out, out+r); prev = "";

  REP(i,r) cout << out[i] << endl;
  
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": " << endl, solve();

  return 0;
}
