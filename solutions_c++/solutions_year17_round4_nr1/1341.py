#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_G = 101;
const int MAX_P = 4;

int p;
int dp[MAX_G][MAX_G][MAX_G][MAX_G][MAX_P];
int target[MAX_P];

int eat(int r0, int r1, int r2, int r3, int rem, int which) {
  int ans = (rem == 0);

  if (which == 0) r0--;
  if (which == 1) r1--;
  if (which == 2) r2--;
  if (which == 3) r3--;

  rem = p - ((which - rem + p) % p);
  rem %= p;

  ans += dp[r0][r1][r2][r3][rem];
  return ans;
}

int main() {
  int tests; cin >> tests;
  for (int test = 1; test <= tests; test++) {
    for (int i = 0; i < MAX_P; i++)
      target[i] = 0;

    int n; cin >> n >> p;
    for (int i = 0; i < n; i++) {
      int g; cin >> g;
      target[g % p]++;
    }

    for (int r0 = 0; r0 <= target[0]; r0++) {
      for (int r1 = 0; r1 <= target[1]; r1++) {
        for (int r2 = 0; r2 <= target[2]; r2++) {
          for (int r3 = 0; r3 <= target[3]; r3++) {
            for (int rem = 0; rem < p; rem++) {
              int &ans = dp[r0][r1][r2][r3][rem];
              ans = 0;

              if (r0 > 0)
                ans = max(ans, eat(r0, r1, r2, r3, rem, 0));
              if (r1 > 0)
                ans = max(ans, eat(r0, r1, r2, r3, rem, 1));
              if (r2 > 0)
                ans = max(ans, eat(r0, r1, r2, r3, rem, 2));
              if (r3 > 0)
                ans = max(ans, eat(r0, r1, r2, r3, rem, 3));
            }
          }
        }
      }
    }

    int ans = dp[target[0]][target[1]][target[2]][target[3]][0];
    cout << "Case #" << test << ": " << ans << endl;
  }
}
