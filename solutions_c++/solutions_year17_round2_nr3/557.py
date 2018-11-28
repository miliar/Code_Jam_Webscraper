#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)  
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define MP(x,y) make_pair(x,y)
#define REP(i,n) for(int i=0; i<(int)(n); i++)

const int INF = 1LL << 30;
int N, Q;
long long E[100], S[100];
long long dist[100][100];
double tm[100][100];

void solve() {
  cin >> N >> Q;
  REP (i, N) cin >> E[i] >> S[i];
  REP (i, N) REP (j, N) {
    cin >> dist[i][j];
    if (dist[i][j] == -1)
      dist[i][j] = INF;
  }

  REP (k, N) REP (i, N) REP (j, N) dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
  REP (i, N) REP (j, N) {
    tm[i][j] = 1e100;
    if (dist[i][j] <= E[i])
      tm[i][j] = 1.0 * dist[i][j] / S[i]; 
  }

  REP (k, N) REP (i, N) REP (j, N) tm[i][j] = min(tm[i][j], tm[i][k] + tm[k][j]);
  
  cout << fixed << setprecision(10);
  REP (i, Q) {
    int u, v;
    cin >> u >> v;
    cout << tm[--u][--v];
    if (i == Q-1)
      cout << endl;
    else
      cout << " ";
  }
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
