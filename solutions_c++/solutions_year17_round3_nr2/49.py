#include <bits/stdc++.h>

using namespace std;

// const int T = 10;
const int T = 24 * 60;

bool is_available[2][T];
int f[T + 1][T / 2 + 1][2];

void UpdateAvailability(int n, bool is_available[T]) {
  std::fill(is_available, is_available + T, true);
  for (int i = 0; i < n; ++i) {
    int b, e; cin >> b >> e;

    std::fill(is_available + b, is_available + e, false);
  }
}

void Update(int& a, int b) {
  if (b == -1) {
    return;
  } else if (a == -1) {
    a = b;
  } else {
    a = min(a, b);
  }
}

int StartWith(int parent_id) {
  memset(f, -1, sizeof(f));

  f[0][0][parent_id] = 0;
  for (int t = 0; t < T; ++t) {
    for (int c = 0; c <= T / 2; ++c) {
      for (int p = 0; p < 2; ++p) {
        if (f[t][c][p] == -1) {
          continue;
        }

        for (int next_p = 0; next_p < 2; ++next_p) {
          if (!is_available[next_p][t] || (next_p == 0 && c + 1 > T / 2)) {
            continue;
          }

          Update(f[t + 1][c + (next_p == 0)][next_p], f[t][c][p] + (p != next_p));
        }
      }
    }
  }

  return f[T][T / 2][parent_id];
}

void SolveSingleCase(int case_id) {
  int n, m; cin >> n >> m;
  UpdateAvailability(n, is_available[0]);
  UpdateAvailability(m, is_available[1]);

  int answer = -1;
  Update(answer, StartWith(0));
  Update(answer, StartWith(1));
  cout << "Case #" << case_id << ": " << answer << "\n";
}

int main() {
  int cases_num; cin >> cases_num;

  for (int i = 0; i < cases_num; ++i) {
    SolveSingleCase(i + 1);
  }

  return 0;
}
