#include <bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')

typedef long long int lld;
const long double PI = acos(-1.0);
const int NMAX = 1000;
const int KMAX = 1000;

int N, K;
vector<pair<int, int> > V;
long double dp[NMAX + 5][KMAX + 5][2];

long double surface(const pair<int, int>& a) {
  return PI * a.first * a.first;
}

long double height(const pair<int, int>& a) {
  return 2 * PI * a.first * a.second;
}

long double solve() {
  for (int i = 1; i <= N; ++i) {
    for (int j = 1; j <= K; ++j) {
      dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][0] + height(V[i]));
      dp[i][j][1] = max(max(dp[i - 1][j][1], dp[i - 1][j - 1][1] + height(V[i])),
                        dp[i - 1][j - 1][0] + height(V[i]) + surface(V[i]));
    }
  }
  return dp[N][K][1];
}

void clean() {
  V.clear();
  V.push_back({0, 0});
  memset(dp, 0, sizeof(dp));
}

int main() {
  cin.sync_with_stdio(false);

  int num_cases;
  cin >> num_cases;

  for (int case_index = 1; case_index <= num_cases; ++case_index) {
    clean();

    cin >> N >> K;
    for (int i = 1, x, y; i <= N; ++i) {
      cin >> x >> y;
      V.push_back({x, y});
    }

    cout << "Case #" << case_index << ": ";

    long double sol = solve();
    cout << fixed << setprecision(10) << sol;

    cout << '\n';
  }


  return 0;
}
