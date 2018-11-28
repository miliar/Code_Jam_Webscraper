#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define all(a) a.begin(), a.end()
#define fi first
#define se second
#define sz(a) a.size()

typedef vector <int> vi;
typedef long long ll;
typedef pair <int, int> pii;

const int mod = 1e9 + 7, N = 7;

int T;
string S;

int main() {
//  freopen("output.txt", "w", stdout);
  cin >> T;
  for (int test = 1, K, ans, len, pos, cnt; test <= T; test++) {
    cin >> S >> K;
    if (!count(all(S), '-')) {
      printf("Case #%d: 0\n", test);
      continue;
    }
    ans = 1;
    len = sz(S);
    cnt = 0;
    while (1) {
      pos = S.find('-');
      if (pos == -1) {
        break;
      }
      cnt++;
      if (pos + K <= len) {
        for (int start = pos; start < pos + K; start++) {
          if (S[start] == '-') {
            S[start] = '+';
          } else {
            S[start] = '-';
          }
        }
      } else {
        ans = 0;
        break;
      }
    }
    if (ans) {
      printf("Case #%d: %d\n", test, cnt);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", test);      
    }
  }
  return 0;
}