#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long double ld;

const ld pi = acos(-1);

struct ts {
  ld r, h;
  ts() { }
  bool operator< (const ts& rhs) const {
    return r > rhs.r;
  }
} seq[1000];

ld memo[1001][1001];
int n, k;
bool saw[1001][1001];
ld go(int i = 0, int j = 0) {
  if(saw[i][j]) return memo[i][j];
  saw[i][j] = true;
  if(j == k || i == n) return memo[i][j] = 0.0;
  ld t = seq[i].h*2*pi*seq[i].r;
  if(j == 0) t += seq[i].r*seq[i].r*pi;
  return memo[i][j] = max(go(i+1, j+1) + t, go(i+1, j));
}

int main() {
  int t; scanf("%d", &t);
  for(int cas = 1; cas <= t; ++cas) {
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; ++i) scanf("%Lf %Lf", &seq[i].r, &seq[i].h);
    memset(saw, false, sizeof saw);
    sort(seq, seq + n);
    printf("Case #%d: %.9Lf\n", cas, go());
  }
  return 0;
}