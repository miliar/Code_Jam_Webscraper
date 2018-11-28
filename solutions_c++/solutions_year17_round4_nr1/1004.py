#include <bits/stdc++.h>
#define FOR(x,n) for(int x = 0; x < n; x++)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
#define FIN ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;
typedef long long ll;


const int MXN = 101, MXP = 5;
int N, P, G[MXN], Gmod[MXN], modsG[MXP], modsL[MXP];
int ans[MXN];
map< vector<int>, int > m;

int solve(vector<int> &a, int p){
  if(m.count(a)) return m[a];
  m[a] = a.back() == 0;
  int tmp = a.back() == 0;
  for(int x = 0; x < p; x++){
    if(a[2*x]){
      vector<int> b = a;
      b[2*x]--;
      b[SZ(b)-1] = (p - (p - a.back() + x)%p)%p;
      tmp = max(tmp, (a.back() == 0) + solve(b, p));
    }

    if(a[2*x+1]){
      vector<int> b = a;
      b[2*x+1]--;
      if(a.back() > x)
        b[SZ(b)-1] = a.back() - x;
      else
        b[SZ(b)-1] = (p-(x - a.back()))%p;
      tmp = max(tmp, (a.back() == 0) + solve(b, p));
    }
  }

  return m[a] = tmp;
}


int main() { FIN;
  int T; cin >> T;

  vector< pair< vector<int>, int> > input[MXP] = {};

  for(int cases = 1; cases <= T; cases++){
    int n, p; cin >> n >> p;
    pair< vector<int>, int> tmpP = {};
    tmpP.second = cases;

    FOR(x,n) {
      int tmp; cin >> tmp;
      tmpP.first.push_back(tmp);
    }

    input[p].push_back(tmpP);
  }

  for(int x = 0; x < MXP; x++){
    for(auto i : input[x]){
      memset(modsL, 0, sizeof(modsL));
      memset(modsG, 0, sizeof(modsG));
      FOR(y,SZ(i.first)){
        if(i.first[y] < x)
          modsL[i.first[y]%x]++;
        else
          modsG[i.first[y]%x]++;
      }
      vector<int> start, end;
      FOR(y,x)
       start.push_back(modsG[y]), start.push_back(modsL[y]), end.push_back(0), end.push_back(0);
      start.push_back(0);
      end.push_back(0);
      m[end] = 0;
      ans[i.second] = solve(start, x);
    }
    m.clear();
  }

  for(int cases = 1; cases <= T; cases++){
    cout << "Case #" << cases << ": ";
    cout << ans[cases] << "\n"; 
  }
}
