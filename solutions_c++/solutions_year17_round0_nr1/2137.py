#include <bits/stdc++.h>
#define REP(x, n) for (int x = 0; x < (int)(n); x++)
#define RREP(x, n) for (int x = (int)(n)-1; x >= 0; --x)
#define FOR(x, m, n) for (int x = (int)m; x < (int)(n); x++)
#define EACH(itr, cont) \
  for (typeof((cont).begin()) itr = (cont).begin(); itr != (cont).end(); ++itr)
#define ALL(X) (X).begin(), (X).end()
#define mem0(X) memset((X), 0, sizeof(X))
#define mem1(X) memset((X), 255, sizeof(X))

using namespace std;
typedef long long LL;

void flip(string &s, int idx, int K){
  FOR(i, idx, idx + K) if (s[i] == '-') s[i] = '+';
  else s[i] = '-';
}

void doStuff() {
  string s;
  int K, result = 0;
  cin >> s >> K;
  int N = s.length();
  REP(i, N) if (s[i] == '-') {
    if (i + K > N) {
      printf("IMPOSSIBLE\n");
      return;
    } else
      flip(s, i, K), ++result;
  }
  printf("%d\n", result);
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d: ", t + 1), doStuff();
  return 0;
}