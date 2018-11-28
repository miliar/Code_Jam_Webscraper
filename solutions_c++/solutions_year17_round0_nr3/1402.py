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

map<long long, long long> m;

void solve() {
  long long N, K;
  scanf("%lld%lld", &N, &K);
  m.clear();
  m[N] = 1;
  long long lastLen;
  while (K > 0) {
    map<long long, long long>::iterator it = m.end();
    --it;
    long long l = it->first, cnt = it->second;
    lastLen = l;
    K -= cnt;
    m.erase(it);
    m[(l - 1) / 2] += cnt;
    m[l / 2] += cnt;
  }
  printf("%lld %lld\n", lastLen / 2, (lastLen - 1) / 2);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
