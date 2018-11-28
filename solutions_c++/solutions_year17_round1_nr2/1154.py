#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

const int MAXN = 50;
const int MAXP = 50;

int N, P;
int R[MAXN];
int Q[MAXN][MAXP];
int l[MAXN][MAXP], r[MAXN][MAXP];

const int MAXM = 1001;
int nx,ny,m,ans;//nx,ny分别为二分图两边节点的个数,两边的节点分别用1..nx,1..ny编号,m为边数
bool g[MAXM][MAXM];//图G邻接矩阵g[x][y]
bool y[MAXM];//Y集合中点i访问标记
int link[MAXM];//link[y]表示当前与y节点相邻的x节点

void init() {
    int x,y;
    memset(g,0,sizeof(g));
    ans = 0;
    nx = ny = P;
    for (int i = 0; i < P; i++) {
      for (int j = 0; j < P; j++) {
        if (r[0][i] < l[1][j] || r[1][j] < l[0][i]) {
        } else {
          g[i + 1][j + 1] = true;
        }
      }
    }
}

bool find(int x) { //是否存在X集合中节点x开始的增广路
    for (int i = 1;i <= ny;i++)
        if (g[x][i] && !y[i]) { //如果节点i与x相邻并且未访问过
            y[i] = true;
            if (link[i] == -1 || find(link[i])) { //如果找到一个未盖点i中或从与i相邻的节点出发有增广路
                link[i] = x;
                return true;
            }
        }
    return false;
}

int MaximumMatch() {
    int ret = 0;
    memset(link,-1,sizeof(link));
    for (int i = 1;i <= nx;i++) {
        memset(y,0,sizeof(y));
        if (find(i))
            ret++;
    }
    return ret;
}


int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    cin >> N >> P;
    for (int i = 0; i < N; ++i) {
      cin >> R[i];
    }
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < P; ++j) {
        cin >> Q[i][j];
        r[i][j] = ((Q[i][j] * 10)/ (9 * R[i]));
        l[i][j] = ((Q[i][j] * 10 + 11 * R [i] - 1)/ (11 * R[i]));
      }
    }
    int ans = 0;
    if (N == 1) {
      for (int j = 0; j < P; ++j) {
        if (l[0][j] <= r[0][j]) {
          ans++;
        }
      }
    } else {
      init();
      ans = MaximumMatch();
    }
    printf("Case #%d: %d\n", cases + 1, ans);
  }
}