#include <cstdio>
#include <vector>
using namespace std;

char f[110][110], f_[110][110];

bool canp[110][110];
bool canx[110][110];

vector<int> con[210];
int fr[210]; bool vs[210];

bool dfs(int x){
  vs[x] = true;
  for(int nx : con[x]){
    if(fr[nx] == 0 || (!vs[fr[nx]] && dfs(fr[nx]))){
      fr[nx] = x; return true;
    }
  }
  return false;
}

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    printf("Case #%d: ", tt);

    int N, M; scanf("%d%d", &N, &M);
    for(int i = 1; i <= N; i++){
      for(int j = 1; j <= N; j++){
        f[i][j] = f_[i][j] = '.';
        canp[i][j] = canx[i][j] = true;
      }
      f[i][N + 1] = f_[i][N + 1] = 0;
    }

    for(int i = 1; i <= M; i++){
      char c; int x, y; scanf(" %c%d%d", &c, &x, &y);
      f[x][y] = f_[x][y] = c;

      if(c == '+' || c == 'o'){ // diag
        for(int k = 1; k <= N; k++){
          int l = x + y - k;
          if(l >= 1 && l <= N) canp[k][l] = false;
          l = k - x + y;
          if(l >= 1 && l <= N) canp[k][l] = false;
        }
      }
      if(c == 'x' || c == 'o'){
        for(int k = 1; k <= N; k++){
          canx[x][k] = canx[k][y] = false;
        }
      }
    }

    // bipartite matching for +
    for(int i = 1; i <= 2 * N - 1; i++){
      con[i].clear(); fr[i] = 0;
    }

    for(int i = 1; i <= N; i++){
      for(int j = 1; j <= N; j++){
        if(canp[i][j]){ // (i + j - 1, j - i + N)
          con[i + j - 1].push_back(j - i + N);
        }
      }
    }

    for(int i = 1; i <= 2 * N - 1; i++){
      for(int j = 1; j <= 2 * N - 1; j++) vs[j] = false;
      dfs(i);
    }

    for(int i = 1; i <= 2 * N - 1; i++){
      if(fr[i] != 0){
        int x = (fr[i] - i + 1 + N) / 2;
        int y = (fr[i] + i + 1 - N) / 2;

        if(f_[x][y] == '.') f_[x][y] = '+';
        if(f_[x][y] == 'x') f_[x][y] = 'o';
      }
    }

    // bipartite matching for x
    for(int i = 1; i <= N; i++){
      con[i].clear(); fr[i] = 0;
    }

    for(int i = 1; i <= N; i++){
      for(int j = 1; j <= N; j++){
        if(canx[i][j]) con[i].push_back(j);
      }
    }

    for(int i = 1; i <= N; i++){
      for(int j = 1; j <= N; j++) vs[j] = false;
      dfs(i);
    }

    for(int i = 1; i <= N; i++){
      if(fr[i] != 0){
        if(f_[fr[i]][i] == '.') f_[fr[i]][i] = 'x';
        if(f_[fr[i]][i] == '+') f_[fr[i]][i] = 'o';
      }
    }

    // calculate
    int ans = 0, cnt = 0;
    for(int i = 1; i <= N; i++){
      for(int j = 1; j <= N; j++){
        if(f_[i][j] == '+' || f_[i][j] == 'x') ans++;
        if(f_[i][j] == 'o') ans += 2;

        if(f_[i][j] != f[i][j]) cnt++;
      }
    }

    printf("%d %d\n", ans, cnt);

    for(int i = 1; i <= N; i++){
      for(int j = 1; j <= N; j++){
        if(f_[i][j] != f[i][j]) printf("%c %d %d\n", f_[i][j], i, j);
      }
    }
  }
  return 0;
}
