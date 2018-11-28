#include <bits/stdc++.h>
using namespace std;

struct lol {
  int cal, e, city;

  lol(int _c = 0, int _e = 0, int _cit = 0) { cal = _c; e = _e; city = _cit; }
};

int i, j, n, q, start, finish, dist[105][105], e[105], s[105];
bool used[105];
double dp[105][105];

void clearAll() {
  memset(dp, 0, sizeof(dp));
  memset(dist, 0, sizeof(dist));
  memset(e, 0, sizeof(e));
  memset(s, 0, sizeof(s));
  memset(used, 0, sizeof(used));
}

double solve(int start, int finish) {
  memset(used, 0, sizeof(used));
  for(i = 0; i <= n + 1; ++i)
    for(j = 0; j <= n + 1; ++j)
      dp[i][j] = 1e18;

  dp[start][start] = 0; used[start] = 1;

  queue<lol> q;
  for(q.push(lol(start, e[start], start)); !q.empty(); q.pop()) {
    int cal = q.front().cal;
    int en = q.front().e;
    int city = q.front().city;

    for(i = 1; i <= n; ++i) {
      if(dist[city][i] == -1 || dist[city][i] > en) continue;
      if(dp[cal][i] <= dp[cal][city] + (double)dist[city][i] / s[cal]) continue;

      dp[cal][i] = dp[cal][city] + (double)dist[city][i] / s[cal];
      q.push(lol(cal, en - dist[city][i], i));
    }

    dp[city][city] = min(dp[city][city], dp[cal][city]);
    cal = city; en = e[cal];

    for(i = 1; i <= n; ++i) {
      if(dist[city][i] == -1 || dist[city][i] > en) continue;
      if(dp[cal][i] <= dp[cal][city] + (double)dist[city][i] / s[cal]) continue;

      dp[cal][i] = dp[cal][city] + (double)dist[city][i] / s[cal];
      q.push(lol(cal, en - dist[city][i], i));
    }
  }

  double ans = 1e18;

  for(i = 1; i <= n; ++i) ans = min(ans, dp[i][finish]);

  return ans;
}

int main() {
  ifstream cin("test1.in");
  ofstream cout("test.out");
  ios_base::sync_with_stdio(0);

  int test, tests;
  cin >> tests;
  for(test = 1; test <= tests; ++test, cout << '\n') {
    clearAll();
    cout << "Case #" << test << ": ";

    cin >> n >> q;
    for(i = 1; i <= n; ++i) cin >> e[i] >> s[i];

    for(i = 1; i <= n; ++i)
      for(j = 1; j <= n; ++j)
        cin >> dist[i][j];

    while(q--) {
      cin >> start >> finish;
      cout << setprecision(6) << fixed << solve(start, finish) << ' ';
    }
  }

  return 0;
}

/*
dp[i][j] = min time to be in j-th city with i-th horse
*/