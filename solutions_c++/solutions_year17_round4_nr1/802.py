#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>

#define pb push_back
#define mp make_pair

#define f first
#define s second

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

const int N = (int) 1e6 + 7;
const int MOD = (int) 1e9 + 7;

const int SQRT = (int) 320;

int n, p;
int cur[101][101][101][4];
int nxt[101][101][101][4];

int cnt[10];

void upd(int &a, int b) {
  a = max(a, b);
}

void clr() {
  for (int c0 = 0; c0 <= cnt[0]; c0++)
    for (int c1 = 0; c1 <= cnt[1]; c1++)
      for (int c2 = 0; c2 <= cnt[2]; c2++)
        for (int last = 0; last < p; last++)
          nxt[c0][c1][c2][last] = -MOD;
}

int solveAll() {
  cur[0][0][0][0] = 0;
  for (int i = 1; i < p; i++)
    cur[0][0][0][i] = -MOD;

  for (int i = 0; i < n; i++) {
    clr();
    //if(i==2)cout<<i<<' '<<cnt[0]<<' '<<cnt[1]<<' '<<cnt[2]<<"!!!"<<endl;
    for (int c0 = 0; c0 <= cnt[0]; c0++) {
      for (int c1 = 0; c1 <= cnt[1]; c1++) {
        //if(i==2)cout<<c0<<' '<<c1<<' '<<cnt[2]<<" PLEAASE\n";
        for (int c2 = 0; c2 <= cnt[2]; c2++) {
          int c3 = i - c0 - c1 - c2;
          //if(i==2)cout<<c0<<' '<<c1<<' '<<c2<<' '<<c3<<' '<<cnt[2]<<endl;
          if (c3 > cnt[3]) continue;
          if (c3 < 0) break;
          for (int last = 0; last < p; last++) {
            //cout<<i<<" and "<<c0<<' '<<c1<<' '<<c2<<' '<<c3<<" with last "<<last<<" is " <<cur[c0][c1][c2][last]<<endl;
            if (c0 < cnt[0]) {
              upd(nxt[c0 + 1][c1][c2][last], cur[c0][c1][c2][last] + (last == 0));
            }
            if (c1 < cnt[1]) {
              upd(nxt[c0][c1 + 1][c2][(last + p - 1) % p], cur[c0][c1][c2][last] + (last == 0));
            }
            if (c2 < cnt[2]) {
              upd(nxt[c0][c1][c2 + 1][(last + p - 2) % p], cur[c0][c1][c2][last] + (last == 0));
            }
            if (c3 < cnt[3]) {
              upd(nxt[c0][c1][c2][(last + p - 3) % p], cur[c0][c1][c2][last] + (last == 0));
            }
          }
        }
      }
    }
    memcpy(cur, nxt, sizeof nxt);
  }
  int res = 0;
  for (int i = 0; i < p; i++) res = max(res, cur[cnt[0]][cnt[1]][cnt[2]][i]);
  return res;
}

void solve() {
  scanf("%d%d", &n, &p);
  memset(cnt, 0, sizeof cnt);
  for (int i = 0; i < n; i++) {
    int x; scanf("%d", &x);
    x %= p;
    cnt[x]++;
  }
  printf("%d\n", solveAll());
}

int main() {
  #ifdef LOCAL
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif

  int t; scanf("%d", &t);
  for (int tcase = 1; tcase <= t; tcase++) {
    printf("Case #%d: ", tcase);
    solve();
    cerr << tcase << " is done\n";
  }


  return 0;
}