#include<bits/stdtr1c++.h>
using namespace std;

int T, N, P, G[4];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> N >> P;
    memset(G, 0, sizeof G);
    while (N--) {
      int a; cin >> a;
      G[a%P]++;
    }
    int res = G[0];
    if (P == 2) {
      res += G[1]/2;
      if (G[1] %= 2) {
        res++;
      }
    } else if (P == 3) {
      res += min(G[1], G[2]);
      res += abs(G[1] - G[2]) / 3;
      if (abs(G[1] - G[2]) % 3) {
        res++;
      }
    } else if (P == 4) {
      res += min(G[1], G[3]);
      res += G[2]/2;
      int a = abs(G[1] - G[3]);
      if (G[2] % 2) {
        if (a >= 2) {
          res += 1 + (a-2) / 4;
          if ((a-2)%4) {
            res++;
          }
        } else {
          res++;
        }
      } else {
        res += a / 4;
        if (a % 4) {
          res++;
        }
      }
    }
    cout << res << endl;
  }

  return 0;
}
