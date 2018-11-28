#include<bits/stdc++.h>
#define pb   push_back
using namespace std;
typedef long long ll;
typedef long double ld;

string g[55];
int r, c;

bool db = 0;
const int N = 5555;
int low[N],vis[N],scomp[N],scompNum,I;
vector<int> adj[N]; stack<int> verts;
void scc(int u) { low[u] = vis[u] = ++I; verts.push(u);
  for (int v : adj[u]) {
    if (!vis[v]) scc(v);
    if (scomp[v] == -1) low[u] = min(low[u], low[v]); }
  if (vis[u] <= low[u]) { int v;
    do { v=verts.top(); verts.pop(); scomp[v]=scompNum; } while (v != u);
    ++scompNum; }}
void get_scc(int n) { memset(vis,0,sizeof vis); memset(scomp,-1,sizeof scomp);
  scompNum=I=0; for (int i=0; i<n; ++i) if (!vis[i]) scc(i); }
////////////////////////////////////////////////////////////////////////////////
// 2-SAT using SCC (previous version was TESTED F - SouthAmerica03)
////////////////////////////////////////////////////////////////////////////////
bool truth[N/2]; // N must be at least 2 times the number of variables
// the clause a || b becomes !a => b and !b => a in the implication graph
void add_clause(int a, int b) { adj[a^1].push_back(b); adj[b^1].push_back(a);
if (db) cout<< "Added edge " << a << " " << b <<endl;}
bool two_sat(int n) { get_scc(n);
  memset(low,0,sizeof low);
  for (int i = 0; i < n; i += 2) { if (scomp[i] == scomp[i^1]) return false;
  	truth[i/2] = (scomp[i] < scomp[i^1]); } return true; }

int adj2[55][55][2];

//1 for xy is y, 0 is x
int dfs(int x,int y, int dir, int xy, int t, int mark = 0){
  if (db)cout <<t << " " << x <<" "<< y << " " << dir << " " << xy << " " << g[max(x,0)][max(0,y)]<< (int) g[max(x,0)][max(0,y)] <<endl;
  if (x>=r||x<0||y>=c||y<0) return 1;
  if (g[x][y]=='#') return 1;
  if (g[x][y]=='/') xy=!xy, dir = -dir;
  if (g[x][y]=='\\') xy=!xy;
  if (g[x][y]=='-'|| g[x][y] == '|') return 0;
  if (g[x][y]=='.' && mark){ adj2[x][y][xy]=t; }
  if (!xy) return dfs(x+dir, y, dir, xy, t, mark);
  return dfs(x, y+dir, dir, xy, t, mark);
}


int main(){
  ios_base::sync_with_stdio(false);cin.tie(0);
  int T;
  cin >> T;
  for(int it=0;it<T;it++){
    cin >> r >> c;
    memset(adj2,-1,sizeof adj2);
    for(int i=0;i<r;i++){
      cin >> g[i];
    }
    for(int i=0;i<r*c;i++){
      adj[i].clear();
    }
    int t=0;
    bool pos = true;
    for(int x=0;x<r;x++){
      for(int y=0;y<c;y++){
        if (g[x][y]=='-'|| g[x][y]=='|'){
          if (db) cout << "@ " << t <<endl;
          bool either = false;
          if (dfs(x-1,y,-1, 0,t) && dfs(x+1,y,1,0,t)){
            dfs(x-1,y,-1, 0,t,1) && dfs(x+1,y,1,0,t,1);
            either = true;
          }
          else {
            add_clause(2*t+1,2*t+1);
          }
          if (dfs(x,y-1,-1, 1,t) && dfs(x,y+1,1,1,t)){
            dfs(x,y-1,-1, 1,t,1) && dfs(x,y+1,1,1,t,1);
            either = true;
          }
          else {
            add_clause(2*t,2*t);
          }
          if (!either) {
            pos = false;
            if (db)cout << t << " has failed"<<endl;
          }
          t++;
        }
      }
    }
    if (pos){
      for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
          if (g[i][j]=='.'){
            int a =adj2[i][j][0];
            int b =adj2[i][j][1];
            if (adj2[i][j][0]==-1 && adj2[i][j][1]==-1){
              pos = false;
              if (db)cout << i << " " << j << " is empty" <<endl;
              break;
            }
            else if (a==-1){
              add_clause(2*b+1,2*b+1);
            }
            else if (b==-1){
              add_clause(2*a,2*a);
            }
            else {
              add_clause(2*a,2*b+1);
            }
          }
        }
      }
      if (!two_sat(2*t)) pos = false;
      else if (pos){
        int tt=0;
        for(int i=0;i<r;i++){
          for(int j=0;j<c;j++){
            if (g[i][j]=='-' || g[i][j]=='|'){
              if (db) cout << truth[tt] <<endl;
              if (truth[tt]) g[i][j] = '|';
              else g[i][j] = '-';
              tt++;
            }
          }
        }
      }
    }
    string ans;
    if (!pos){
      ans ="IMPOSSIBLE";
      cout <<"Case #" <<it+1 <<": " << ans <<endl;
    }
    else {
      ans ="POSSIBLE";
      cout <<"Case #" <<it+1 <<": " << ans <<endl;
      for(int i=0;i<r;i++) cout << g[i] << endl;
    }
  }
}
