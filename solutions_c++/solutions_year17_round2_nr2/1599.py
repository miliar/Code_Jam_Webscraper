#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

// #define FL fflush(stdout)

#define MOD 1000000007
#define INF 2000000000
#define maxn 1010

int GLL(LL& x) {
  return scanf("%lld", &x);
}

int GI(int& x) {
  return scanf("%d", &x);
}

bool adj[6][6];
vector<char> transl = {'R', 'O', 'Y', 'G', 'B', 'V'};
vector<int> path;

void dfs(int node, vector<int> cnts) {
//  printf("\nvisiting %d %c\n", node, transl[node]);
//  printf("counts: "); for (auto c: cnts) printf("%d ", c); printf("\n");
  cnts[node]--;
  path.PB(node);

  int maxcnt = 0;
  int next = -1;
  FORN(i, 6) {
    if (adj[node][i] && cnts[i] > 0) {
      if (cnts[i] > maxcnt) {
        maxcnt = cnts[i];
        next = i;
      }
    }
  }
  if (next != -1) {
//    printf("   %c --> %c\n", transl[node], transl[next]);
    dfs(next, cnts);
  }

//  printf("path:   "); for (auto a : path) { cout << transl[a]; }
//  printf("\n");
}

void solve(int t) {
  int n;
  vector<int> c;
  c.resize(6);
  GI(n);
  FORN(i, 6) GI(c[i]);

  FORN(i, 6) {
    vector<int> empty;
    swap(empty, path);
    if (c[i]) {
//      printf("\n \n -------------------------------------\n");
      dfs(i, c);
    }
//    printf("path of size %d: ", path.size());
//    for (auto a : path) { printf("%c", a); }
    if (path.size() == n && path[0] != path[n-1]) break;
  }

//  if (path.size() == n) {
//    for (auto a : path) { cout << transl[a]; }
//    cout << "\n";
//  }

  if (path.size() == n && path[0] != path[n-1]) {
    printf("Case #%d: ", t+1);
    for (auto a : path) { printf("%c", transl[a]); }
    printf("\n");
  } else {
    printf("Case #%d: IMPOSSIBLE\n", t+1);
  }
}

int T;
int main() {
  memset(adj, 0, sizeof adj);

  adj[3][0] = 1;
  adj[5][2] = 1;
  adj[1][4] = 1;

  adj[0][2] = 1;
  adj[0][3] = 1;
  adj[0][4] = 1;

  adj[2][0] = 1;
  adj[2][4] = 1;
  adj[2][5] = 1;

  adj[4][0] = 1;
  adj[4][1] = 1;
  adj[4][2] = 1;

  GI(T);
  for (int t = 0; t < T; t++) {
    solve(t);
  }
  return 0;
}
