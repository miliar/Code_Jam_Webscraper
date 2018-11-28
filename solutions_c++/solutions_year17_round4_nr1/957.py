#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define ALL(a) begin(a), end(a)
#define SZ(a) ((int)(a).size())

#ifdef __DEBUG
#define debug if (true)
#else
#define debug if (false)
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int N = 105;

int n, p;
int g[N];
int memo[N][N][N];

int go(int one, int two, int three) {
  if (memo[one][two][three] != -1) {
    return memo[one][two][three];
  }
  int ret = 0;
  for (int i = 0; i <= p - 1; i++) {
    if (one < i) {
      break;
    }
    for (int j = 0; j <= p - 1; j++) {
      if (two < j) {
        break;
      }
      for (int k = 0; k <= p - 1; k++) {
        if (three < k) {
          break;
        }
        if (i == j && j == k && k == 0) {
          continue;
        }
        int tot = (i + j * 2 + k * 3) % p;
        if (tot == 0) {
          ret = max(ret, 1 + go(one - i, two - j, three - k));
        }
      }
    }
  }
  if (one >= p) {
    ret = max(ret, 1 + go(one - p, two, three));
  }
  if (two >= p) {
    ret = max(ret, 1 + go(one, two - p, three));
  }
  if (three >= p) {
    ret = max(ret, 1 + go(one, two, three - p));
  }
  if (one > 0 || two > 0 || three > 0) {
    ret = max(ret, 1);
  }
  debug printf("%d %d %d -> %d\n", one, two, three, ret);
  return memo[one][two][three] = ret;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    cin >> n >> p;
    for (int i = 0; i < n; i++) {
      cin >> g[i];
      g[i] %= p;
    }
    int cnt[4] = {0, 0, 0, 0};
    for (int i = 0; i < n; i++) {
      cnt[g[i]]++;
    }
    static int caseNo = 1;
    memset(memo, -1, sizeof(memo));
    printf("Case #%d: %d\n", caseNo++, go(cnt[1], cnt[2], cnt[3]) + cnt[0]);
  }
  return 0;
}

