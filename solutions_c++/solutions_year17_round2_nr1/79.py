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

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    int n, d;
    cin >> d >> n;
    vi k(n), s(n);
    for (int i = 0; i < n; i++) {
      cin >> k[i] >> s[i];
    }
    long double ans = 1e19;
    for (int i = 0; i < n; i++) {
      ans = min(ans, d / ((d - k[i]) / ((long double)s[i])));
    }
    static int caseNo = 1;
    printf("Case #%d: %.7Lf\n", caseNo++, ans);
  }
  return 0;
}

