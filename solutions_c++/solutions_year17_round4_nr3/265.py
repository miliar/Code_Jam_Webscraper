#include <cstdio>
#include <vector>
#include <stack>
using namespace std;

char s[6][60];
int id[6][60];

// 1 ~ cnt : 가로
// cnt + 1 ~ 2 * cnt : 세로
vector<int> con[510];

stack<int> st; int vc, sc;
int idx[510], low[510];
bool ins[510]; int sid[510];

void dfs(int v){
  idx[v] = low[v] = ++vc;
  st.push(v); ins[v] = true;

  for(int w : con[v]){
    if(idx[w] == 0){ dfs(w); low[v] = min(low[v], low[w]); }
    else if(ins[w]) low[v] = min(low[v], idx[w]);
  }

  if(low[v] == idx[v]){
    sc++;
    for(;;){
      int w = st.top(); st.pop(); ins[w] = false;
      sid[w] = sc; if(w == v) break;
    }
  }
}

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    printf("Case #%d: ", tt);

    int R, C; scanf("%d%d", &R, &C);
    for(int i = 1; i <= R; i++){
      for(int j = 1; j <= C; j++) id[i][j] = 0;
    }

    int cnt = 0;

    for(int i = 1; i <= R; i++){
      scanf("%s", s[i] + 1);
      for(int j = 1; j <= C; j++){
        if(s[i][j] == '-' || s[i][j] == '|') id[i][j] = ++cnt;
      }
    }

    vc = 0; sc = 0;
    for(int i = 1; i <= 2 * cnt; i++){
      con[i].clear();
      idx[i] = 0; low[i] = 0; ins[i] = false; sid[i] = 0;
    }

    bool val = true;

    for(int i = 1; val && i <= R; i++){
      for(int j = 1; val && j <= C; j++){
        if(s[i][j] == '#') continue;

        if(s[i][j] == '.'){
          int horid = 0, verid = 0;

          for(int x = j + 1; x <= C; x++){
            if(s[i][x] == '#') break;
            if(s[i][x] == '-' || s[i][x] == '|'){ horid = id[i][x]; break; }
          }
          for(int x = j - 1; x >= 1; x--){
            if(s[i][x] == '#') break;
            if(s[i][x] == '-' || s[i][x] == '|'){ horid = id[i][x]; break; }
          }

          for(int x = i + 1; x <= R; x++){
            if(s[x][j] == '#') break;
            if(s[x][j] == '-' || s[x][j] == '|'){ verid = id[x][j]; break; }
          }
          for(int x = i - 1; x >= 1; x--){
            if(s[x][j] == '#') break;
            if(s[x][j] == '-' || s[x][j] == '|'){ verid = id[x][j]; break; }
          }

          if(horid == 0 && verid == 0){ val = false; continue; }
          if(horid == 0){
            // verid : always ver
            con[verid].push_back(verid + cnt);
          }
          else if(verid == 0){
            // horid : always hor
            con[horid + cnt].push_back(horid);
          }
          else{
            // verid = ver or horid = hor
            con[horid + cnt].push_back(verid + cnt);
            con[verid].push_back(horid);
          }

          continue;
        }

        bool ver = true, hor = true;
        for(int x = j + 1; x <= C; x++){
          if(s[i][x] == '#') break;
          if(s[i][x] == '-' || s[i][x] == '|'){ hor = false; break; }
        }
        for(int x = j - 1; x >= 1; x--){
          if(s[i][x] == '#') break;
          if(s[i][x] == '-' || s[i][x] == '|'){ hor = false; break; }
        }

        for(int x = i + 1; x <= R; x++){
          if(s[x][j] == '#') break;
          if(s[x][j] == '-' || s[x][j] == '|'){ ver = false; break; }
        }
        for(int x = i - 1; x >= 1; x--){
          if(s[x][j] == '#') break;
          if(s[x][j] == '-' || s[x][j] == '|'){ ver = false; break; }
        }

        if(!hor && !ver){ val = false; continue; }
        if(!hor){ // always ver
          con[id[i][j]].push_back(id[i][j] + cnt);
        }
        else if(!ver){ // always hor
          con[id[i][j] + cnt].push_back(id[i][j]);
        }
      }
    }

    if(!val){ puts("IMPOSSIBLE"); continue; }

    for(int i = 1; i <= 2 * cnt; i++) if(idx[i] == 0) dfs(i);

    bool ans = true;

    for(int i = 1; ans && i <= cnt; i++){
      if(sid[i] == sid[i + cnt]) ans = false;
    }

    puts(ans ? "POSSIBLE" : "IMPOSSIBLE");

    if(ans){
      for(int i = 1; i <= R; i++){
        for(int j = 1; j <= C; j++){
          if(s[i][j] == '#' || s[i][j] == '.'){ putchar(s[i][j]); continue; }
          putchar(sid[id[i][j]] < sid[id[i][j] + cnt] ? '-' : '|');
        }
        printf("\n");
      }
    }
  }
  return 0;
}
