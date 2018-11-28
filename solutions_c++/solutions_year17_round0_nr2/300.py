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
    int n = SZ(s);
    for (int i = 0; i < n; i++) {
      if (!is_sorted(begin(s), begin(s) + i + 1)) {
        assert(i > 0);
        int j = i - 1;
        while (j >= 0 && s[j] == s[i - 1]) {
          j--;
        }
        s[j + 1]--;
        for (int k = j + 2; k < n; k++) {
          s[k] = '9';
        }
        break;
      }
    }
    int start = 0;
    while (start < n - 1 && s[start] == '0') {
      start++;
    }
    s = s.substr(start, n - start);
    static int caseNo = 1;
    printf("Case #%d: %s\n", caseNo++, s.c_str());
  }
  return 0;
}

