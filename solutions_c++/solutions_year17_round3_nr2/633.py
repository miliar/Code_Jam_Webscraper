#include <bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')

typedef long long int lld;
const int VMAX = 1440;
const int INF = VMAX * 2;

bitset < 2 * VMAX + 5 > cameron;
bitset < 2 * VMAX + 5 > james;
vector<pair<int, int>> cameron_activities;
vector<pair<int, int>> james_activities;
int dp[2 * VMAX + 5][2 * VMAX + 5][2];

int min(const int& a, const int& b, const int& c) {
  return min(a, min(b, c));
}

int solve() {
  if (!cameron[0]) {
    dp[0][1][0] = 0;
  }
  if (!james[0]) {
    dp[0][0][1] = 0;
  }

  for (int i = 0; i < VMAX; ++i) {
    for (int j = 0; j <= VMAX / 2; ++j) {
      if (!cameron[i + 1]) {
        dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][0]);
        dp[i + 1][j + 1][0] = min(dp[i + 1][j + 1][0], dp[i][j][1] + 1);
      }
      if (!james[i + 1]) {
        dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][1]);
        dp[i + 1][j][1] = min(dp[i + 1][j][1], dp[i][j][0] + 1);
      }
    }
  }

  /*  for (int i = 0; i < 100; ++i) {
      for (int j = 0; j <= 10; ++j) {
        printf("[%d/%d] ", dp[i][j][0], dp[i][j][1]);
      }
      printf("\n");
    }*/

  return min(dp[VMAX - 1][VMAX / 2][0], dp[VMAX - 1][VMAX / 2][1]);
}

void clean() {
  cameron = 0;
  james = 0;
  cameron_activities.clear();
  james_activities.clear();
  for (int i = 0; i <= VMAX; ++i) {
    for (int j = 0; j <= VMAX; ++j) {
      dp[i][j][0] = dp[i][j][1] = INF;
    }
  }
}

int main() {
  cin.sync_with_stdio(false);

  int num_cases;
  cin >> num_cases;

  for (int case_index = 1; case_index <= num_cases; ++case_index) {
    clean();

    int A, B;
    cin >> A >> B;

    int minx = INF;
    for (int i = 0, x, y; i < A; ++i) {
      cin >> x >> y;
      cameron_activities.push_back({x, y});
      minx = min(minx, x);
    }

    for (int i = 0, x, y; i < B; ++i) {
      cin >> x >> y;
      james_activities.push_back({x, y});
      minx = min(minx, x);
    }

    for (int i = 0; i < A; ++i) {
      int x = cameron_activities[i].first - minx;
      int y = cameron_activities[i].second - minx - 1;
      for (int j = x; j <= y; ++j) {
        cameron[j] = true;
        cameron[j + VMAX] = true;
      }
    }

    for (int i = 0; i < B; ++i) {
      int x = james_activities[i].first - minx;
      int y = james_activities[i].second - minx - 1;
      for (int j = x; j <= y; ++j) {
        james[j] = true;
        james[j + VMAX] = true;
      }
    }

    cout << "Case #" << case_index << ": ";

    int sol = solve();
    if (sol % 2) {
      ++sol;
    }
    cout << sol;

    cout << '\n';
  }


  return 0;
}
