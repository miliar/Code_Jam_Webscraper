#include <bits/stdc++.h>

using namespace std;

const int N = 1010;
const double PI = acos(-1.0);

struct Pancake {
  int r;
  int h;
};

Pancake pancakes[N];
long long f[N][N];

void SolveSingleCase(int case_id) {
  int n, k; cin >> n >> k;
  for (int i = 1; i <= n; ++i) {
    cin >> pancakes[i].r >> pancakes[i].h;
  }

  sort(pancakes + 1, pancakes + n + 1, [](const Pancake& a, const Pancake& b) { return a.r < b.r; });
  memset(f, -1, sizeof(f));

  f[0][0] = 0;
  double answer = 0.0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j <= k; ++j) {
      if (f[i][j] == -1) {
        continue;
      }

      f[i + 1][j] = max(f[i + 1][j], f[i][j]);
      if (j + 1 <= k) {
        f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + pancakes[i + 1].h * 1ll * pancakes[i + 1].r);

        if (j + 1 == k) {
          answer = max(answer, PI * (2.0 * f[i + 1][k] + pancakes[i + 1].r * 1ll * pancakes[i + 1].r));
        }
      }
    }
  }

  std::cout << "Case #" << case_id << ": " << answer << "\n";
}

int main() {
  std::cout << fixed << setprecision(12);
  int cases_num; cin >> cases_num;

  for (int i = 0; i < cases_num; ++i) {
    SolveSingleCase(i + 1);
  }

  return 0;
}
