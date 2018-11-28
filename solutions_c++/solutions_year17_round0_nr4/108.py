#include <iostream>
#include <cstring>
#include <vector>
#include <utility>
using namespace std;

int N, M;
int A[128][128];
int B[128][128];

int G[256][256], Gc;
int X[256], Y[256];
int V[256];

int match(int u) {
  V[u] = 1;
  for(int i=1;i<=Gc;i++) if (G[u][i] && !Y[i]) {
    X[u] = i;
    Y[i] = u;
    return 1;
  }
  for(int i=1;i<=Gc;i++) if (G[u][i] && !V[Y[i]]) {
    if (match(Y[i])) {
      X[u] = i;
      Y[i] = u;
      return 1;
    }
  }
  return 0;
}

void matching() {
  memset(X,0,sizeof(X));
  memset(Y,0,sizeof(Y));
  for(int i=1;i<=Gc;i++) {
    memset(V,0,sizeof(V));
    match(i);
  }
}

int dxn[128][128], dyn[128][128];
struct chang {
  int type;
  int row;
  int col;
};

void do_case(int te) {
  cin >> N >> M;
  memset(A,0,sizeof(A));
  for(int i=1;i<=M;i++) {
    char t;
    int r, c;
    cin >> t >> r >> c;
    if (t == '+') A[r][c] = 1;
    if (t == 'x') A[r][c] = 2;
    if (t == 'o') A[r][c] = 3;
  }
  memcpy(B,A,sizeof(A));
  // build bipartite graph for row-col fill
  memset(G,0,sizeof(G));
  Gc = N;
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) G[i][j] = 1;
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) if (B[i][j]&2) for(int k=1;k<=Gc;k++) G[i][k] = G[k][j] = 0;
  matching();
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) if(X[i] == j) B[i][j] |= 2;
  // build bipartite graph for diags fill
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) {
    dxn[i][j] = i+j-1;
    dyn[i][j] = j-i+N;
  }
  memset(G,0,sizeof(G));
  Gc = 2*N - 1;
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) G[dxn[i][j]][dyn[i][j]] = 1;
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) if (B[i][j]&1) for(int k=1;k<=Gc;k++) G[dxn[i][j]][k] = G[k][dyn[i][j]] = 0;
  matching();
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) if(X[dxn[i][j]] == dyn[i][j]) B[i][j] |= 1;
  // compute the style + compute the diff between A and B
  int res=0;
  vector<chang> C;
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++) {
    res += !!(B[i][j] & 1);
    res += !!(B[i][j] & 2);
    if (B[i][j] != A[i][j]) {
      chang c;
      c.type = B[i][j];
      c.row = i;
      c.col = j;
      C.push_back(c);
    }
  }
  // all done
  // cout << "A:" << endl;
  // for(int i=1;i<=N;i++) {
  //   for(int j=1;j<=N;j++) {
  //     if (A[i][j] == 0) cout << ".";
  //     if (A[i][j] == 1) cout << "+";
  //     if (A[i][j] == 2) cout << "x";
  //     if (A[i][j] == 3) cout << "o";
  //   }
  //   cout << endl;
  // }
  // cout << "B:" << endl;
  // for(int i=1;i<=N;i++) {
  //   for(int j=1;j<=N;j++) {
  //     if (B[i][j] == 0) cout << ".";
  //     if (B[i][j] == 1) cout << "+";
  //     if (B[i][j] == 2) cout << "x";
  //     if (B[i][j] == 3) cout << "o";
  //   }
  //   cout << endl;
  // }
  cout << "Case #" << te << ": " << res << " " << C.size() << endl;
  for(int i=0;i<C.size();i++) {
    if (C[i].type == 1) cout << "+ ";
    if (C[i].type == 2) cout << "x ";
    if (C[i].type == 3) cout << "o ";
    cout << C[i].row << " " << C[i].col << endl;
  }
}

int main() {
  int te, T=1;
  cin >> te;
  while(te--) {
    do_case(T);
    ++T;
  }
  return 0;
}