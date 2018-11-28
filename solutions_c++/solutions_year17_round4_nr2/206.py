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

ostream& operator<<(ostream& out, pii p){
  return out << p.x << " " << p.y;
}

int n, c, m;
pii in[1005];
vector<int> buyer[1005];
vector<int> pos[1005];

bool check(int num){
  REP(i,c) if (num < (int)buyer[i].size()) return false;
  int sum = 0;
  REP(i,n){
    sum += (int)pos[i].size();
    if (sum > num*(i+1)) return false;
  } return true;
}

pii solve(){
  cin >> n >> c >> m;
  REP(i,m) cin >> in[i].x >> in[i].y, --in[i].x, --in[i].y;
  REP(i,c) buyer[i].clear();
  REP(i,m) buyer[in[i].y].pb(in[i].x);
  REP(i,n) pos[i].clear();
  REP(i,m) pos[in[i].x].pb(in[i].y);

  int num = 1;
  while (!check(num)) ++num;
  
  int num2 = 0;
  REP(i,n) if ((int)pos[i].size() > num) num2 += (int)pos[i].size()-num;
  return {num, num2};
}

int main(){
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": " << solve() << endl;

  return 0;
}
