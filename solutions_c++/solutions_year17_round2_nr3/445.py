#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int Tests;

int a[1000], b[1000], Q[1000000], n, q, inq[1000];
double f[1000], d[1000][1000];

int main() {
  scanf("%d", &Tests); 
  for (int tts = 0; Tests--; ) {
    scanf("%d%d", &n, &q);
    for (int i = 0; i < n; ++i) scanf("%d%d", &a[i], &b[i]);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        int dd;
        scanf("%d", &dd);
        d[i][j] = dd;
      }

    for (int k = 0; k < n; ++k)
      for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
          if (d[i][k] != -1 && d[k][j] != -1)
          if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j])
            d[i][j] = d[i][k] + d[k][j];
    printf("Case #%d:", ++tts);

    for (; q--; ) {
      int u, v;
      scanf("%d%d", &u, &v);
      --u, --v;

      for (int i = 0; i < n; ++i) {
        f[i] = 1e40;
        inq[i] = 0;
      }

      f[u] = 0;
      int top = 0, tail = 1;
      Q[1] = u; inq[u] = 1;
      for (; top < tail; ) {
        int x = Q[++top];
        for (int i = 0; i < n; ++i)
          if (d[x][i] != -1)
          if (i != x && d[x][i] <= a[x] && f[x] + (double)d[x][i] / (double)b[x] < f[i]) {
            f[i] = f[x] + (double)d[x][i] / (double)b[x];
            if (!inq[i]) {
              Q[++tail] = i;
              inq[i] = 1;
            }
          }
        inq[x] = 0;
      }

      printf(" %lf", f[v]);
    }
    puts("");
  }
}