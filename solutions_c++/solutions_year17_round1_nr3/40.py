/* Written by Filip Hlasek 2017 */
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>

#define FOR(i, a, b)   for (int i = (a); i <= (b); i++)
#define FORD(i, a, b)  for (int i = (a); i >= (b); i--)
#define REP(i, b)      for (int i =  0 ; i <  (b); i++)

using namespace std;

long long ceiling(long long A, long long B) { return (A + B - 1) / B; }

long long attackingMoves(long long H, long long A, long long B) {
  long long l = 0, r = H;
  while (l + 10 < r) {
    long long m1 = (2 * l + r) / 3, m2 = (l + 2 * r) / 3;
    long long v1 = m1 + ceiling(H, A + B * m1);
    long long v2 = m2 + ceiling(H, A + B * m2);
    if (v1 < v2) r = m2;
    else l = m1;
  }
  long long best = l + ceiling(H, A + B * l);
  FOR(i, l, r) best = min(best, i + ceiling(H, A + B * i));
  return best;
}

long long simulate(long long H, long long A, long long D, long long moves, int d) {
  long long ans = 0;
  long long h = H;
  // printf("H: %lld A: %lld D: %lld moves: %lld d: %d\n", H, A, D, moves, d);
  while (true) {
    ans++;
    if (moves == 1) break;
    if (d && h - max(0LL, A - D) > 0) {
      d--;
      A = max(0LL, A - D);
      h -= A;
    } else if (h - A > 0) {
      moves--;
      h -= A;
    } else {
      if (H - A <= h) return -1;
      h = H;
      h -= A;
      if (h <= 0) return -1;
    }
  }
  return ans;
}

long long defenceMoves(long long H, long long A, long long D, long long moves) {
  if ((moves - 1) * A < H) return moves;
  long long ans = -1;
  for (int d = 0; d <= A; ++d) {
    long long tmp = simulate(H, A, D, moves, d);
    if (ans == -1 || ans > tmp) ans = tmp;
  }
  return ans;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    int Hd, Ad, Hk, Ak, B, D;
    scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
    printf("Case #%d: ", t);
    long long attack = attackingMoves(Hk, Ad, B);
    long long defence = defenceMoves(Hd, Ak, D, attack);
    if (defence == -1) {
      printf("IMPOSSIBLE\n");
    } else { 
      printf("%lld\n", defence);
    }

  }
  return 0;
}
