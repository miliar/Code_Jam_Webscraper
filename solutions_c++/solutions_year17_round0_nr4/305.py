#include <bits/stdc++.h>
#define FOR(x,n) for(int x = 0; x < n; x++)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
#define CLR(a) memset((a), 0, sizeof(a))
#define SET(a) memset((a), -1, sizeof(a))
#define pb push_back
using namespace std;
typedef vector< vector<int> > vvi;

const int PLUS = 1, CROSS = 2, CIRCLE = 3, NONE = 0; 

const int MXN = 101, MXV = 4 * MXN;
vector<int> edges[MXV] = {};
int match[MXV], visited[MXV];
int Lsize, ANS[MXN][MXN], INPUT[MXN][MXN];

bool rows[MXN], cols[MXN], digsub[2*MXN], digsum[2*MXN];

int augmenting_path(int u)
{
  if(visited[u])
    return 0;
  visited[u] = true;
  for(int v : edges[u])
    if(match[v] == -1 || augmenting_path(match[v])){
      match[v] = u; return 1;
    }
  return 0;
}

int get_mcbm()
{
  int ans = 0;
  SET(match);
  for(int l = 0; l < Lsize; l++)
    CLR(visited), ans += augmenting_path(l);
  return ans;
}

int main()
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int T; cin >> T;

  for(int cases = 1; cases <= T; cases++){
    int N, M, score = 0; cin >> N >> M;
    CLR(ANS); CLR(INPUT);
    CLR(rows); CLR(cols); 
    CLR(digsub); CLR(digsum);
    for(int m = 0; m < M; m++){
      char c; int x, y; cin >> c >> x >> y; x--; y--;
      INPUT[x][y] = ANS[x][y] = c == 'o' ? CIRCLE : (c == '+' ? PLUS : CROSS);
      score += ANS[x][y] == CIRCLE ? 2 : (ANS[x][y] != NONE ? 1 : 0);
      if(ANS[x][y] & CROSS)
        rows[x] = cols[y] = 1;
      if(ANS[x][y] & PLUS)
        digsum[x+y] = digsub[x-y+N-1] = 1;
    }
    

    //solving for horizontal & vertical
    FOR(x,2*N) edges[x].clear();
    FOR(x,N)
      if(!rows[x]){
        FOR(y,N)
          if(!cols[y])
            edges[x].pb(y+N), edges[y+N].pb(x);
      }
    Lsize = N;
    score += get_mcbm();
    FOR(y,N)
      if(match[y+N] != -1)
        ANS[match[y+N]][y] += CROSS;

    //solving for diagonals
    FOR(x,4*N)
      edges[x].clear();
    FOR(x,N) FOR(y,N){
      int a = x + y, b = x - y + N - 1;
      if(!digsum[a] && !digsub[b])
        edges[a].pb(b+2*N-1), edges[b+2*N-1].pb(a);
    }
    Lsize = 2*N-1;
    score += get_mcbm();
    FOR(i,2*N-1)
      if(match[i+2*N-1] != -1){
        int b = i, a = match[i+2*N-1];
        int y = (b - (a+N-1))/(-2), x = a - y;
        ANS[x][y] += PLUS;
      }

    
    int changed = 0;
    FOR(x,N) FOR(y,N) changed += ANS[x][y] != INPUT[x][y];
    cout << "Case #" << cases << ": " << score << " " << changed << "\n";
    FOR(x,N) FOR(y,N)
      if(ANS[x][y] != INPUT[x][y]){
        char c = ANS[x][y] == CIRCLE ? 'o' : (ANS[x][y] == PLUS ? '+' : 'x');
        cout << c << " " << x+1 << " " << y+1 << "\n";
      }
  }
}
