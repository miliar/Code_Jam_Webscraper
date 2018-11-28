#define NDEBUG
#include <cstdint>
#include <cstring>
#include <functional>
#include <iostream>
using namespace std;

#define MINUSONE(v) memset((v), -1, sizeof (v))
template<typename T, typename U> inline bool makemax(T &res, const U &x) {
  if (x > res) {
    res = x;
    return true;
  }
  return false;
}
#define repeat(n) for (int repc = (n); repc > 0; --repc)

const int MAXN = 103;
int8_t memo[MAXN][MAXN][MAXN][MAXN][4];

int P;
struct State {
  int8_t c[4], m;
};
int calc(const State S) {
  if (S.c[0] == 0 && S.c[1] == 0 && S.c[2] == 0 && S.c[3] == 0) {
    return 0;
  }
  int8_t& ref = memo[S.c[0]][S.c[1]][S.c[2]][S.c[3]][S.m];
  if (ref != -1) {
    return ref;
  }
  int ans = 0;
  for (int i = 0; i < P; ++i) {
    if (S.c[i] > 0) {
      State n = S;
      --n.c[i];
      n.m = (S.m + i) % P;
      makemax(ans, calc(n));
    }
  }
  ans += S.m == 0;
  // fprintf(stderr, "f(%d, %d, %d, %d, m=%d) = %d\n", S.c[0], S.c[1], S.c[2], S.c[3], S.m, ans);
  return ref = ans;
}

int solve() {
  int N;
  cin >> N >> P;

  State init;
  for (int i=0; i<4; ++i) {
    init.c[i] = 0;
  }
  init.m = 0;
  repeat (N) {
    int x;
    cin >> x;
    ++init.c[x % P];
  }
  for (int i=0; i<=N; ++i) {
    MINUSONE(memo[i]);
  }
  return calc(init);
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": " << solve() << endl;
  }
}
