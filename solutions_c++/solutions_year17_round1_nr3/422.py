#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long int64;

const int N = 101;
const int INF = ~0U >> 2;

int hd, ad, hk, ak, b, d;
int sd[N][N][N][N];

int dfs(int hd, int ad, int hk, int ak) {
  if (hk == 0) return 0;
  if (ad >= hk) return 1;

  int& a = sd[hd][ad][hk][ak];
  if (a != -1) return a;
  a = INF;

  // 1. attack
  if (ak < hd) check_min(a, 1 + dfs(hd - ak, ad, hk - ad, ak));

  // 2. buff
  if (ak < hd) check_min(a, 1 + dfs(hd - ak, min(hk, ad + b), hk, ak));

  // 3. cure
  if (::hd > ak) check_min(a, 1 + dfs(::hd - ak, ad, hk, ak));

  // 4. debuff
  if (ak > 0 && ak - d < hd) check_min(a, 1 + dfs(hd - max(ak - d, 0), ad, hk, max(ak - d, 0)));

  return a;
}

void solve() {
  scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
  fill(sd[0][0][0], sd[N][0][0], -1);
  int ans = dfs(hd, ad, hk, ak);
  if (ans == INF) {
    printf("IMPOSSIBLE\n");
  } else {
    printf("%d\n", ans);
  }
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: ", index);
    solve();
  }
  return 0;
}
