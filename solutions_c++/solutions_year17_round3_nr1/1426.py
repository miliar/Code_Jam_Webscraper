#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

const int MAXN = 1010;

int N, K;
vector<pair<int, int> > pancakes;

double dp[MAXN][MAXN];
bool found[MAXN][MAXN];

double f(int last, int k) {
  if (last == N || k == 0) {
    return 0.0;
  }
  if (found[last][k]) {
    return dp[last][k];
  }

  double sol = f(last + 1, k);

  if (k == K) {
    sol = max(sol, 1.0 *  pancakes[last].first * pancakes[last].first * M_PI + 2.0 * pancakes[last].first * pancakes[last].second * M_PI + f(last + 1, k - 1));
  } else {
    sol = max(sol, 2.0 * pancakes[last].first * pancakes[last].second * M_PI + f(last + 1, k - 1));
  }
  found[last][k] = true;
  return dp[last][k] = sol;
}



int main(void) {
  int T;
  int test_case = 0;
  scanf("%d", &T);

  while (T--) {
    memset(found, 0, sizeof(found));
    pancakes.resize(0);

    scanf("%d %d", &N, &K);

    int w, h;
    for (int i = 0; i < N; ++i) {
      scanf("%d %d", &w, &h);
      pancakes.push_back(make_pair(w, h));
    }

    sort(pancakes.rbegin(), pancakes.rend());

    printf("Case #%d: %.9lf\n", ++test_case, f(0, K));
  }
  return 0;
}
