#include <cstdio>
#include <vector>
#include <functional>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)

int T, N, P, R[55], Q[55][55], top[55];
int lo(int i) {
  int j = top[i];
  int num = 10*Q[i][j];
  int den = 11*R[i];
  return (num + den - 1) / den;
}
int hi(int i) {
  int j = top[i];
  int num = 10 * Q[i][j];
  int den = 9 * R[i];
  return num / den;
}
bool lower(int i1, int i2) {
  return 1LL * Q[i1][top[i1]] * R[i2] < 1LL * Q[i2][top[i2]] * R[i1];
}

int main() {
  //freopen("c.in", "r", stdin);
  scanf("%d", &T);
  FOR(cn, 1, T) {
    printf("Case #%d: ", cn);
    scanf("%d%d", &N, &P);
    REP(i, N) scanf("%d", R+i);
    REP(i, N) {
      REP(j, P) scanf("%d", &Q[i][j]);
      sort(Q[i], Q[i] + P, greater<int>());
      //printf("here i=%d, N=%d\n", i, N);
      // REP(j, P) printf("%d ", Q[i][j]);      puts("");
      top[i] = 0;
    }
    int ans = 0;
    while (true) {
      bool done = false;
      REP(i, N) if (top[i] >= P) { done = true; break; }
      if (done) break;
      //REP(i, N) printf("%d ", top[i]); puts("");
      int maxi = 0;
      REP(i, N) {
        if (lower(maxi, i)) maxi = i;
      }
      bool good = true;
      REP(i, N)
        if (lo(maxi) > hi(i)) {
          good = false;
          break;
        }
      if (good) {
        ans++;
        REP(i, N) top[i]++;
      } else {
        top[maxi]++;
      }
    }
    printf("%d\n", ans);
    
  }
  return 0;
}
