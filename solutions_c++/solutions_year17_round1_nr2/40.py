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

class event{
public:

  int lo, hi, id;
  bool tp;

  bool operator<(event t){
    int a = tp ? hi : lo;
    int b = t.tp ? t.hi : t.lo;
    if (a != b) return a < b;
    if (tp != t.tp) return tp < t.tp;
    return false;
  }
    
};

int n, p;
int r[55];
int q[55][55];

void solve(){

  cin >> n >> p;
  REP(i,n) cin >> r[i];
  REP(i,n) REP(j,p) cin >> q[i][j];
  
  vector<event> sweep;
  REP(i,n) REP(j,p){
#define r r[i]
#define q q[i][j]
    int id = i;
    int lo = (10*q+11*r-1) / (11*r);
    int hi = (10*q) / (9*r);
#undef r
#undef q
    if (lo <= hi) sweep.pb({lo, hi, id, false}), sweep.pb({lo, hi, id, true});
  } sort(sweep.begin(), sweep.end());

  multiset<int> all[55];
  int sol = 0;
  
  for (auto e : sweep){
#define ac all[e.id]
    if (e.tp){
      bool check = true;
      while (true){
#define at all[i]
	REP(i,n) if (at.empty()) check = false;
	if (!check) break;
	REP(i,n) at.erase(at.begin());
	++sol;
#undef at
      }
      if (ac.find(e.hi) != ac.end()) ac.erase(ac.find(e.hi));
    } else {
      ac.insert(e.hi);
    }
#undef ac
  }

  cout << sol << endl;
  
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": ", solve();

  return 0;
}
