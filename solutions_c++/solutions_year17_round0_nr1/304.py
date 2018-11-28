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
    string s;
    cin >> s;
    int k;
    cin >> k;
    int flipCount = 0;
    for (int i = 0; i + k <= SZ(s); i++) {
      if (s[i] == '-') {
        flipCount++;
        for (int j = 0; j < k; j++) {
          s[i + j] = s[i + j] == '+' ? '-' : '+';
        }
      }
    }
    bool can = count(ALL(s), '-') == 0;
    static int caseNo = 1;
    if (!can) {
      printf("Case #%d: IMPOSSIBLE\n", caseNo++);
    } else {
      printf("Case #%d: %d\n", caseNo++, flipCount);
    }
  }
  return 0;
}

