#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i = a; i < b; i ++)
#define per(i,a,b) for (int i = b-1; i >= a; i --)

const int MAXLEN = 1e3 + 100;

char S[MAXLEN];
int a[MAXLEN];
int K, len;

int find(int x) {
  rep(i, x, len)
    if (a[i] == -1)
      return i;
  return len;
}

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int T, res;
  cin >> T;
  rep(t, 1, T + 1) {
    cin >> S;
    cin >> K;
    len = strlen(S);
    rep(i, 0, len)
      if (S[i] == '-')
        a[i] = -1;
      else a[i] = 1;
    res = 0;
    int i = 0;
    while (i < len) {
      i = find(-1);
      if (i >= len)
        break;
      if (len - i < K) {
        res = -1;
        break;
      }
      rep(j, 0, K)
        a[i + j] = -1 * a[i + j];
      res ++;
    }
    cout << "Case #" << t << ": ";
    if (res == -1)
      cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
  }
  return 0;
}
