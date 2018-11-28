#include <bits/stdc++.h>

using namespace std;

typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

const int maxc = 55;
int r,c,nl,n;
char mat[maxc][maxc];
int vist[maxc][maxc];
int d[2][4] = {{1,-1,0,0},{0,0,1,-1}};
int tx[2][4] = {{3,2,1,0},{2,3,0,1}};
vvb gd;
vii laser,cell;
vi dlas;
map<ii,int> emp,las;

int tr(int dir,char x){
  if(x == '/') return tx[0][dir];
  else if(x == '\\') return tx[1][dir];
  else return dir;
}

void dfs1(int v, vb& used, vi& order, vvi& g) {
  used[v] = true;
  for (int i = 0; i < int(g[v].size()); ++i)
    if(not used[g[v][i]]) dfs1(g[v][i],used,order,g);
  order.push_back(v);
}
void dfs2(int v, int cl, vi& comp, vvi& gt) {
  comp[v] = cl;
  for (int i = 0; i < int(gt[v].size()); ++i)
    if (comp[gt[v][i]]==-1)dfs2(gt[v][i],cl,comp,gt);
}
//g -> adjacency list, gt -> inverse of g
vi scc(vvi& g, vvi& gt) {
  int n = g.size();
  vector<bool> used(n, false);
  vector<int> order;
  for (int i = 0; i < n; ++i)
    if (not used [i]) dfs1(i, used, order, g);
  vi comp(n, -1); int cc = 0;
  for (int i = 0; i < n; ++i)
    if (comp[order[n-i-1]] == -1)
      dfs2(order[n-i-1], cc++, comp, gt);
  return comp;
}

bool checkgd(){
  for(int i = 0; i < n; ++i){
    if(!(gd[i][0] or gd[i][1])) return false;
  }
  return true;
}

int main () {
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> r >> c;
    laser = vii(0);
    cell = vii(0);
    emp.clear();
    las.clear();
    for(int i = 0; i < r; ++i){
      for(int j = 0; j < c; ++j){
        cin >> mat[i][j];
        if(mat[i][j] == '-' or mat[i][j] == '|'){
          las[ii(i,j)] = laser.size();
          laser.push_back(ii(i,j));
        }
        else if(mat[i][j] == '.'){
          emp[ii(i,j)] = cell.size();
          cell.push_back(ii(i,j));
        }
      }
    }
    nl = laser.size();
    gd = vvb(nl,vb(2,1));
    for(int i = 0; i < nl; ++i){
      for(int dir = 0; dir < 4; ++dir){
        int x = laser[i].first;
        int y = laser[i].second;
        int d1 = dir;
        while(true){
          int xx = x+d[0][d1];
          int yy = y+d[1][d1];
          if(xx < 0 or yy < 0 or xx == r or yy == c) break;
          if(mat[xx][yy] == '#') break;
          if(mat[xx][yy] == '|' or mat[xx][yy] == '-'){
            gd[i][dir/2] = 0;
            break;
          }
          int d2 = tr(d1,mat[xx][yy]);
          d1 = d2;
          x = xx;
          y = yy;
        }
      }
    }
//     cerr << "COSA " << nl << "\n";
    if(!checkgd()){
      cout << "Case #" << cass << ": IMPOSSIBLE\n";
      continue;
    }
//     cerr << "COSA " << nl << "\n";
    dlas = vi(nl,0);
    vvi cond(cell.size(),vi(laser.size(),0));
    for(int i = 0; i < nl; ++i){
      for(int dir = 0; dir < 4; ++dir){
        if(!gd[i][dir/2]){
          dlas[i] = ((dir/2)^1);
          continue;
        }
        int x = laser[i].first;
        int y = laser[i].second;
        int d1 = dir;
        while(true){
//           cerr << x << ' ' << y << '\n';
          int xx = x+d[0][d1];
          int yy = y+d[1][d1];
          if(xx < 0 or yy < 0 or xx == r or yy == c) break;
          if(mat[xx][yy] == '#') break;
          if(mat[xx][yy] == '|' or mat[xx][yy] == '-'){
            gd[i][dir/2] = 0;
            break;
          }
          if(mat[xx][yy] == '.'){
            cond[emp[ii(xx,yy)]][i] |= 2-dir/2;
//             cerr << "bien\n";
          }
          int d2 = tr(d1,mat[xx][yy]);
          d1 = d2;
          x = xx;
          y = yy;
        }
      }
    }
//     cerr << "COSA " << nl << ' ' << cell.size() << "\n";
//     for(int i = 0; i < nl; ++i){
//       for(int j = 0; j < 2; ++j){
//         if(gd[i][j]) cout << 1;
//         else cout << 0;
//       }
//       cout << '\n';
//     }
    int n = nl;
    bool bad = false;
    vvi cond2(cell.size());
    vb xxc(cell.size(),0);
    for(int i = 0; i < cell.size(); ++i){
      for(int j = 0; j < laser.size(); ++j){
//         cerr << cond[i][j] << '\n';
        if(cond[i][j]) cond2[i].push_back(2*j+cond[i][j]%2);
        if(cond[i][j] == 3) xxc[i] = true;
      }
      if(cond2[i].size() == 0){
        cout << "Case #" << cass << ": IMPOSSIBLE\n";
        bad = true;
        break;
      }
      if(xxc[i]) cond2[i] = vi(0);
    }
//     cerr << "COSA " << nl << "\n";
    if(bad) continue;
//     cerr << "COSA2 " << nl << "\n";
    vvi g(2*nl),gt(2*nl);
    for(int i = 0; i < cell.size(); ++i){
      if(cond2[i].size() == 2){
        int x = cond2[i][0];
        int y = cond2[i][1];
        g[x^1].push_back(y);
        g[y^1].push_back(x);
        gt[x].push_back(y^1);
        gt[y].push_back(x^1);
      }
      else if(cond2[i].size() == 1){
        int x = cond2[i][0];
        g[x^1].push_back(x);
        gt[x].push_back(x^1);
      }
    }
    for(int i = 0; i < nl; ++i){
      if(!gd[i][0]){
        g[2*i].push_back(2*i+1);
        gt[2*i+1].push_back(2*i);
      }
      if(!gd[i][1]){
        gt[2*i].push_back(2*i+1);
        g[2*i+1].push_back(2*i);
      }
    }
    //Make the graf, its inverse, etc
    vi comp = scc(g, gt);
    //2-SAT: X -> 2 * i, ! X -> 2 * i + 1
    for (int i = 0; i < 2 * n; i += 2)
      if (comp[i] == comp[i + 1]){
        cout << "Case #" << cass << ": IMPOSSIBLE\n";
        bad = true;
        break;
      }
    if(bad) continue;
    //Write solution
    for (int i = 0; i < 2 * n; ++i)
      if (comp[i]>comp[i^1]){
        //i is part of sol
        if(i%2) dlas[i/2] = 0;
        else dlas[i/2] = 1;
      }
    cout << "Case #" << cass << ": POSSIBLE\n";
    for(int i = 0; i < r; ++i){
      for(int j = 0; j < c; ++j){
        if(mat[i][j] == '-' or mat[i][j] == '|'){
          if(dlas[las[ii(i,j)]] == 0) cout << '-';
          else cout << '|';
        }
        else cout << mat[i][j];
      }
      cout << '\n';
    }
  }
}