#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int cap[2010][2010], nn;
int vis[2010];
bool doit(int x, int y) {
  if (vis[x]) return false;
  if (x == y) return true;
  vis[x] = true;
  for (int z = 0; z < nn; z++) if (cap[x][z] && doit(z, y)) {
    cap[x][z]--;
    cap[z][x]++;
    return true;
  }
  return false;
}

int main() {
  int T, N, C, M, prob=1;
  for (cin >> T; T--;) {
    cin >> N >> C >> M;
    vector<int> tP(M), tC(M);
    for (int i = 0; i < M; i++) {
      cin >> tP[i] >> tC[i];
      tP[i]--; tC[i]--;
    }
    nn = 2+C+N;

    int ret1 = 0, tot = 0;
    memset(cap, 0, sizeof(cap));
    for (int i = 0; i < M; i++) {
      cap[0][2+tC[i]] += 1;
      for (int j = 0; j <= tP[i]; j++) {
        cap[2+tC[i]][2+C+j] += 1;
      }
      ret1 = max(ret1, cap[0][2+tC[i]]);
    }
    for (int j = 0; j < N; j++) {
      cap[2+C+j][1] = ret1;
    }
    while (tot < M) {
      memset(vis, 0, sizeof(vis));
      if (doit(0, 1)) {
        tot++;
      } else {
        ret1++;
        for (int j = 0; j < N; j++) cap[2+C+j][1] += 1;
      }
    }

    int ret2 = M;
    memset(cap, 0, sizeof(cap));
    for (int i = 0; i < M; i++) {
      cap[0][2+tC[i]] += 1;
      cap[2+tC[i]][2+C+tP[i]] += 1;
    }
    for (int j = 0; j < N; j++) {
      cap[2+C+j][1] = ret1;
    }
    for (;;) {
      memset(vis, 0, sizeof(vis));
      if (doit(0, 1)) {
        ret2--;
      } else {
        break;
      }
    }

    cout << "Case #" << prob++ << ": " << ret1 << ' ' << ret2 << endl;
  }
}
