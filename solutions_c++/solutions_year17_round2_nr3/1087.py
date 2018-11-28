#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 110;
const double INF = 1000000000000000000.0;
int n;
int e[MAXN];
int s[MAXN];
int d[MAXN][MAXN];

double dp[MAXN][MAXN];

double horse_time(int horse_city_index, int city_start, int city_end) {  
  double horse_distance = 0.0;
  for (int i = horse_city_index; i < city_end; ++i) {
    horse_distance += d[i][i + 1];
  }

  double trip_distance = 0.0;
  for (int i = city_start; i < city_end; ++i) {
    trip_distance += d[i][i + 1];
  }
  
  if (horse_distance > e[horse_city_index]) return INF;
  return trip_distance / s[horse_city_index];
}

double f(int horse_index, int city_index) {
  if (city_index == n - 1) {
    return 0;
  }
  if (dp[horse_index][city_index] >= -0.5) {
    return dp[horse_index][city_index];
  }
  return dp[horse_index][city_index] = min(
      horse_time(horse_index, city_index, city_index + 1) + f(horse_index, city_index + 1),
      horse_time(city_index, city_index, city_index + 1) + f(city_index, city_index + 1));
}

int main(void) {
  int T, test_case = 1;
  
  scanf("%d", &T);

  while (T--) {
    scanf("%d %*d", &n);
    
    for (int i = 0; i < n; ++i) {
      scanf("%d %d", &e[i], &s[i]);
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        scanf("%d", &d[i][j]);
      }
    }
    scanf("%*d %*d");
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        dp[i][j] = -1.0; 
      }
    }

    printf("Case #%d: %.9lf\n", test_case++, f(0, 0));
  }
  
  return 0;
}
