#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 330;
const ll  MODD = 1000000007;

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<vi> vvi;
#define X first
#define Y second

class SCC {
private:
    int n, comp;
    vvi g, gt;
    vi seq, vis;
    void dfs(int u, const vvi &adj){
  for (int v : adj[u]){
            if (vis[v] == -1){
                vis[v] = comp;
                dfs(v, adj);
            }
        }
        seq.push_back(u);
    }
public:
    SCC() {}
    SCC(int _n){
        n = _n;
        g.assign(n, vi()); gt.assign(n, vi());
    }
    void add_edge(int u, int v){
        g[u].push_back(v); gt[v].push_back(u);
    }
    pair<int, vi> find_SCC(){
        vis.assign(n, -1); comp = 0;
        for (int i = 0; i < n; i++){
            if (vis[i] == -1){
                vis[i] = comp;
                dfs(i, g);
            }
        }
        vis.assign(n, -1); comp = 0;
        for (int i = n-1; i >= 0; i--){
            int u = seq[i];
            if (vis[u] == -1){
                vis[u] = comp;
                dfs(u, gt);
                comp++;
            }
        }
        return {comp, vis};
    }
};

//listings:twosat
// 2-SAT solver. Include SCC code from graph algorithms. VAR(x) is variable x,
// NOT(VAR(x)) is the negation of variable x. Complexity: O(n + m)
int VAR(int x) { return 2*x; }
int NOT(int x) { return x^1; }

struct TwoSAT {
  int n;  SCC scc;
  // Create a 2-SAT equation with n variables
  TwoSAT(int n) : n(n), scc(2 * n) { }
  set<pair<int,int> > x;
  void add_or(int u, int v) {
    if (u == NOT(v)) return;
    if(x.count(make_pair(u,v))) return;
    x.emplace(u,v);
    scc.add_edge(NOT(u), v);  scc.add_edge(NOT(v), u);
  }
  void add_true(int u){ add_or(u, u); }
  void add_false(int u) { add_or(NOT(u), NOT(u)); }
  void add_xor(int u, int v) { add_or(u, v); add_or(NOT(u), NOT(v)); }
  pair<bool, vector<bool>> solve() {
    vi comp = scc.find_SCC().Y;  vector<bool> val(n);
    for (int i = 0; i < 2 * n; i += 2){
      if (comp[i] == comp[i + 1]) return {false, val};
      val[i/2] = (comp[i] > comp[i + 1]);
    }
    return {true, val};
  }
};

int A[MAX_N];
char C[MAX_N][MAX_N];

const int di[4] = {-1,1,0,0};
const int dj[4] = {0,0,-1,1};


void do_case(){
  pair<bool,vector<bool>> s;
  int m,n; cin >> m >> n;
  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++)
      cin >> C[i][j];
  
  TwoSAT G(m*n);

  for(int i=0;i<m;i++){
    int ctr = 0;
    for(int j=0;j<n;j++){
      if(C[i][j] == '#'){ ctr = 0;  continue; }
      if(C[i][j] == '.') continue;
      ctr++;
      if(ctr == 1) continue;
      for(int k=j;k>=0;k--){
        if(C[i][k] == '#') break;
        if(C[i][k] != '.')
          G.add_true(VAR(i*n+k));
      }
    }
  }

  for(int i=0;i<n;i++){
    int ctr = 0;
    for(int j=0;j<m;j++){
      if(C[j][i] == '#') { ctr = 0; continue; }
      if(C[j][i] == '.') continue;
      ctr++;
      if(ctr == 1) continue;
        for(int k=j;k>=0;k--){
          if(C[k][i] == '#') break;
          if(C[k][i] != '.')
            G.add_false(VAR(k*n+i));
        }
      }
    }

  

  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++){
      if(C[i][j] == '.'){
        vector<pair<int,int> > guys[2];
        for(int k=0;k<4;k++){
          for(int d=1;;d++){
            int nI = i+d*di[k], nJ = j+d*dj[k];
            if(!(0 <= nI && nI < m && 0 <= nJ && nJ < n)) break;
            if(C[nI][nJ] == '#') break;
            if(C[nI][nJ] != '.')
              guys[k/2].emplace_back(nI,nJ);
          }
        }
        if(guys[0].empty() && guys[1].empty()) goto imp;
        if(guys[0].size() > 1 && guys[1].size() > 1) goto imp;
        if(guys[1].empty() && guys[0].size() > 1) goto imp;
        if(guys[0].empty() && guys[1].size() > 1) goto imp;
        if(guys[1].empty())
          G.add_true(VAR(guys[0][0].first*n+guys[0][0].second));
        else if(guys[0].empty())
          G.add_false(VAR(guys[1][0].first*n+guys[1][0].second));
        else
          G.add_or((VAR(guys[0][0].first*n+guys[0][0].second)),
            NOT(VAR(guys[1][0].first*n+guys[1][0].second)));
    }
  }

  s = G.solve();
  if(!s.first) goto imp;

  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++)
      if(C[i][j] == '|' || C[i][j] == '-')
        C[i][j] = "-|"[s.second[i*n+j]];

  cout << "POSSIBLE" << endl;
  for(int i=0;i<m;i++){
    for(int j=0;j<n;j++)
      cout << C[i][j];
    cout << endl;
  }

  return;
  imp:
  cout << "IMPOSSIBLE" << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(9);
  
  int T,C=1; cin >> T;
  
  while(T--) {
    cout << "Case #" << C++ << ": ";
    //cout << do_case() << endl;
    do_case();
  }
  
  return 0;
}
