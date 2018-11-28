
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef long double ld;

#define For(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define Ford(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define Rep(i, n) for (int i(0), _n(n); i < _n; ++i)
#define Repd(i, n) for (int i((n)-1); i >= 0; --i)
#define Fill(a, c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define Max(a, b) (a) < (b) ? (b) : (a)
#define Min(a, b) (a) < (b) ? (a) : (b)

template <typename T, typename S> T cast(S s) {
  stringstream ss;
  ss << s;
  T res;
  ss >> res;
  return res;
}

template <typename T> inline T sqr(T a) { return a * a; }
template <typename T> inline int Size(const T &c) { return (int)c.size(); }
template <typename T> inline void checkMin(T &a, T b) {
  if (b < a)
    a = b;
}
template <typename T> inline void checkMax(T &a, T b) {
  if (b > a)
    a = b;
}

char S[1010];
int K;
char buf[1024];

int Solve() {
  int len = (int)strlen(S);
  int flip_count = 0;
  For(t, 0, len - K) {
    if (S[t] == '-') {
      flip_count++;
      For(u, t, t + K - 1) {
        if (S[u] == '-')
          S[u] = '+';
        else
          S[u] = '-';
      }
    }
  }
  For(t, len - K + 1, len - 1) {
    if (S[t] == '-') {
      return -1;
    }
  }

  return flip_count;
}

int main() {

  fgets(buf, 1024, stdin);
  int T = atoi(buf);
  For(tcase, 1, T) {
    scanf("%s %d", S, &K);

    int ans = Solve();

    if (ans == -1)
      printf("Case #%d: IMPOSSIBLE", tcase);
    else
      printf("Case #%d: %d", tcase, ans);
    printf("\n");
  }
}
