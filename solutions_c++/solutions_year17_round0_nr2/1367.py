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

const int D = 20;
int d[D + 1];

long long solve() {
  long long N;
  scanf("%lld", &N);
  REP(i, D) { d[i] = N % 10; N /= 10; }
  int last_can_decrease = -1;
  FORD(i, D - 1, 0) {
    if (d[i] > d[i + 1]) last_can_decrease = i;
    if (d[i] < d[i + 1]) {
      d[last_can_decrease]--;
      FORD(j, last_can_decrease - 1, 0) d[j] = 9;
      break;
    }
  }
  long long ans = 0;
  FORD(i, D - 1, 0) ans = 10 * ans + d[i];
  return ans;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: %lld\n", t, solve());
  }
  return 0;
}
