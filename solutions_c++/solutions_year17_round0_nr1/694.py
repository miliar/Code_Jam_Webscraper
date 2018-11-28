#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long int64;

const int N = 1010;

char s[N];
int n, k;

void solve() {
  scanf("%s%d", s, &k);
  n = strlen(s);
  int ans = 0;
  for (int i = 0; i <= n - k; ++i) {
    if (s[i] != '-') continue;
    ++ans;
    for (int j = 0; j < k; ++j) {
      s[i + j] = s[i + j] == '+' ? '-' : '+';
    }
  }
  for (int i = n - k; i < n; ++i) {
    if (s[i] != '+') {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  printf("%d\n", ans);
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
